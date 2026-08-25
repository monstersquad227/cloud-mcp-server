from aliyun.client.get_nacos_instance import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_nacos_instance")
    def get_nacos_instance(
        region_id: str,
        instance_id: str,
        acl_switch: bool = False,
    ) -> dict:
        """查询阿里云 MSE Nacos 实例详细信息

        Args:
            region_id: 实例所属地域 ID, 示例值: cn-hangzhou.
            instance_id: MSE 实例 ID, 示例值: mse-cn-st21ri2****.
            acl_switch: 是否查询访问控制白名单, 默认值 false.
        """
        return client.get_nacos_instance(
            region_id=region_id,
            instance_id=instance_id,
            acl_switch=acl_switch,
        )
