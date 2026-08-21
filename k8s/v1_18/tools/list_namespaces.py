from k8s.v1_18.client.list_namespaces import KubernetesClient


def register(mcp):
    @mcp.tool("list_kubernetes_namespaces")
    def list_namespaces(
        cluster: str | None = None,
        context: str | None = None,
    ) -> dict:
        """列出 Kubernetes 集群中的命名空间

        Args:
            cluster: 环境名。fat -> fatkubeconfig，prod -> prodkubeconfig；不传则用 kubeconfig.
            context: kubeconfig 中的 context 名称；不传则用该配置的 current-context.
        """
        client = KubernetesClient(cluster=cluster, context=context)
        return client.list_namespaces()
