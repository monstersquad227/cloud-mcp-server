from alibabacloud_mse20190531.client import Client as Mse20190531Client
from alibabacloud_mse20190531 import models as mse_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def get_nacos_instance(
        self,
        region_id: str,
        instance_id: str,
        acl_switch: bool = False,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"mse.{region_id}.aliyuncs.com"
        client = Mse20190531Client(config)
        request = mse_models.QueryClusterDetailRequest(
            instance_id=instance_id,
            acl_switch=acl_switch,
            accept_language="zh",
        )
        resp = client.query_cluster_detail(request)
        return resp.body.to_map()
