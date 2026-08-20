from aliyun.client.list_policies_for_user import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("list_aliyun_policies_for_user")
    def list_policies_for_user(user_name: str) -> dict:
        """查询阿里云 RAM 用户的授权列表（云账号范围，不含资源组授权）

        Args:
            user_name: RAM 用户名称, 示例值: alice.
        """
        return client.list_policies_for_user(user_name=user_name)
