import gi.repository.Gtk as Gtk
import docker
import sys
from . docker_listboxes import ContainerListBox, ContainerInfoListBox, ImageListBox, ImageInfoListBox
# from gi import require_version
# require_version("GTK", "3.0")


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_border_width(3)
        self.set_default_size(800, 800)
        self.app = app

        # Notebook
        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Container
        self.container_page = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.container_infobox = ContainerInfoListBox()
        self.container_labelbox = ContainerListBox(self.container_infobox, self, self.app.docker_client)

        for container in app.containers:
            self.container_labelbox.add_row(container)

        self.container_page.add1(self.container_labelbox)
        self.container_page.add2(self.container_infobox)

        # Images
        self.image_page = Gtk.Paned.new(Gtk.Orientation.HORIZONTAL)
        self.image_infobox = ImageInfoListBox()
        self.image_labelbox = ImageListBox(self.app.docker_client, self, self.container_labelbox, self.image_infobox)

        for image in app.images:
            self.image_labelbox.add_row(image)

        self.scrollable_image_info = Gtk.ScrolledWindow()
        self.scrollable_image_info.add_with_viewport(self.image_infobox)

        self.image_page.add1(self.image_labelbox)
        self.image_page.add2(self.scrollable_image_info)

        # add pages
        self.notebook.append_page(self.container_page, Gtk.Label("Containers"))
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

