from alibabacloud_ecs20140526.client import Client as Ecs20140526Client
from alibabacloud_ecs20140526 import models as ecs_models
from alibabacloud_tea_openapi import models as open_api_models

from .base import AliyunBaseClient


class AliyunClient(AliyunBaseClient):
    def revoke_security_group(
        self,
        region_id: str,
        security_group_id: str,
        ip_protocol: str | None = None,
        port_range: str | None = None,
        source_cidr_ip: str | None = None,
        source_group_id: str | None = None,
        policy: str | None = None,
        priority: str | None = None,
        nic_type: str | None = None,
        security_group_rule_id: str | None = None,
    ):
        config = open_api_models.Config(
            access_key_id=self.config.access_key_id,
            access_key_secret=self.config.access_key_secret,
            region_id=region_id,
        )
        config.endpoint = f"ecs.{region_id}.aliyuncs.com"
        client = Ecs20140526Client(config)
        permissions = None
        if ip_protocol is not None:
            permissions = [
                ecs_models.RevokeSecurityGroupRequestPermissions(
                    ip_protocol=ip_protocol,
                    port_range=port_range,
                    source_cidr_ip=source_cidr_ip,
                    source_group_id=source_group_id,
                    policy=policy,
                    priority=priority,
                    nic_type=nic_type,
                )
            ]
        request = ecs_models.RevokeSecurityGroupRequest(
            region_id=region_id,
            security_group_id=security_group_id,
            permissions=permissions,
            security_group_rule_id=[security_group_rule_id] if security_group_rule_id else None,
        )
        resp = client.revoke_security_group(request)
        return resp.body.to_map()
