from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def list_namespaces(self):
        namespaces = self.core_v1.list_namespace()
        return {
            "alias": self.cluster_alias,
            "count": len(namespaces.items),
            "namespaces": [
                {
                    "name": ns.metadata.name,
                    "status": ns.status.phase if ns.status else None,
                    "creation_timestamp": (
                        ns.metadata.creation_timestamp.isoformat()
                        if ns.metadata.creation_timestamp
                        else None
                    ),
                }
                for ns in namespaces.items
            ],
        }
