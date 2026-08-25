from alibabacloud_mse20190531.client import Client as Mse20190531Client
from alibabacloud_mse20190531 import models as mse_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def list_nacos_instances(
        self,
        region_id: str,
        page_num: int = 1,
        page_size: int = 10,
        cluster_alias_name: str = None,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"mse.{region_id}.aliyuncs.com"
        client = Mse20190531Client(config)
        request = mse_models.ListClustersRequest(
            region_id=region_id,
            page_num=page_num,
            page_size=page_size,
            cluster_alias_name=cluster_alias_name,
            accept_language="zh",
        )
        resp = client.list_clusters(request)
        result = resp.body.to_map()
        data = result.get("Data") or []
        result["Data"] = [
            item for item in data if item.get("ClusterType") == "Nacos-Ans"
        ]
        return result
