from aliyun.client.list_users import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_users")
    def list_users(marker: str = "", max_items: int = 100) -> dict:
        """查询所有阿里云 RAM 用户

        Args:
            marker: 分页标记, 当上次返回 IsTruncated 为 true 时传入返回的 Marker 继续查询, 默认空.
            max_items: 返回条数, 取值范围 1~1000, 默认值 100.
        """
        return client.list_users(
            marker=marker or None,
            max_items=max_items,
        )
