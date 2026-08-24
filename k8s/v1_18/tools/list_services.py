from k8s.v1_18.client.list_services import KubernetesClient


def register(mcp):
    @mcp.tool("list_kubernetes_services")
    def list_services(
        namespace: str,
        cluster: str | None = None,
        context: str | None = None,
    ) -> dict:
        """列出指定命名空间中的 Service

        Args:
            namespace: 命名空间名称，示例值: fat.
            cluster: 环境名。fat -> fatkubeconfig，prod -> prodkubeconfig；不传则用 kubeconfig.
            context: kubeconfig 中的 context 名称；不传则用该配置的 current-context.
        """
        client = KubernetesClient(cluster=cluster, context=context)
        return client.list_services(namespace=namespace)
