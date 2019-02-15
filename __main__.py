import argparse
from src import app_utils


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


def process_args(args):
    """
    Processes arguments, then executes the appropriate command.
    :param args:
    :return: a list of either docker containers or docker images
    """
    docker_list = []

    """if args.i:"""
    if 1:
        docker_list = app_utils.parse_images(
            app_utils.execute_cmd("docker image ls"))

    if args.c:
        docker_list = app_utils.parse_containers(
            app_utils.execute_cmd("docker container ls"))

    return docker_list


def main():
    args = read_args()
    dockers = process_args(args)

    _gui = __import__("gui.app_window", fromlist=['app_window'])
    _gui.run(dockers)


if __name__ == "__main__":
    main()


