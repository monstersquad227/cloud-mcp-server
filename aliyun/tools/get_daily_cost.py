from aliyun.client import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("get_aliyun_daily_cost")
    def get_daily_cost(date: str, page_size: int = 20, page_num: int = 1) -> dict:
        """获取阿里云某天花费的金额
        
        Args:
            date: 账单日期, YYYY-MM-DD, 示例值: 2026-01.
            page_size: 每页数量, 默认值 20, 最大值: 300.
            page_num: 页码, 默认值为 1.
        """
        return client.get_daily_cost(date=date, page_size=page_size, page_num=page_num)