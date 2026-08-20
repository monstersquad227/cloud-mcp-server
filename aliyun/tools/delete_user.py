from aliyun.client.delete_user import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("delete_aliyun_user")
    def delete_user(user_name: str) -> dict:
        """删除一个阿里云 RAM 用户。删除前需保证该用户不拥有任何权限且不属于任何用户组。

        Args:
            user_name: RAM 用户名称, 长度 1~64, 可包含字母、数字、半角句号(.), 短划线(-), 下划线(_), 示例值: alice.
        """
        return client.delete_user(user_name=user_name)
