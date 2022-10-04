import argparse
import sys

from .commands import list_img, list_albums, delete_img, delete_album, make_site
from .commands import upload_img, download_img
from .service.aws_helper import init_s3_session
from .service.initializer import initialize

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help="sub-command help")

upload_parser = subparsers.add_parser("upload")
upload_parser.add_argument("--album", required=True, help="Album name")
upload_parser.add_argument("--path", default='.', help="Path to image")

download_parser = subparsers.add_parser("download")
download_parser.add_argument("--album", required=True, help="Album name")
download_parser.add_argument("--path", default='.', help="Path to save images")

list_parser = subparsers.add_parser("list")
list_parser.add_argument("--album", help="Album name")

delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("--album", required=True, help="Album name")
delete_parser.add_argument("--photo", help="Image name")

subparsers.add_parser("mksite")

subparsers.add_parser("init")


def upload(session, **kwargs):
    upload_img(session, **kwargs)


def download(session, **kwargs):
    download_img(session, **kwargs)


def list_command(session, album):
    list_img(session, album) if album else list_albums(session)


def delete(session, album, photo):
    delete_img(session, album, photo) if photo else delete_album(session, album)


def mksite(session):
    make_site(session)


def init():
    initialize()


COMMANDS_NAME_AND_FUNCTIONS = {
    "upload": upload,
    "download": download,
    "list": list_command,
    "delete": delete,
    "mksite": mksite,
    "init": init,
}


def main():
    sys.tracebacklimit = -1

    if len(sys.argv) < 2:
        parser.error("Введите команду")

    command = sys.argv[1]
    function = COMMANDS_NAME_AND_FUNCTIONS.get(command)

    if function != init:
        session = init_s3_session()
        function(session, **vars(parser.parse_args()))
        session.close()
    else:
        function()


if __name__ == "__main__":
    main()
