import argparse
import docker
#from src import app_utils


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
        for image in docker_client.images.list():
            print(image)
        exit(0)

    if args.c:
        print("containers : ")
        for container in docker_client.images.list():
            print(container)
        exit(0)

    if args.v:
        print("verbose mode on")

    return {
        'images': docker_client.images.list(),
        'containers': docker_client.containers.list()
    }


def main():
    docker_client = docker.from_env()
    args = read_args()
    dockers = process_args(args, docker_client)
    _gui = __import__("gui.app_window", fromlist=['app_window'])
    _gui.run(dockers)


if __name__ == "__main__":
    main()
