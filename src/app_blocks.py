

class Container:
    """Container represents a docker container listed in <docker ps> or
    <docker container ls>"""
    def __init__(self, container_id, name):
        self.container_id = container_id
        self.name = name

    def __str__(self):
        return "Container : " + self.name


class Image:
    """Image represents a docker image listed in <docker image ls>"""
    def __init__(self, name, tag, image_id, size):
        self.name = name
        self.tag = tag
        self.image_id = image_id
        self.size = size

    def __str__(self):
        return self.name



