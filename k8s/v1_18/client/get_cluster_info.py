from kubernetes.config import list_kube_config_contexts
from kubernetes.config.config_exception import ConfigException

from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def get_cluster_info(self):
        version = self.version_api.get_code()
        nodes = self.core_v1.list_node()

        context_name = self.context
        cluster_name = None
        try:
            contexts, active_context = list_kube_config_contexts(
                config_file=self._kubeconfig,
            )
            if self.context:
                matched = next(
                    (c for c in contexts if c.get("name") == self.context),
                    None,
                )
                if matched:
                    context_name = matched.get("name")
                    cluster_name = matched.get("context", {}).get("cluster")
            elif active_context:
                context_name = active_context.get("name")
                cluster_name = active_context.get("context", {}).get("cluster")
        except ConfigException:
            pass

        return {
            "alias": self.cluster_alias,
            "context": context_name,
            "cluster": cluster_name,
            "version": {
                "major": version.major,
                "minor": version.minor,
                "git_version": version.git_version,
                "platform": version.platform,
                "go_version": version.go_version,
            },
            "node_count": len(nodes.items),
            "nodes": [
                {
                    "name": node.metadata.name,
                    "status": next(
                        (
                            condition.type
                            for condition in (node.status.conditions or [])
                            if condition.status == "True"
                            and condition.type == "Ready"
                        ),
                        "NotReady",
                    ),
                    "roles": [
                        label.replace("node-role.kubernetes.io/", "")
                        for label in (node.metadata.labels or {})
                        if label.startswith("node-role.kubernetes.io/")
                    ],
                    "kubelet_version": (
                        node.status.node_info.kubelet_version
                        if node.status and node.status.node_info
                        else None
                    ),
                    "os_image": (
                        node.status.node_info.os_image
                        if node.status and node.status.node_info
                        else None
                    ),
                }
                for node in nodes.items
            ],
        }
