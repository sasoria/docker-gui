import gi.repository.Gtk as Gtk
import docker
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
        self.set_default_size(400, 200)
        self.app = app

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Containers
        self.container_page = Gtk.ListBox()
        self.container_page.set_border_width(10)
        self.container_page.set_selection_mode(Gtk.SelectionMode.NONE)
        for container in app.containers:
            row = self.create_row(container, self.on_click_inspect, "inspect")
            self.container_page.add(row)

        # Images
        self.image_page = Gtk.ListBox()
        self.image_page.set_border_width(10)
        self.image_page.set_selection_mode(Gtk.SelectionMode.NONE)
        for image in app.images:
            row = self.create_row(image, self.on_click_run, "run")
            self.image_page.add(row)

        self.notebook.append_page(self.container_page, Gtk.Label("Containers"))
        self.notebook.append_page(self.image_page, Gtk.Label("Images"))

    def create_row(self, docker_component, on_click, button_label):
        row = Gtk.ListBoxRow()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

        row.add(box)

        label = self._create_label(docker_component.__str__())
        button = self._create_button(button_label, docker_component, on_click)

        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)

        return row

    def _create_label(self, label_name):
        label = Gtk.Label(label_name)
        label.set_justify(Gtk.Justification.FILL)
        label.set_line_wrap(True)
        # FIXME : fix signal for label click
        label.connect("activate-link", self.on_click_run, label_name)

        return label

    def _create_button(self, button_label, docker_component, on_click):
        button = Gtk.Button.new_with_label(button_label)
        button.connect("clicked", on_click, docker_component)

        return button

    def on_click_inspect(self, button, container):
        container_string = app_utils.execute_cmd("docker inspect {}".format(container.container_id))
        container_json = json.loads(container_string)

        print(container_json)

        inspect_window = InspectWindow(container_json)
        inspect_window.connect("destroy", Gtk.main_quit)
        inspect_window.show_all()

    def on_click_run(self, button, image):
        # FIXME : check if image is represented correctly
        docker_commands.docker_run(self.app.docker_client, image)
        print(
            "".format(image.)
        )

        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK,
                                   "{0} is running".format(image))
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

