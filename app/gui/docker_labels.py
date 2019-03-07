import gi.repository.Gtk as Gtk
from src import docker_commands


class ContainerLabel(Gtk.Label):
    def __init__(self, docker_container):
        Gtk.Label.__init__(self, xalign=0)
        self.docker_container = docker_container
        self.data = docker_commands.inspect(docker_container)
        self.text = "{0} ({1})".format(self.data['Config']['Image'], self.docker_container.name)
        self.set_text(self.text)
        # self.set_justify(Gtk.Justification.LEFT)
        # self.set_line_wrap(True)

    def get_docker_container(self):
        return self.docker_container


class ImageLabel(Gtk.Label):
    def __init__(self, docker_image):
        Gtk.Label.__init__(self, xalign=0)
        self.docker_image = docker_image
        self.text = self.docker_image.tags[0]
        self.set_text(self.text)
        self.set_justify(Gtk.Justification.LEFT)
        self.set_line_wrap(True)

