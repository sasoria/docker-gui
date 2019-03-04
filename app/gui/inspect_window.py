import gi.repository.Gtk as Gtk


class InspectWindow(Gtk.Window):
    def __init__(self, container_json):
        Gtk.Window.__init__(self, title="inspect container")
        self.set_border_width(3)
        self.set_default_size(800, 400)
        self.container_json = container_json

        self.add(self.create_label())

    def create_label(self):
        label = Gtk.Label()
        label.set_markup(self.create_markup())
        print(self.create_markup())

        return label

    def create_markup(self):
        text = ""

#        for item in self.container_json:
#            for elem in item:
#                # print(elem)
#                text += "<b>{0}</b>: \n".format(elem)
#               # for e in elem:
#               #     text += "{0}".format(e)

        for item in self.container_json:
            if isinstance(item, dict):
                for k,v in item.items():
                    if isinstance(v, dict):
                        text += "<b>{0}: </b>: \n".format(k)
                        for i, j in v.items():
                            text += "\t<b>{0}</b>: {1}\n".format(i, j)
                    else:
                        text += "<b>{0}</b>: {1}\n".format(k, v)

        # print("Id: {0}".format(self.container_json[0]['Id']))
        # print("Created: {0}".format(self.container_json[0]['Created']))

        return text
