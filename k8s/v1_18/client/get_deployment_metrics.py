from kubernetes.client.rest import ApiException

from .client import KubernetesBaseClient


def _parse_cpu(value: str | None) -> float | None:
    """将 CPU 量转成核数（float）。"""
    if value is None or value == "":
        return None
    value = str(value)
    if value.endswith("n"):
        return int(value[:-1]) / 1_000_000_000
    if value.endswith("u"):
        return int(value[:-1]) / 1_000_000
    if value.endswith("m"):
        return int(value[:-1]) / 1000
    return float(value)


def _parse_memory_bytes(value: str | None) -> int | None:
    """将内存量转成字节。"""
    if value is None or value == "":
        return None
    value = str(value)
    units = {
        "Ki": 1024,
        "Mi": 1024**2,
        "Gi": 1024**3,
        "Ti": 1024**4,
        "K": 1000,
        "M": 1000**2,
        "G": 1000**3,
        "T": 1000**4,
    }
    for suffix, factor in units.items():
        if value.endswith(suffix):
            return int(float(value[: -len(suffix)]) * factor)
    return int(value)


def _format_cpu(cores: float | None) -> str | None:
    if cores is None:
        return None
    millicores = cores * 1000
    if millicores < 1:
        return f"{cores * 1_000_000:.0f}u"
    if millicores < 1000:
        return f"{millicores:.0f}m"
    return f"{cores:.3f}"


def _format_memory(nbytes: int | None) -> str | None:
    if nbytes is None:
        return None
    if nbytes < 1024:
        return f"{nbytes}B"
    if nbytes < 1024**2:
        return f"{nbytes / 1024:.1f}Ki"
    if nbytes < 1024**3:
        return f"{nbytes / 1024**2:.1f}Mi"
    return f"{nbytes / 1024**3:.2f}Gi"


def _resource_dict(resources) -> dict:
    if not resources:
        return {"cpu": None, "memory": None, "cpu_cores": None, "memory_bytes": None}
    cpu = None
    memory = None
    if hasattr(resources, "get"):
        cpu = resources.get("cpu")
        memory = resources.get("memory")
    else:
        cpu = getattr(resources, "cpu", None)
        memory = getattr(resources, "memory", None)
    cpu_cores = _parse_cpu(cpu)
    memory_bytes = _parse_memory_bytes(memory)
    return {
        "cpu": _format_cpu(cpu_cores) if cpu_cores is not None else cpu,
        "memory": _format_memory(memory_bytes) if memory_bytes is not None else memory,
        "cpu_cores": cpu_cores,
        "memory_bytes": memory_bytes,
    }


class KubernetesClient(KubernetesBaseClient):
    def get_deployment_metrics(self, namespace: str, name: str):
        deployment = self.apps_v1.read_namespaced_deployment(name=name, namespace=namespace)
        selector = deployment.spec.selector.match_labels or {}
        label_selector = ",".join(f"{k}={v}" for k, v in selector.items())

        containers_spec = []
        for container in deployment.spec.template.spec.containers or []:
            resources = container.resources
            containers_spec.append(
                {
                    "name": container.name,
                    "requests": _resource_dict(
                        resources.requests if resources else None
                    ),
                    "limits": _resource_dict(resources.limits if resources else None),
                }
            )

        pods = self.core_v1.list_namespaced_pod(
            namespace=namespace,
            label_selector=label_selector,
        )

        metrics_by_pod: dict[str, dict] = {}
        metrics_error = None
        try:
            metrics_list = self.custom_objects.list_namespaced_custom_object(
                group="metrics.k8s.io",
                version="v1beta1",
                namespace=namespace,
                plural="pods",
                label_selector=label_selector,
            )
            for item in metrics_list.get("items", []):
                pod_name = item.get("metadata", {}).get("name")
                containers = []
                total_cpu = 0.0
                total_memory = 0
                for c in item.get("containers", []):
                    usage = c.get("usage", {})
                    cpu_cores = _parse_cpu(usage.get("cpu")) or 0.0
                    memory_bytes = _parse_memory_bytes(usage.get("memory")) or 0
                    total_cpu += cpu_cores
                    total_memory += memory_bytes
                    containers.append(
                        {
                            "name": c.get("name"),
                            "cpu": _format_cpu(cpu_cores),
                            "memory": _format_memory(memory_bytes),
                            "cpu_cores": cpu_cores,
                            "memory_bytes": memory_bytes,
                        }
                    )
                metrics_by_pod[pod_name] = {
                    "timestamp": item.get("timestamp"),
                    "window": item.get("window"),
                    "cpu": _format_cpu(total_cpu),
                    "memory": _format_memory(total_memory),
                    "cpu_cores": total_cpu,
                    "memory_bytes": total_memory,
                    "containers": containers,
                }
        except ApiException as exc:
            metrics_error = f"metrics.k8s.io 不可用: {exc.reason}"

        pod_metrics = []
        sum_cpu = 0.0
        sum_memory = 0
        for pod in pods.items:
            pod_name = pod.metadata.name
            usage = metrics_by_pod.get(pod_name)
            if usage:
                sum_cpu += usage["cpu_cores"] or 0
                sum_memory += usage["memory_bytes"] or 0
            pod_metrics.append(
                {
                    "name": pod_name,
                    "phase": pod.status.phase if pod.status else None,
                    "node": pod.spec.node_name if pod.spec else None,
                    "usage": usage,
                }
            )

        result = {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "deployment": name,
            "replicas": deployment.spec.replicas if deployment.spec else None,
            "containers": containers_spec,
            "pods": pod_metrics,
            "total_usage": {
                "cpu": _format_cpu(sum_cpu),
                "memory": _format_memory(sum_memory),
                "cpu_cores": sum_cpu,
                "memory_bytes": sum_memory,
            },
        }
        if metrics_error:
            result["metrics_error"] = metrics_error
        return result
