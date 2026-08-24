from k8s.v1_18.client.get_deployment_metrics import KubernetesClient


def register(mcp):
    @mcp.tool("get_kubernetes_deployment_metrics")
    def get_deployment_metrics(
        namespace: str,
        name: str,
        cluster: str | None = None,
        context: str | None = None,
    ) -> dict:
        """查看指定 Deployment 的 CPU / 内存指标（requests、limits、实时用量）

        Args:
            namespace: 命名空间名称，示例值: fat.
            name: Deployment 名称，示例值: authweb.
            cluster: 环境名。fat -> fatkubeconfig，prod -> prodkubeconfig；不传则用 kubeconfig.
            context: kubeconfig 中的 context 名称；不传则用该配置的 current-context.
        """
        client = KubernetesClient(cluster=cluster, context=context)
        return client.get_deployment_metrics(namespace=namespace, name=name)
