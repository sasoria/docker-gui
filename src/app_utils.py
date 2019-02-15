import subprocess
from .app_blocks import Container
from .app_blocks import Image


def execute_cmd(cmd):
    """
    Executes a command <cmd> as a subprocess.
    :param cmd: given command.
    :return: std.out
    """
    subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE)
    out, err = subproc.communicate()

    return out.decode()


def parse_images(out):
    """
    Parses images  from std.out and creates a list of <Image> with their respective attributes.
    :param out: std.out
    :return: a list of images.
    """
    images = []
    for item in out.split("\n"):
        if len(item) == 0:
            print("ignoring empty list")
        elif item.split()[0] == "REPOSITORY":
            print("ignoring header")
        else:
            lst = item.split()
            images.append(Image(lst[0], lst[1], lst[2], lst[3]))

    return images


def parse_containers(out):
    """
    Parses containers from st.out and creates a list of <Container> with their respective attributes.
    :param out: std.out
    :return: a list of containers
    """
    containers = []
    for item in out.split("\n"):
        if len(item) == 0:
            print("ignoring empty list")
        elif item.split()[0] == "CONTAINER":
            print("ignoring header")
        else:
            lst = item.split()
            containers.append(Container(lst[0], lst[-1]))

    return containers


"""

    for container in container_list:
        print("{0}".format(container.__str__()))

    for image in images:
        print("*{0}".format(image.__str__()))

"""
