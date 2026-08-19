from datetime import datetime
from zoneinfo import ZoneInfo


def register(mcp):
    @mcp.tool("get_today")
    def get_today() -> dict:
        """获取今天的日期（中国时区）

        Returns:
            date: 今天日期，格式为 YYYY-MM-DD
            month: 当月账期，格式为 YYYY-MM
        """
        today = datetime.now(ZoneInfo("Asia/Shanghai")).date()
        return {
            "date": today.isoformat(),
            "month": today.strftime("%Y-%m"),
        }
