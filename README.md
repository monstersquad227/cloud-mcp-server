# CLOUD-MCP-SERVER

## Tools

### get_account_balance
获取阿里云账户余额

### get_daily_cost
获取阿里云某天花费的金额

### get_monthly_cost
获取阿里云某月花费的金额

### describe_instance_status
查询阿里云 ECS 实例的状态信息列表（通过 RegionId）

### describe_instances
查询阿里云 ECS 实例的详细信息列表（通过 RegionId）

### describe_security_groups
查询阿里云安全组基本信息列表（通过 RegionId）

### describe_security_group_attribute
查询阿里云安全组和组内规则信息（通过 RegionId 与 SecurityGroupId）

### authorize_security_group
增加阿里云安全组入方向规则

### revoke_security_group
删除阿里云安全组入方向规则

### list_users
查询所有阿里云 RAM 用户

### get_user
查询阿里云 RAM 用户的详细信息

### list_policies_for_user
查询阿里云 RAM 用户的授权列表

### delete_user
删除一个阿里云 RAM 用户

### create_user
创建阿里云 RAM 用户

### add_user_to_group
将阿里云 RAM 用户添加到指定的用户组

### list_groups
查询阿里云 RAM 用户组列表

### remove_user_from_group
将阿里云 RAM 用户从用户组中移除

### get_kubernetes_cluster_info
获取 Kubernetes 集群信息。`cluster` 按约定选配置文件：不传 -> `kubeconfig`，`fat` -> `fatkubeconfig`，`prod` -> `prodkubeconfig`。

### list_kubernetes_namespaces
列出 Kubernetes 集群中的命名空间

### list_kubernetes_deployments
列出指定命名空间中的 Deployment

## Start

### virtual environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### install

```bash
pip3 install -r requirements.txt
```

### run

```bash
python3 server.py
```

### development

```bash
mcp dev server.py
```
