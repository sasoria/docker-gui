import gi.repository.Gtk as Gtk
from src import docker_commands


class ContainerLabel(Gtk.Label):
    """ A container label displays the name of a container and the image it is running. """
    def __init__(self, docker_container):
        Gtk.Label.__init__(self, xalign=0)
        self.docker_container = docker_container
        self.data = docker_commands.inspect(docker_container)
        self.text = "{0} ({1})".format(self.data['Config']['Image'], self.docker_container.name)
        self.set_text(self.text)

    def get_docker_container(self):
        return self.docker_container


class ImageLabel(Gtk.Label):
    """ An ImageLabel displays the image tag of an image. """
    def __init__(self, docker_image):
        Gtk.Label.__init__(self, xalign=0)
        self.docker_image = docker_image
        self.text = self.docker_image.tags[0]
        self.set_text(self.text)

    def get_docker_image(self):
        return self.docker_image

