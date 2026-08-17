from mcp.server.fastmcp import FastMCP
from aliyun.tools.get_account_balance import register as aliyun_tools


mcp = FastMCP("cloud-mcp-server", host="0.0.0.0", port=10000)

aliyun_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse")
