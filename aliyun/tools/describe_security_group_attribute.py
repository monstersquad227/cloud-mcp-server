from aliyun.client.describe_security_group_attribute import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("describe_aliyun_security_group_attribute")
    def describe_security_group_attribute(
        region_id: str,
        security_group_id: str,
        direction: str = "all",
    ) -> dict:
        """查询阿里云安全组和组内规则信息

        Args:
            region_id: 安全组所属地域 ID, 示例值: cn-hangzhou.
            security_group_id: 安全组 ID.
            direction: 安全组规则方向, 取值: egress(出方向)/ingress(入方向)/all(全部), 默认值 all.
        """
        return client.describe_security_group_attribute(
            region_id=region_id,
            security_group_id=security_group_id,
            direction=direction,
        )
