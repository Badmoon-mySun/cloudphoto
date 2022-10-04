import argparse
import sys

from commands.list import list_img, list_albums
from service.initializer import initialize
from service.aws_helper import init_s3_session
from commands import upload_img, download_img

parser = argparse.ArgumentParser()
# parser.add_argument("command", nargs='?', help="test")
subparsers = parser.add_subparsers(help="sub-command help")


def upload(session):
    upload_parser = subparsers.add_parser("upload")
    upload_parser.add_argument("--album", required=True, help="Album name")
    upload_parser.add_argument("--path", default='.', help="Path to image")
    args = vars(parser.parse_args())
    upload_img(session, **args)


def download(session):
    upload_parser = subparsers.add_parser("download")
    upload_parser.add_argument("--album", required=True, help="Album name")
    upload_parser.add_argument("--path", default='.', help="Path to save images")
    args = vars(parser.parse_args())
    download_img(session, **args)


def list_command(session):
    upload_parser = subparsers.add_parser("list")
    upload_parser.add_argument("--album", help="Album name")
    args = vars(parser.parse_args())
    album = args.get('album')
    list_img(session, album) if album else list_albums(session)


COMMANDS_NAME_AND_FUNCTIONS = {
    "upload": upload,
    "download": download,
    "list": list_command,
    "init": initialize,
}


def main():
    sys.tracebacklimit = -1
    try:
        command = sys.argv[1]
    except Exception as e:
        raise Exception("Введите команду")

    function = COMMANDS_NAME_AND_FUNCTIONS.get(command)

    if function != initialize:
        session = init_s3_session()
        function(session)
    else:
        function()


if __name__ == "__main__":
    main()
