import gi.repository.Gtk as Gtk
import json
import sys
from src import docker_commands
# from gi import require_version
# require_version("GTK", "3.0")
from . inspect_window import InspectWindow


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_border_width(3)
        self.set_default_size(800, 800)
        self.app = app

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        self.container_paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)

        # Containers
        self.container_listbox = Gtk.ListBox()
        self.container_listbox.set_border_width(10)
        self.container_info_listbox = Gtk.ListBox()
        for container in app.containers:
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

            row.add(box)

            label = self._create_label("{0} ({1})".format(container.attrs['Config']['Image'], container.name))

            box.pack_start(label, True, True, 0)
            self.container_listbox.add(row)

        self.container_paned.add1(self.container_listbox)
        self.container_paned.add2(self.container_info_listbox)

        # Images
        self.image_page = Gtk.ListBox()
        self.image_page.set_border_width(10)
        self.image_page.set_selection_mode(Gtk.SelectionMode.NONE)
        for image in app.images:
            #row = self._create_row(image, self.on_click_run, "run")
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

            row.add(box)

            label = self._create_label(image.tags[0])
            button = self._create_button("run", image, self.on_click_run)

            box.pack_start(label, True, True, 0)
            box.pack_start(button, True, True, 0)
            self.image_page.add(row)

        self.notebook.append_page(self.container_paned, Gtk.Label("Containers"))
        self.notebook.append_page(self.image_page, Gtk.Label("Images"))

    def _create_label(self, label_name):
        label = Gtk.Label(label_name)
        label.set_justify(Gtk.Justification.LEFT)
        label.set_line_wrap(True)

        return label

    def _create_button(self, button_label, docker_component, on_click):
        button = Gtk.Button.new_with_label(button_label)
        button.connect("clicked", on_click, docker_component)

        return button

    def on_click_inspect(self, button, container):
        container_data = docker_commands.inspect(container)

        inspect_window = InspectWindow(container_data)
        inspect_window.connect("destroy", Gtk.main_quit)
        inspect_window.show_all()

    def on_click_run(self, button, image):
        image_tag = image.tags[0]
        docker_commands.run(self.app.docker_client, image_tag)
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK,
                                   "{0} is running".format(image_tag))
        dialog.run()
        print("INFO: dialog closed")

        dialog.destroy()


class Application(Gtk.Application):
    def __init__(self, dockers, docker_client):
        Gtk.Application.__init__(self)
        self.images = dockers['images']
        self.containers = dockers['containers']
        self.docker_client = docker_client

    def do_activate(self):
        win = Window(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


def run(dockers, docker_client):
    """
    Runs the window as an application.
    :param dockers: a dictionary of images and containers
    :param docker_client: docker sdk client
    :return: exit status
    """
    app = Application(dockers, docker_client)
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)

