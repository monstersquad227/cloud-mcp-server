import os

from alibabacloud_bssopenapi20171214.client import Client as BssOpenApi20171214Client
from alibabacloud_tea_openapi import models as open_api_models
from dotenv import load_dotenv

load_dotenv()


class AliyunBaseClient:
    def __init__(self):
        config = open_api_models.Config(
            access_key_id=os.getenv("ALIYUN_ACCESS_KEY_ID"),
            access_key_secret=os.getenv("ALIYUN_ACCESS_KEY_SECRET"),
            region_id=os.getenv("ALIYUN_REGION_ID"),
        )
        self.client = BssOpenApi20171214Client(config)
