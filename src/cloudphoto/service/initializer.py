from botocore.exceptions import ClientError

from .aws_helper import create_s3_session
from .config import create_config

DEFAULT_ENDPOINT = "https://storage.yandexcloud.net"
DEFAULT_REGION = "ru-central1"


def initialize():
    access_key = input("access key: ")
    secret_access_key = input("secret access key: ")
    bucket_name = input("bucket name: ")
    try:
        s3 = create_s3_session(access_key, secret_access_key, DEFAULT_ENDPOINT, DEFAULT_REGION)
        s3.create_bucket(Bucket=bucket_name, ACL='public-read-write')
    except ClientError as clientError:
        if clientError.response["Error"]["Code"] != "BucketAlreadyOwnedByYou":
            raise clientError

    create_config(access_key=access_key, secret_key=secret_access_key, bucket_name=bucket_name)
