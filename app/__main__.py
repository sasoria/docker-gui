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
    :param args: parsed arguments
    :return: a dictionary of docker containers and docker images.
    """

    if args.i:
        print("images : ")
        for image in app_utils.ls_images():
            print(image.__str__())
            exit(0)

    if args.c:
        print("containers : ")
        for container in app_utils.ls_containers():
            print(container.__str__())
            exit(0)

    if args.v:
        print("verbose mode on")

    return {
        'images': app_utils.ls_images(),
        'containers': app_utils.ls_containers()
    }


def main():
    args = read_args()
    dockers = process_args(args)
    _gui = __import__("gui.app_window", fromlist=['app_window'])
    _gui.run(dockers)


if __name__ == "__main__":
    main()

