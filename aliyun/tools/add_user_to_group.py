from aliyun.client.add_user_to_group import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("add_aliyun_user_to_group")
    def add_user_to_group(user_name: str, group_name: str) -> dict:
        """将阿里云 RAM 用户添加到指定的用户组

        Args:
            user_name: RAM 用户名称, 示例值: alice.
            group_name: 用户组名称, 示例值: Dev-Team.
        """
        return client.add_user_to_group(user_name=user_name, group_name=group_name)
