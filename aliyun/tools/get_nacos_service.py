from aliyun.client.get_nacos_service import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_nacos_service")
    def get_nacos_service(
        region_id: str,
        instance_id: str,
        service_name: str,
        page_num: int = 1,
        page_size: int = 10,
        group_name: str = None,
        namespace_id: str = None,
        cluster_name: str = None,
    ) -> dict:
        """查询阿里云 MSE Nacos 服务详情(含实例列表)

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            instance_id: MSE Nacos 实例 ID, 示例值: mse-cn-st21v5****.
            service_name: 服务名称, 示例值: providers:com.example.DemoService.
            page_num: 页码, 起始值为 1, 默认值 1.
            page_size: 每页数量, 默认值 10.
            group_name: 服务分组名称, 可选, 默认 DEFAULT_GROUP.
            namespace_id: 命名空间 ID, 可选.
            cluster_name: 集群名称, 可选, 默认 DEFAULT.
        """
        return client.get_nacos_service(
            region_id=region_id,
            instance_id=instance_id,
            service_name=service_name,
            page_num=page_num,
            page_size=page_size,
            group_name=group_name,
            namespace_id=namespace_id,
            cluster_name=cluster_name,
        )
