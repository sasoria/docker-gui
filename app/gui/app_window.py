import gi.repository.Gtk as Gtk
import docker
import sys
from . docker_listboxes import ContainerListBox, ImageListBox
from src import docker_commands
# from gi import require_version
# require_version("GTK", "3.0")


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_border_width(3)
        self.set_default_size(800, 800)
        self.app = app

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Containers
        self.container_paned = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.container_info_listbox = Gtk.ListBox()
        self.container_label_listbox = ContainerListBox(self.container_info_listbox)
        for container in app.containers:
            row = self.container_label_listbox.add_row(container)
            self.container_label_listbox.add(row)

        self.container_paned.add1(self.container_label_listbox)
        self.container_paned.add2(self.container_info_listbox)

        # Images
        self.image_page = ImageListBox(self.app.docker_client, self)
        for image in app.images:
            row = self.image_page.add_row(image)
            self.image_page.add(row)

        self.notebook.append_page(self.container_paned, Gtk.Label("Containers"))
        self.notebook.append_page(self.image_page, Gtk.Label("Images"))


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

