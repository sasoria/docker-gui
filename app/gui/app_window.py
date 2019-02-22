import gi.repository.Gtk as Gtk
import sys
# from gi import require_version
# require_version("GTK", "3.0")


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_border_width(3)
        self.set_default_size(200, 100)

        self.notebook = Gtk.Notebook()
        self.add(self.notebook)

        # Containers
        self.page1 = Gtk.ListBox()
        self.page1.set_border_width(10)
        for container in app.containers:
            self.page1.add(Gtk.Label(container.__str__()))

        # Images
        self.page2 = Gtk.ListBox()
        self.page2.set_border_width(10)
        for image in app.images:
            self.page2.add(Gtk.Label(image.__str__()))

        # TODO : Add inspect command in a button. Should display ports (Networksettings.Ports).

        self.notebook.append_page(self.page1, Gtk.Label("Containers"))
        self.notebook.append_page(self.page2, Gtk.Label("Images"))


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

