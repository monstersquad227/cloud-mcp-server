from alibabacloud_mse20190531.client import Client as Mse20190531Client
from alibabacloud_mse20190531 import models as mse_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def get_nacos_config(
        self,
        region_id: str,
        instance_id: str,
        data_id: str,
        group: str,
        namespace_id: str = None,
        beta: bool = False,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"mse.{region_id}.aliyuncs.com"
        client = Mse20190531Client(config)
        request = mse_models.GetNacosConfigRequest(
            instance_id=instance_id,
            data_id=data_id,
            group=group,
            namespace_id=namespace_id,
            beta=beta,
            accept_language="zh",
        )
        resp = client.get_nacos_config(request)
        return resp.body.to_map()
