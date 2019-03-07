import gi.repository.Gtk as Gtk
from . docker_labels import ContainerLabel, ImageLabel
from src import docker_commands


class ContainerListBox(Gtk.ListBox):
    def __init__(self, info_listbox, paned):
        Gtk.ListBox.__init__(self)
        self.set_border_width(10)
        self.connect("row-activated", self.on_click_inspect)
        self.info_listbox = info_listbox
        self.paned = paned

    def add_row(self, container):
        row = Gtk.ListBoxRow()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)
        label = ContainerLabel(container)
        box.pack_start(label, True, True, 0)
        row.add(box)

        return row

    def on_click_inspect(self, listbox, container):
        row = listbox.get_selected_row()
        label = row.get_child().get_children()[0]
        container = label.get_docker_container()
        print(label.get_label())
        print(container.id)
        container_data = docker_commands.inspect(container)

        # remove old row
        if self.info_listbox.get_row_at_index(0):
            for row in self.info_listbox:
                row.destroy()

        # add header
        self.info_listbox.add(Gtk.Label(container_data['Config']['Image']))

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
            self.info_listbox.add(Gtk.Label("{0} : {1}".format(key, value), xalign=0))


        # update GtkWidget
        self.info_listbox.show_all()

    def get_docker_container(self):
        return self.docker_container


class ImageListBox(Gtk.ListBox):
    def __init__(self, docker_client, window):
        Gtk.ListBox.__init__(self)
        self.set_border_width(10)
        self.set_selection_mode(Gtk.SelectionMode.NONE)
        self.docker_client = docker_client
        self.window = window

    def add_row(self, image):
        row = Gtk.ListBoxRow()
        box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=200)

        row.add(box)

        label = ImageLabel(image)
        button = Gtk.Button.new_with_label("run")
        button.connect("clicked", self.on_click_run, image)

        box.pack_start(label, True, True, 0)
        box.pack_start(button, True, True, 0)

        return row

    def on_click_run(self, widget, image):
        image_tag = image.tags[0]
        docker_commands.run(self.docker_client, image_tag)
        # FIXME : throws <TypeError: could not convert value for property `transient_for'
        # from ImageListBox to GtkWindow>. Possiply beacuse it lacks access to a Gtk.Window
        dialog = Gtk.MessageDialog(self.window,
                                   0,
                                   Gtk.MessageType.INFO,
                                   Gtk.ButtonsType.OK,
                                   "{0} is running".format(image_tag)
                                   )
        dialog.run()
        dialog.destroy()

        # FIXME : refresh and add container to container page (1?) need access too container_listbox
        # self.show_all()
