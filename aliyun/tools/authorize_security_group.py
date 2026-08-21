from aliyun.client.authorize_security_group import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("authorize_aliyun_security_group")
    def authorize_security_group(
        region_id: str,
        security_group_id: str,
        ip_protocol: str,
        port_range: str,
        source_cidr_ip: str = "",
        source_group_id: str = "",
        policy: str = "accept",
        priority: str = "1",
        description: str = "",
        nic_type: str = "",
    ) -> dict:
        """增加阿里云安全组入方向规则

        Args:
            region_id: 安全组所属地域 ID, 示例值: cn-hangzhou.
            security_group_id: 安全组 ID.
            ip_protocol: 协议类型, 取值: TCP/UDP/ICMP/GRE/ALL.
            port_range: 端口范围, TCP/UDP 示例: 22/22 或 1/65535; ICMP/GRE/ALL 为 -1/-1.
            source_cidr_ip: 源 IPv4 CIDR 地址段, 示例值: 0.0.0.0/0. 与 source_group_id 二选一.
            source_group_id: 源安全组 ID. 与 source_cidr_ip 二选一.
            policy: 授权策略, 取值: accept(允许)/drop(拒绝), 默认值 accept.
            priority: 规则优先级, 取值范围 1~100, 数字越小优先级越高, 默认值 1.
            description: 规则描述, 1~512 个字符.
            nic_type: 网卡类型, 经典网络取值 internet/intranet; VPC 安全组无需设置.
        """
        return client.authorize_security_group(
            region_id=region_id,
            security_group_id=security_group_id,
            ip_protocol=ip_protocol,
            port_range=port_range,
            source_cidr_ip=source_cidr_ip or None,
            source_group_id=source_group_id or None,
            policy=policy,
            priority=priority,
            description=description or None,
            nic_type=nic_type or None,
        )
