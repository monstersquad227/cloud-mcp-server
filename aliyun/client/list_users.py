from alibabacloud_ram20150501.client import Client as Ram20150501Client
from alibabacloud_ram20150501 import models as ram_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def list_users(self, marker: str | None = None, max_items: int = 100):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
        )
        config.endpoint = "ram.aliyuncs.com"
        client = Ram20150501Client(config)
        request = ram_models.ListUsersRequest(
            marker=marker,
            max_items=max_items,
        )
        resp = client.list_users(request)
        return resp.body.to_map()
