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


def docker_run(docker_client, image):
    try:
        docker_client.containers.run(image)
    except docker.errors.ContainerError:
        print("Error : container is already running")
    except docker.errors.ImageNotFound:
        print("Error : image not found")
    except docker.errors.APIError:
        print("Error : server returned an error")
