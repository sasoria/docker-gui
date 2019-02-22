

class Container:
    """Container, a docker container listed in <docker ps> or
    <docker container ls>"""
    def __init__(self, container_id, image, name):
        self.container_id = container_id
        self.image = image
        self.name = name

    def __str__(self):
        return "{0} ({1})".format(self.name, self.image)


class Image:
    """Image, a docker image listed in <docker image ls>"""
    def __init__(self, name, tag, image_id, size):
        self.name = name
        self.tag = tag
        self.image_id = image_id
        self.size = size

    def __str__(self):
        return self.name



