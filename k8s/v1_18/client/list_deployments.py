from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def list_deployments(self, namespace: str):
        deployments = self.apps_v1.list_namespaced_deployment(namespace=namespace)
        return {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "count": len(deployments.items),
            "deployments": [
                {
                    "name": dep.metadata.name,
                    "replicas": dep.spec.replicas if dep.spec else None,
                    "ready_replicas": (
                        dep.status.ready_replicas if dep.status else None
                    ),
                    "available_replicas": (
                        dep.status.available_replicas if dep.status else None
                    ),
                    "updated_replicas": (
                        dep.status.updated_replicas if dep.status else None
                    ),
                    "creation_timestamp": (
                        dep.metadata.creation_timestamp.isoformat()
                        if dep.metadata.creation_timestamp
                        else None
                    ),
                }
                for dep in deployments.items
            ],
        }
