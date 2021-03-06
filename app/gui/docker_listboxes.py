import gi.repository.Gtk as Gtk
from . docker_labels import ContainerLabel, ImageLabel
from ..src import docker_commands


class ContainerListBox(Gtk.ListBox):
    def __init__(self, info_listbox, window, docker_client):
        Gtk.ListBox.__init__(self)
        self.set_border_width(10)
        self.connect("row-activated", self.on_click_inspect)
        self.info_listbox = info_listbox
        self.docker_client = docker_client
        self.window = window

    def add_row(self, container):
        row = Gtk.ListBoxRow()
        box = self._create_box(ContainerLabel(container), container)
        row.add(box)
        self.add(row)

    def _create_box(self, label, container):
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        box.pack_start(label, True, True, 0)
        box.pack_start(self._create_button(container), False, True, 1)

        return box

    def _create_button(self, container):
        kill_button = Gtk.Button.new_with_label("kill")
        kill_button.connect("clicked", self.on_click_kill, container)

        return kill_button

    def _kill_dialog(self, message):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, message)
        dialog.run()
        dialog.destroy()

    def on_click_kill(self, widget, container):
        docker_commands.kill(container)
        message = "{0} has terminated.".format(container)
        self._kill_dialog(message)

        self.clear_labels()
        self.update_containers()

    def on_click_inspect(self, listbox, listbox_row):
        label = listbox_row.get_child().get_children()[0]
        container = label.get_docker_container()

        self.info_listbox.remove_rows()
        self.info_listbox.create_rows(container)
        self.info_listbox.show_labels()

    def update_containers(self):
        """ Runs docker list_containers and updates this GtkWidget. """
        for container in docker_commands.list_containers(self.docker_client): # FIXME add docker client to this
            self.add_row(container)

        self.show_labels()

    def clear_labels(self):
        """ Removes all container labels from this GtkWidget and updates this GtkWidget. """
        for row in self:
            self.remove(row)

        self.show_labels()

    def show_labels(self):
        """ Displays any new GtkWidgets added to this. """
        self.show_all()


class ContainerInfoListBox(Gtk.ListBox):
    def __init__(self):
        Gtk.ListBox.__init__(self)
        self.set_margin_left(10)
        self.set_margin_top(10)

    def create_rows(self, container):
        """
        Creates listbox rows with information about the container
        :param container: docker container
        """
        container_info = {
            'id': docker_commands.inspect(container)['Id'],
            'created': docker_commands.inspect(container)['Created'],
            'path': docker_commands.inspect(container)['Path'],
            'status': docker_commands.inspect(container)['State']['Status'],
            'name': docker_commands.inspect(container)['Name'],
            'mounts': docker_commands.inspect(container)['Mounts'],
            'user': docker_commands.inspect(container)['Config']['User'],
            'hostname': docker_commands.inspect(container)['Config']['Hostname'],
            'domainname': docker_commands.inspect(container)['Config']['Domainname'],
            'volumes': docker_commands.inspect(container)['Config']['Volumes'],
            'ipaddress': docker_commands.inspect(container)['NetworkSettings']['IPAddress']
        }

        for key, value in container_info.items():
            self.add(Gtk.Label("{0} : {1}".format(key, value), xalign=0))

    def remove_rows(self):
        """ Clears the info_listbox for all listbox rows if there is a header row. """
        if self.get_row_at_index(0):
            for row in self:
                row.destroy()

    def show_labels(self):
        """ Redraws the widget in info_listbox, the right side pane with information of each container. """
        self.show_all()


class ImageListBox(Gtk.ListBox):
    def __init__(self, docker_client, window, container_labelbox, image_infobox):
        Gtk.ListBox.__init__(self)
        self.set_border_width(10)
        # self.set_selection_mode(Gtk.SelectionMode.NONE)
        self.docker_client = docker_client
        self.window = window
        self.container_labelbox = container_labelbox
        self.image_infobox = image_infobox
        self.connect("row-activated", self.on_click_show_dockerfile)

    def add_row(self, image):
        row = Gtk.ListBoxRow()
        box = self._create_box(ImageLabel(image), image)
        row.add(box)
        self.add(row)

    def _create_box(self, label, image):
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=20)
        box.pack_start(label, True, True, 0)
        box.pack_start(self._create_button(image), False, True, 0)

        return box

    def _create_button(self, image):
        run_button = Gtk.Button.new_with_label("run")
        run_button.connect("clicked", self.on_click_run, image)

        return run_button

    def _run_dialog(self, message):
        dialog = Gtk.MessageDialog(self.window, 0, Gtk.MessageType.INFO, Gtk.ButtonsType.OK, message)
        dialog.run()
        dialog.destroy()

    def on_click_run(self, widget, image):
        image_tag = image.tags[0]
        docker_commands.run(self.docker_client, image_tag)
        message = "{0} is running".format(image_tag)
        self._run_dialog(message)

        self.container_labelbox.clear_labels()
        self.container_labelbox.update_containers()

    def on_click_show_dockerfile(self, listbox, listbox_row):
        label = listbox_row.get_child().get_children()[0]
        image = label.get_docker_image()

        self.image_infobox.remove_rows()
        self.image_infobox.create_rows(image)
        self.image_infobox.show_labels()


class ImageInfoListBox(Gtk.ListBox):
    def __init__(self):
        Gtk.ListBox.__init__(self)
        self.set_selection_mode(Gtk.SelectionMode.NONE)
        self.set_margin_left(10)
        self.set_margin_top(10)

    def create_rows(self, image):
        """
        Creates listbox rows with the dockerfile of the selected image.
        :param image: docker image
        """
        dockerfile = docker_commands.dockerfile_from_image(image)

        for line in dockerfile.splitlines():
            self.add(Gtk.Label("{0}".format(line), xalign=0))

    def remove_rows(self):
        """ Clears the info_listbox for all listbox rows if it is not empty. """
        if self.get_row_at_index(0):
            for row in self:
                row.destroy()

    def show_labels(self):
        """ Redraws the widget in info_listbox, the right side pane with the dockerfile. """
        self.show_all()

