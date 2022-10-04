import logging
from pathlib import Path

from cloudphoto.service.config import get_bucket_name
from cloudphoto.service.utils import check_album

IMG_EXTENSIONS = [".jpg", ".jpeg", ".png", ".gif"]


def is_image(file):
    return file.is_file() and file.suffix in IMG_EXTENSIONS


def upload_img(session, album: str, path: str):
    path = Path(path)
    check_album(album)
    count = 0

    if not path.is_dir():
        raise Exception(f"{str(path)} directory does not exist")

    for file in path.iterdir():
        if is_image(file):
            try:
                print(f"{file.name} image uploading...")
                key = f"{album}/{file.name}"
                session.upload_file(str(file), get_bucket_name(), key)
                count += 1
            except Exception as ex:
                logging.warning(ex)

    if not count:
        raise Exception(f"There are no images with extensions in the specified folder, allowed: {IMG_EXTENSIONS}")
