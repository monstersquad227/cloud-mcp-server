from alibabacloud_mse20190531.client import Client as Mse20190531Client
from alibabacloud_mse20190531 import models as mse_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def list_nacos_services(
        self,
        region_id: str,
        instance_id: str,
        page_num: int = 1,
        page_size: int = 10,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
        has_ip_count: str = None,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"mse.{region_id}.aliyuncs.com"
        client = Mse20190531Client(config)
        request = mse_models.ListAnsServicesRequest(
            region_id=region_id,
            instance_id=instance_id,
            page_num=page_num,
            page_size=page_size,
            service_name=service_name,
            group_name=group_name,
            namespace_id=namespace_id,
            has_ip_count=has_ip_count,
            accept_language="zh",
        )
        resp = client.list_ans_services(request)
        return resp.body.to_map()
