from aliyun.client.remove_user_from_group import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("remove_aliyun_user_from_group")
    def remove_user_from_group(user_name: str, group_name: str) -> dict:
        """将阿里云 RAM 用户从用户组中移除

        Args:
            user_name: RAM 用户名称, 示例值: alice.
            group_name: 用户组名称, 示例值: Dev-Team.
        """
        return client.remove_user_from_group(user_name=user_name, group_name=group_name)
