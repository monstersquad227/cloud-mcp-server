from aliyun.client.get_user import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_user")
    def get_user(user_name: str) -> dict:
        """查询阿里云 RAM 用户的详细信息

        Args:
            user_name: RAM 用户名称, 长度 1~64, 可包含字母、数字、半角句号(.), 短划线(-), 下划线(_), 示例值: alice.
        """
        return client.get_user(user_name=user_name)
