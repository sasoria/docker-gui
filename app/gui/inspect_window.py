import gi.repository.Gtk as Gtk


class InspectWindow(Gtk.Window):
    def __init__(self, container_data):
        Gtk.Window.__init__(self, title="inspect container")
        self.set_border_width(3)
        self.set_default_size(800, 400)

        self.add(self._create_label(container_data))

    def _create_label(self, data):
        label = Gtk.Label()
        #label.set_markup(self.create_inspected_info())
        self._print_container(data)
        return label

    def _create_data_string(self):
        data_string = ""

    def _print_container(self, data):
        for k, v in data.items():
            if isinstance(v, dict):
                self._print_container(v)
            else:
                print("{0}:{1}".format(k, v))

