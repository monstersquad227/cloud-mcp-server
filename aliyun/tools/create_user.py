from aliyun.client.create_user import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("create_aliyun_user")
    def create_user(
        user_name: str,
        display_name: str = "",
        mobile_phone: str = "",
        email: str = "",
        comments: str = "",
    ) -> dict:
        """创建阿里云 RAM 用户

        Args:
            user_name: RAM 用户名称, 长度 1~64, 可包含字母、数字、半角句号(.), 短划线(-), 下划线(_), 示例值: alice.
            display_name: 显示名称, 长度 1~128, 默认空.
            mobile_phone: 手机号码, 格式: 国际区号-号码, 示例值: 86-18688888888, 默认空.
            email: 电子邮箱, 示例值: alice@example.com, 默认空.
            comments: 备注, 长度 1~128, 默认空.
        """
        return client.create_user(
            user_name=user_name,
            display_name=display_name or None,
            mobile_phone=mobile_phone or None,
            email=email or None,
            comments=comments or None,
        )
