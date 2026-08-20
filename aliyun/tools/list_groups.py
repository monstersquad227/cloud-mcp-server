from aliyun.client.list_groups import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_groups")
    def list_groups(marker: str = "", max_items: int = 100) -> dict:
        """查询阿里云 RAM 用户组列表

        Args:
            marker: 分页标记, 当上次返回 IsTruncated 为 true 时传入返回的 Marker 继续查询, 默认空.
            max_items: 每页最大条数, 取值范围 1~100, 默认值 100.
        """
        return client.list_groups(
            marker=marker or None,
            max_items=max_items,
        )
