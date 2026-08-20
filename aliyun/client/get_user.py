from alibabacloud_ram20150501.client import Client as Ram20150501Client
from alibabacloud_ram20150501 import models as ram_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def get_user(self, user_name: str):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
        )
        config.endpoint = "ram.aliyuncs.com"
        client = Ram20150501Client(config)
        request = ram_models.GetUserRequest(user_name=user_name)
        resp = client.get_user(request)
        return resp.body.to_map()
