from k8s.v1_18.client.get_cluster_info import KubernetesClient


def register(mcp):
    @mcp.tool("get_kubernetes_cluster_info")
    def get_cluster_info(
        cluster: str | None = None,
        context: str | None = None,
    ) -> dict:
        """获取 Kubernetes 集群信息，包括版本、当前上下文及节点列表

        Args:
            cluster: 环境名。fat -> fatkubeconfig，prod -> prodkubeconfig；不传则用 kubeconfig.
            context: kubeconfig 中的 context 名称；不传则用该配置的 current-context.
        """
        client = KubernetesClient(cluster=cluster, context=context)
        return client.get_cluster_info()
