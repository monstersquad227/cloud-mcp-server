from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def list_services(self, namespace: str):
        services = self.core_v1.list_namespaced_service(namespace=namespace)
        return {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "count": len(services.items),
            "services": [
                {
                    "name": svc.metadata.name,
                    "type": svc.spec.type if svc.spec else None,
                    "cluster_ip": svc.spec.cluster_ip if svc.spec else None,
                    "external_ips": list(svc.spec.external_i_ps or []) if svc.spec else [],
                    "ports": [
                        {
                            "name": p.name,
                            "protocol": p.protocol,
                            "port": p.port,
                            "target_port": str(p.target_port) if p.target_port is not None else None,
                            "node_port": p.node_port,
                        }
                        for p in (svc.spec.ports or [])
                    ]
                    if svc.spec
                    else [],
                    "selector": dict(svc.spec.selector or {}) if svc.spec else {},
                    "creation_timestamp": (
                        svc.metadata.creation_timestamp.isoformat()
                        if svc.metadata.creation_timestamp
                        else None
                    ),
                }
                for svc in services.items
            ],
        }
