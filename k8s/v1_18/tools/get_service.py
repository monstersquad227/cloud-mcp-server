from k8s.v1_18.client.get_service import KubernetesClient


def register(mcp):
    @mcp.tool("get_kubernetes_service")
    def get_service(
        namespace: str,
        name: str,
        cluster: str | None = None,
        context: str | None = None,
    ) -> dict:
        """查看指定 Service 的详细信息（规格、端口、Endpoints、关联 Pod）

        Args:
            namespace: 命名空间名称，示例值: fat.
            name: Service 名称，示例值: authweb.
            cluster: 环境名。fat -> fatkubeconfig，prod -> prodkubeconfig；不传则用 kubeconfig.
            context: kubeconfig 中的 context 名称；不传则用该配置的 current-context.
        """
        client = KubernetesClient(cluster=cluster, context=context)
        return client.get_service(namespace=namespace, name=name)
