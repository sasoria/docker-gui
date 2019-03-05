import argparse
import docker
from src import docker_commands


def read_args():
    """
    Reads arguments from the command line.
    :return: parsed arguments
    """
    parser = argparse.ArgumentParser()

    parser.add_argument("-i",
                        help="list docker images",
                        action="store_true")

    parser.add_argument("-c",
                        help="list docker containers",
                        action="store_true")

    parser.add_argument("-v",
                        help="verbose mode on",
                        action="store_true")

    return parser.parse_args()


def process_args(args, docker_client):
    """
    Processes arguments, then executes the appropriate command.
    :param args: parsed arguments
    :param docker_client: docker sdk client
    :return: a dictionary of docker containers and docker images.
    """

    if args.i:
        print("images : ")
        for image in docker_commands.list_images(docker_client):
            print(image.tag[0])
        exit(0)

    if args.c:
        print("containers : ")
        for container in docker_commands.list_containers(docker_client):
            print(container)
        exit(0)

    if args.v:
        print("verbose mode on")

    return {
        'images': docker_commands.list_images(docker_client),
        'containers': docker_commands.list_containers(docker_client)
    }


def main():
    args = read_args()
    docker_client = docker.from_env()
    dockers = process_args(args, docker_client)
    _gui = __import__("gui.app_window", fromlist=['app_window'])
    _gui.run(dockers, docker_client)


if __name__ == "__main__":
    main()
