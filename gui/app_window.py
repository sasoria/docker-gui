import gi.repository.Gtk as Gtk
import sys
# from gi import require_version
# require_version("GTK", "3.0")


class Window(Gtk.ApplicationWindow):
    def __init__(self, app):
        print("{0}".format(app.args))

        Gtk.Window.__init__(self, title="dockger-gui", application=app)
        self.set_default_size(200, 100)
        # TODO : Add Notebook
        hbox = Gtk.Box(spacing=10)
        hbox.set_homogeneous(False)
        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_left.set_homogeneous(False)
        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        # TODO : add both images and containers
        for arg in app.args:
            vbox_left.pack_start(Gtk.Label(arg), True, True, 0)

        self.add(hbox)


class Application(Gtk.Application):
    def __init__(self, args):
        Gtk.Application.__init__(self)
        self.args = args

    def do_activate(self):
        win = Window(self)
        win.show_all()

    def do_startup(self):
        Gtk.Application.do_startup(self)


def run(args):
    """
    Runs the window as an application, passes a list of docker container/images.
    :param args:
    :return:
    """
    app = Application(args)
    exit_status = app.run(sys.argv)
    sys.exit(exit_status)
