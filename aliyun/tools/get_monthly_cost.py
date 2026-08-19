from aliyun.client import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_monthly_cost")
    def get_monthly_cost(month: str) -> dict:
        """获取阿里云某月花费的金额
        
        Args:
            month: 账期，格式为 YYYY-MM
        """
        return client.get_monthly_cost(month=month)
