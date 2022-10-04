from pathlib import Path

from cloudphoto.service.config import get_bucket_name
from cloudphoto.service.utils import DELIMITER, is_album_exist


def list_img(session, album):
    bucket = get_bucket_name()

    if not is_album_exist(session, bucket, album):
        raise Exception(f"Album '{album}' does not exist")

    list_objects = session.list_objects(
        Bucket=bucket,
        Prefix=album + DELIMITER,
        Delimiter=DELIMITER
    )
    images = []
    for key in list_objects["Contents"]:
        images.append(Path(key["Key"]).name)

    if not len(images):
        raise Exception("Нет картинок.")

    print(f"Images in album {album}:")
    for photo_name in images:
        print(f"# {photo_name}")


def list_albums(session):
    bucket = get_bucket_name()
    list_objects = session.list_objects(Bucket=bucket)
    albums = set()
    if "Contents" in list_objects:
        for key in list_objects["Contents"]:
            albums.add(Path(key["Key"]).parent)

    if not len(albums):
        raise Exception(f"Is no albums in {bucket}")

    print(f"Albums in bucket {bucket}:")
    for album in albums:
        print(f"# {album}")
