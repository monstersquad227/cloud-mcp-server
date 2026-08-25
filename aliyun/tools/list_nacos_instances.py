from aliyun.client.list_nacos_instances import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_nacos_instances")
    def list_nacos_instances(
        region_id: str,
        page_num: int = 1,
        page_size: int = 10,
        cluster_alias_name: str = None,
    ) -> dict:
        """查询阿里云 MSE Nacos 实例列表

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            page_num: 页码, 起始值为 1, 默认值 1.
            page_size: 每页数量, 默认值 10.
            cluster_alias_name: 集群别名, 支持模糊匹配, 可选.
        """
        return client.list_nacos_instances(
            region_id=region_id,
            page_num=page_num,
            page_size=page_size,
            cluster_alias_name=cluster_alias_name,
        )
