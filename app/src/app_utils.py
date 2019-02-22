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

    return out.decode('utf-8')


def parse_images(out):
    """
    Parses images  from std.out and creates a list of <Image> with its respective attributes.
    :param out: std.out
    :return: a list of images.
    """
    images = []
    for item in out.split("\n"):
        if len(item) == 0:
            # ignoring empty list
        elif item.split()[0] == "REPOSITORY":
            # ignoring header
        else:
            lst = item.split()
            images.append(Image(lst[0], lst[1], lst[2], lst[3]))

    return images


def parse_containers(out):
    """
    Parses containers from st.out and creates a list of <Container> with its respective attributes.
    :param out: std.out
    :return: a list of containers
    """
    containers = []
    for item in out.split("\n"):
        if len(item) == 0:
            # ignoring empty list
        elif item.split()[0] == "CONTAINER":
            # ignoring header
        else:
            lst = item.split()
            containers.append(Container(lst[0], lst[1], lst[-1]))

    return containers


def ls_images():
    """
    Performs docker list(ls) command for images.
    :return: a list of images.
    """
    return parse_images(execute_cmd("docker image ls"))


def ls_containers():
    """
    Performs docker list(ls) command for containers.
    :return: a list of containers.
    """
    return parse_containers(execute_cmd("docker container ls"))


