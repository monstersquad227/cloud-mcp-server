from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def describe_instances(
        self,
        region_id: str,
        page_number: int = 1,
        page_size: int = 10,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"ecs.{region_id}.aliyuncs.com"
        client = Ecs20140526Client(config)
        request = ecs_models.DescribeInstancesRequest(
            region_id=region_id,
            page_number=page_number,
            page_size=page_size,
        )
        resp = client.describe_instances(request)
        return resp.body.to_map()
