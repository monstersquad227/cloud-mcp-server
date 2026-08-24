from kubernetes.client.rest import ApiException

from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def get_service(self, namespace: str, name: str):
        service = self.core_v1.read_namespaced_service(
            name=name,
            namespace=namespace,
        )
        spec = service.spec
        selector = dict(spec.selector or {}) if spec else {}
        label_selector = ",".join(f"{k}={v}" for k, v in selector.items())

        pods = []
        if label_selector:
            pod_list = self.core_v1.list_namespaced_pod(
                namespace=namespace,
                label_selector=label_selector,
            )
            pods = [
                {
                    "name": pod.metadata.name,
                    "phase": pod.status.phase if pod.status else None,
                    "node": pod.spec.node_name if pod.spec else None,
                    "pod_ip": pod.status.pod_ip if pod.status else None,
                    "ready": all(
                        c.ready for c in (pod.status.container_statuses or [])
                    )
                    if pod.status and pod.status.container_statuses
                    else False,
                }
                for pod in pod_list.items
            ]

        endpoints = None
        try:
            eps = self.core_v1.read_namespaced_endpoints(
                name=name,
                namespace=namespace,
            )
            endpoints = [
                {
                    "addresses": [
                        {
                            "ip": addr.ip,
                            "target_ref": (
                                {
                                    "kind": addr.target_ref.kind,
                                    "name": addr.target_ref.name,
                                }
                                if addr.target_ref
                                else None
                            ),
                        }
                        for addr in (subset.addresses or [])
                    ],
                    "not_ready_addresses": [
                        {
                            "ip": addr.ip,
                            "target_ref": (
                                {
                                    "kind": addr.target_ref.kind,
                                    "name": addr.target_ref.name,
                                }
                                if addr.target_ref
                                else None
                            ),
                        }
                        for addr in (subset.not_ready_addresses or [])
                    ],
                    "ports": [
                        {
                            "name": p.name,
                            "port": p.port,
                            "protocol": p.protocol,
                        }
                        for p in (subset.ports or [])
                    ],
                }
                for subset in (eps.subsets or [])
            ]
        except ApiException:
            endpoints = []

        load_balancer = None
        if service.status and service.status.load_balancer:
            load_balancer = [
                {
                    "ip": item.ip,
                    "hostname": item.hostname,
                }
                for item in (service.status.load_balancer.ingress or [])
            ]

        return {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "name": name,
            "metadata": {
                "uid": service.metadata.uid,
                "labels": service.metadata.labels or {},
                "annotations": service.metadata.annotations or {},
                "creation_timestamp": (
                    service.metadata.creation_timestamp.isoformat()
                    if service.metadata.creation_timestamp
                    else None
                ),
            },
            "spec": {
                "type": spec.type if spec else None,
                "cluster_ip": spec.cluster_ip if spec else None,
                "external_ips": list(spec.external_i_ps or []) if spec else [],
                "external_name": spec.external_name if spec else None,
                "load_balancer_ip": spec.load_balancer_ip if spec else None,
                "external_traffic_policy": spec.external_traffic_policy if spec else None,
                "session_affinity": spec.session_affinity if spec else None,
                "selector": selector,
                "ports": [
                    {
                        "name": p.name,
                        "protocol": p.protocol,
                        "port": p.port,
                        "target_port": str(p.target_port)
                        if p.target_port is not None
                        else None,
                        "node_port": p.node_port,
                    }
                    for p in (spec.ports or [])
                ]
                if spec
                else [],
            },
            "status": {
                "load_balancer": load_balancer,
            },
            "endpoints": endpoints,
            "pods": pods,
        }
