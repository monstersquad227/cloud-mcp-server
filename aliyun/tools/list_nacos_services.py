from aliyun.client.list_nacos_services import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_nacos_services")
    def list_nacos_services(
        region_id: str,
        instance_id: str,
        page_num: int = 1,
        page_size: int = 10,
        service_name: str = None,
        group_name: str = None,
        namespace_id: str = None,
        has_ip_count: str = None,
    ) -> dict:
        """查询阿里云 MSE Nacos 实例下的服务列表

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            instance_id: MSE Nacos 实例 ID, 示例值: mse-cn-st21v5****.
            page_num: 页码, 起始值为 1, 默认值 1.
            page_size: 每页数量, 默认值 10.
            service_name: 服务名称, 可选.
            group_name: 服务分组名称, 可选.
            namespace_id: 命名空间 ID, 可选.
            has_ip_count: 是否查询服务实例数量, 可选.
        """
        return client.list_nacos_services(
            region_id=region_id,
            instance_id=instance_id,
            page_num=page_num,
            page_size=page_size,
            service_name=service_name,
            group_name=group_name,
            namespace_id=namespace_id,
            has_ip_count=has_ip_count,
        )
