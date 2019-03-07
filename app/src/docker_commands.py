import subprocess
import docker
import sys


def execute_cmd(cmd):
    """
    Executes a command <cmd> as a subprocess.
    :param cmd: given command.
    :return: std.out
    """
    subproc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = subproc.communicate()

    if err:
        print("Error : {0}".format(err))
        sys.exit(1)

    return out.decode('utf-8')


def run(docker_client, image):
    """
    Runs a docker image as a container.
    :param docker_client: docker sdk client
    :param image: docker image
    :return: container created from the image
    """
    try:
        container = docker_client.containers.run(image, detach=True)
    except docker.errors.ContainerError:
        print("Error : container is already running")
    except docker.errors.ImageNotFound:
        print("Error : image not found")
    except docker.errors.APIError:
        print("Error : server returned an api error")

    return container


def inspect(container):
    """
    Inspects a docker container. This is not equivalent to <docker inspect>,
    because it lacks some information (See SDK documentation for details).
    :param container: container to be inspected
    :return: representation of the container in a dict
    """

    if container is None:
        print("Error : missing a container")
        return None

    return container.attrs


def list_images(docker_client):
    """
    Lists docker images.
    :param docker_client: docker sdk client
    :return: a list of images
    """
    try:
        images = docker_client.images.list()
    except docker.errors.APIError:
        print("Error : server returned an api Error")
    except ConnectionError:
        print("test")

    return images


def list_containers(docker_client):
    """
    Lists docker containers.
    :param docker_client: docker sdk client
    :return: a list of containers
    """
    try:
        containers = docker_client.containers.list()
    except docker.errors.APIError:
        print("Error : server returned an api Error")

    return containers


def kill(container):
    try:
        container.kill()
    except docker.errors.APIError:
        print("Error : server returned an api Error")
