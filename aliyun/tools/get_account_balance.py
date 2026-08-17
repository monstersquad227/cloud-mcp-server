from aliyun.client import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool()
    def get_account_balance() -> dict:
        """获取阿里云账户余额"""
        return client.get_account_balance()