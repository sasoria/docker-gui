import gi.repository.Gtk as Gtk
import json
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

        label = self.create_label(docker_component.__str__())
        button = self.create_button(button_label, docker_component, on_click)

        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)

        return row

    def create_label(self, label_name):
        label = Gtk.Label(label_name)
        label.set_justify(Gtk.Justification.FILL)
        label.set_line_wrap(True)

        return label

    def create_button(self, button_label, docker_component, on_click):
        button = Gtk.Button.new_with_label(button_label)
        button.connect("clicked", on_click, docker_component)

        return button

    def on_click_inspect(self, button, container):
        container_string = app_utils.execute_cmd("docker inspect {}".format(container.container_id))
        container_json = json.loads(container_string)
        # TODO : implement a new gtk window that displays

        for item in container_json:
            for j in item:
                print(j)

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

