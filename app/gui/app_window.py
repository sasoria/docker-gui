import gi.repository.Gtk as Gtk
import sys
# from gi import require_version
# require_version("GTK", "3.0")
from src import app_utils


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_border_width(3)
        self.set_default_size(400, 200)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Containers
        self.page1 = Gtk.ListBox()
        self.page1.set_border_width(10)
        self.page1.set_selection_mode(Gtk.SelectionMode.NONE)
        for container in app.containers:
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

            row.add(box)

            label = Gtk.Label(container.__str__())
            label.set_justify(Gtk.Justification.FILL)
            label.set_line_wrap(True)

            button = Gtk.Button.new_with_label("run")
            button.connect("clicked", self.on_click_run, container)

            box.pack_start(label, True, True, 0)
            box.pack_start(button, True, True, 0)

            self.page1.add(row)

        # Images
        self.page2 = Gtk.ListBox()
        self.page2.set_border_width(10)
        self.page2.set_selection_mode(Gtk.SelectionMode.NONE)
        for image in app.images:
            row = Gtk.ListBoxRow()
            box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

            row.add(box)

            label = Gtk.Label(image.__str__())
            label.set_justify(Gtk.Justification.FILL)
            label.set_line_wrap(True)

            button = Gtk.Button.new_with_label("run")
            button.connect("clicked", self.on_click_run, image)

            box.pack_start(label, True, True, 0)
            box.pack_start(button, True, True, 0)

            self.page2.add(row)

        # TODO : Add inspect command in a button. Should display ports (Networksettings.Ports).

        self.notebook.append_page(self.page1, Gtk.Label("Containers"))
        self.notebook.append_page(self.page2, Gtk.Label("Images"))

    def create_docker_component_row(self, docker_component, on_click):
        row = Gtk.ListBoxRow()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

        row.add(box)

        label = Gtk.Label(docker_component.__str__())
        label.set_justify(Gtk.Justification.FILL)
        label.set_line_wrap(True)

        button = Gtk.Button.new_with_label("run")
        button.connect("clicked", on_click, docker_component)

        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)

        return row

    def on_click_inspect(self, button, container):
        print(container.__str__)
        print(container.id)

    def on_click_run(self, button, image):
        app_utils.execute_cmd("docker run {0}".format(image.__str__()))
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK,
                                   "{0} is running".format(image.__str__()))
        dialog.run()
        print("INFO: dialog closed")

        dialog.destroy()


class Application(Gtk.Application):
    def __init__(self, dockers):
        Gtk.Application.__init__(self)
        self.images = dockers['images']
        self.containers = dockers['containers']

    def do_activate(self):
        win = Window(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


def run(dockers):
    """
    Runs the window as an application.
    :param dockers: a dictionary of images and containers
    :return: exit status
    """
    app = Application(dockers)
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)

