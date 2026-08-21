from aliyun.client.describe_security_groups import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("describe_aliyun_security_groups")
    def describe_security_groups(
        region_id: str,
        page_number: int = 1,
        page_size: int = 10,
    ) -> dict:
        """查询阿里云安全组基本信息列表

        Args:
            region_id: 安全组所属地域 ID, 示例值: cn-hangzhou.
            page_number: 页码, 起始值为 1, 默认值 1.
            page_size: 每页数量, 取值范围 1~100, 默认值 10.
        """
        return client.describe_security_groups(
            region_id=region_id,
            page_number=page_number,
            page_size=page_size,
        )
