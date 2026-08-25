from aliyun.client.list_nacos_configs import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_nacos_configs")
    def list_nacos_configs(
        region_id: str,
        instance_id: str,
        page_num: int = 1,
        page_size: int = 10,
        data_id: str = None,
        group: str = None,
        app_name: str = None,
        namespace_id: str = None,
        tags: str = None,
    ) -> dict:
        """查询阿里云 MSE Nacos 实例下的配置列表

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            instance_id: MSE Nacos 实例 ID, 示例值: mse-cn-7mz2fj****.
            page_num: 页码, 起始值为 1, 默认值 1.
            page_size: 每页数量, 默认值 10.
            data_id: 配置 Data ID, 支持模糊匹配, 可选.
            group: 配置分组 Group, 可选.
            app_name: 应用名, 可选.
            namespace_id: 命名空间 ID, 可选.
            tags: 配置标签, 可选.
        """
        return client.list_nacos_configs(
            region_id=region_id,
            instance_id=instance_id,
            page_num=page_num,
            page_size=page_size,
            data_id=data_id,
            group=group,
            app_name=app_name,
            namespace_id=namespace_id,
            tags=tags,
        )
