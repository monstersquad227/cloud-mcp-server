from aliyun.client.get_account_balance import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_account_balance")
    def get_account_balance() -> dict:
        """获取阿里云账户余额"""
        return client.get_account_balance()
