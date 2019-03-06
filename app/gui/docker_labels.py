import gi.repository.Gtk as Gtk


class ContainerLabel(Gtk.Label):
    def __init__(self, text, docker_container):
        Gtk.Label.__init__(self)
        self.docker_container = docker_container
        self.set_text(text)

    def get_docker_container(self):
        return self.docker_container
