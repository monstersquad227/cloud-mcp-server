from aliyun.client import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_daily_cost")
    def get_daily_cost(date: str) -> dict:
        """获取阿里云某天花费的金额
        
        Args:
            date: 日期，格式为 YYYY-MM-DD
        """
        return client.get_daily_cost(date=date)