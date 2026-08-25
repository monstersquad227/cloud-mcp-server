from aliyun.client.get_nacos_config import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_nacos_config")
    def get_nacos_config(
        region_id: str,
        instance_id: str,
        data_id: str,
        group: str,
        namespace_id: str = None,
        beta: bool = False,
    ) -> dict:
        """查询阿里云 MSE Nacos 配置详情

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            instance_id: MSE Nacos 实例 ID, 示例值: mse-cn-i7m2h0****.
            data_id: 配置 Data ID, 示例值: log.yaml.
            group: 配置分组 Group, 示例值: DEFAULT_GROUP.
            namespace_id: 命名空间 ID, 默认 public, 可选.
            beta: 是否获取 Beta 发布配置, 默认值 false.
        """
        return client.get_nacos_config(
            region_id=region_id,
            instance_id=instance_id,
            data_id=data_id,
            group=group,
            namespace_id=namespace_id,
            beta=beta,
        )
