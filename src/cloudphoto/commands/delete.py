from cloudphoto.service.config import get_bucket_name
from cloudphoto.service.utils import DELIMITER, is_image_exist, get_image_key, is_album_exist


def delete_img(session, album: str, image: str):
    img_key = get_image_key(album, image)
    bucket = get_bucket_name()

    if not is_album_exist(session, bucket, album):
        raise Exception("Album does not exist")

    if not is_image_exist(session, bucket, album, image):
        raise Exception("Image does not exist")

    session.delete_objects(
        Bucket=bucket, Delete={"Objects": [{"Key": img_key}]}
    )


def get_all_images_key(session, bucket: str, album: str):
    list_objects = session.list_objects(
        Bucket=bucket,
        Prefix=album + DELIMITER,
        Delimiter=DELIMITER,
    )["Contents"]
    return [{"Key": img_key.get('Key')} for img_key in list_objects]


def delete_album(session, album: str):
    bucket = get_bucket_name()

    if not is_album_exist(session, bucket, album):
        raise Exception("Album does not exist")

    img_keys = get_all_images_key(session, bucket, album)

    session.delete_objects(Bucket=bucket, Delete={"Objects": img_keys})
