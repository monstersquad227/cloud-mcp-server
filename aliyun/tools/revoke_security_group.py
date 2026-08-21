from aliyun.client.revoke_security_group import AliyunClient


def register(mcp):
    client = AliyunClient()

    @mcp.tool("revoke_aliyun_security_group")
    def revoke_security_group(
        region_id: str,
        security_group_id: str,
        ip_protocol: str = "",
        port_range: str = "",
        source_cidr_ip: str = "",
        source_group_id: str = "",
        policy: str = "",
        priority: str = "",
        nic_type: str = "",
        security_group_rule_id: str = "",
    ) -> dict:
        """删除阿里云安全组入方向规则

        Args:
            region_id: 安全组所属地域 ID, 示例值: cn-hangzhou.
            security_group_id: 安全组 ID.
            ip_protocol: 协议类型, 取值: TCP/UDP/ICMP/GRE/ALL. 与 security_group_rule_id 二选一.
            port_range: 端口范围, TCP/UDP 示例: 22/22 或 1/65535; ICMP/GRE/ALL 为 -1/-1.
            source_cidr_ip: 源 IPv4 CIDR 地址段, 示例值: 0.0.0.0/0. 与 source_group_id 二选一.
            source_group_id: 源安全组 ID. 与 source_cidr_ip 二选一.
            policy: 授权策略, 取值: accept(允许)/drop(拒绝).
            priority: 规则优先级, 取值范围 1~100.
            nic_type: 网卡类型, 经典网络取值 internet/intranet; VPC 安全组无需设置.
            security_group_rule_id: 安全组规则 ID. 与按规则属性删除二选一, 可通过 describe_security_group_attribute 查询.
        """
        return client.revoke_security_group(
            region_id=region_id,
            security_group_id=security_group_id,
            ip_protocol=ip_protocol or None,
            port_range=port_range or None,
            source_cidr_ip=source_cidr_ip or None,
            source_group_id=source_group_id or None,
            policy=policy or None,
            priority=priority or None,
            nic_type=nic_type or None,
            security_group_rule_id=security_group_rule_id or None,
        )
