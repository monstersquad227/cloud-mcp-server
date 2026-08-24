from mcp.server.fastmcp import FastMCP
from common.tools.get_today import register as get_today_tools
from aliyun.tools.get_account_balance import register as aliyun_get_account_balance_tools
from aliyun.tools.get_daily_cost import register as aliyun_get_daily_cost_tools
from aliyun.tools.get_monthly_cost import register as aliyun_get_monthly_cost_tools
from aliyun.tools.describe_instance_status import register as aliyun_describe_instance_status_tools
from aliyun.tools.describe_instances import register as aliyun_describe_instances_tools
from aliyun.tools.describe_security_groups import register as aliyun_describe_security_groups_tools
from aliyun.tools.describe_security_group_attribute import register as aliyun_describe_security_group_attribute_tools
from aliyun.tools.authorize_security_group import register as aliyun_authorize_security_group_tools
from aliyun.tools.revoke_security_group import register as aliyun_revoke_security_group_tools
from aliyun.tools.list_users import register as aliyun_list_users_tools
from aliyun.tools.get_user import register as aliyun_get_user_tools
from aliyun.tools.list_policies_for_user import register as aliyun_list_policies_for_user_tools
from aliyun.tools.delete_user import register as aliyun_delete_user_tools
from aliyun.tools.create_user import register as aliyun_create_user_tools
from aliyun.tools.add_user_to_group import register as aliyun_add_user_to_group_tools
from aliyun.tools.list_groups import register as aliyun_list_groups_tools
from aliyun.tools.remove_user_from_group import register as aliyun_remove_user_from_group_tools
from k8s.v1_18.tools.get_cluster_info import register as kubernetes_get_cluster_info_tools
from k8s.v1_18.tools.list_namespaces import register as kubernetes_list_namespaces_tools
from k8s.v1_18.tools.list_deployments import register as kubernetes_list_deployments_tools
from k8s.v1_18.tools.list_services import register as kubernetes_list_services_tools
from k8s.v1_18.tools.get_deployment_metrics import register as kubernetes_get_deployment_metrics_tools
from k8s.v1_18.tools.get_deployment import register as kubernetes_get_deployment_tools

mcp = FastMCP("cloud-mcp-server", host="0.0.0.0", port=10000)

get_today_tools(mcp)
aliyun_get_account_balance_tools(mcp)
aliyun_get_daily_cost_tools(mcp)
aliyun_get_monthly_cost_tools(mcp)
aliyun_describe_instance_status_tools(mcp)
aliyun_describe_instances_tools(mcp)
aliyun_describe_security_groups_tools(mcp)
aliyun_describe_security_group_attribute_tools(mcp)
aliyun_authorize_security_group_tools(mcp)
aliyun_revoke_security_group_tools(mcp)
aliyun_list_users_tools(mcp)
aliyun_get_user_tools(mcp)
aliyun_list_policies_for_user_tools(mcp)
aliyun_delete_user_tools(mcp)
aliyun_create_user_tools(mcp)
aliyun_add_user_to_group_tools(mcp)
aliyun_list_groups_tools(mcp)
aliyun_remove_user_from_group_tools(mcp)
kubernetes_get_cluster_info_tools(mcp)
kubernetes_list_namespaces_tools(mcp)
kubernetes_list_deployments_tools(mcp)
kubernetes_list_services_tools(mcp)
kubernetes_get_deployment_tools(mcp)
kubernetes_get_deployment_metrics_tools(mcp)

if __name__ == "__main__":
    mcp.run(transport="sse")
