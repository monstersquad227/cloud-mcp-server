from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def describe_security_group_attribute(
        self,
        region_id: str,
        security_group_id: str,
        direction: str = "all",
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"ecs.{region_id}.aliyuncs.com"
        client = Ecs20140526Client(config)
        request = ecs_models.DescribeSecurityGroupAttributeRequest(
            region_id=region_id,
            security_group_id=security_group_id,
            direction=direction,
        )
        resp = client.describe_security_group_attribute(request)
        return resp.body.to_map()
