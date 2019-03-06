import gi.repository.Gtk as Gtk


class InspectWindow(Gtk.Window):
    def __init__(self, data):
        Gtk.Window.__init__(self, title="Info")
        self.set_border_width(3)
        self.set_default_size(800, 400)
        self.listbox = Gtk.ListBox()
        #self.scrolled_window = Gtk.ScrolledWindow()

        for label in self._create_labels(data):
            self.listbox.add(label)

        #self.viewport.add(self.listbox)
        #self.listbox.add(self.sw)
        #self.scrolled_window.add.with_viewport(self.listbox)
        #self.add(self.sw)
        self.add(self.listbox)

    def _create_labels(self, data):
        labels = []
        self._print_container(data, labels)

        return labels

    def _print_container(self, data, labels):
        for k, v in data.items():
            if isinstance(v, dict):
                labels.append(Gtk.Label(k))
                print("{0}: ".format(k))
                self._print_container(v, labels)
            else:
                print("{0}:{1}".format(k, v))
                labels.append(Gtk.Label("{0}:{1}".format(k, v)))
