from mcp.server.fastmcp import FastMCP
from common.tools.get_today import register as get_today_tools
from aliyun.tools.get_account_balance import register as aliyun_get_account_balance_tools
from aliyun.tools.get_daily_cost import register as aliyun_get_daily_cost_tools
from aliyun.tools.get_monthly_cost import register as aliyun_get_monthly_cost_tools
from aliyun.tools.describe_instance_status import register as aliyun_describe_instance_status_tools
from aliyun.tools.describe_instances import register as aliyun_describe_instances_tools
from aliyun.tools.list_users import register as aliyun_list_users_tools
from aliyun.tools.get_user import register as aliyun_get_user_tools
from aliyun.tools.list_policies_for_user import register as aliyun_list_policies_for_user_tools

mcp = FastMCP("cloud-mcp-server", host="0.0.0.0", port=10000)

get_today_tools(mcp)
aliyun_get_account_balance_tools(mcp)
aliyun_get_daily_cost_tools(mcp)
aliyun_get_monthly_cost_tools(mcp)
aliyun_describe_instance_status_tools(mcp)
aliyun_describe_instances_tools(mcp)
aliyun_list_users_tools(mcp)
aliyun_get_user_tools(mcp)
aliyun_list_policies_for_user_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse")
