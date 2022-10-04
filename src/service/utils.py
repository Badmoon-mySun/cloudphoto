DELIMITER = '/'


def check_album(album: str):
    if album.count("/"):
        raise Exception("album cannot contain '/'")


def is_album_exist(session, bucket, album):
    list_objects = session.list_objects(
        Bucket=bucket,
        Prefix=album + DELIMITER,
        Delimiter=DELIMITER,
    )
    if "Contents" in list_objects:
        for _ in list_objects["Contents"]:
            return True
    return False
