from .client import KubernetesBaseClient


class KubernetesClient(KubernetesBaseClient):
    def list_ingresses(self, namespace: str):
        ingresses = self.networking_v1beta1.list_namespaced_ingress(
            namespace=namespace,
        )
        return {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "count": len(ingresses.items),
            "ingresses": [
                {
                    "name": ing.metadata.name,
                    "ingress_class": (
                        ing.metadata.annotations.get("kubernetes.io/ingress.class")
                        if ing.metadata.annotations
                        else None
                    ),
                    "hosts": [
                        rule.host for rule in (ing.spec.rules or []) if rule.host
                    ],
                    "tls": [
                        {
                            "hosts": list(tls.hosts or []),
                            "secret_name": tls.secret_name,
                        }
                        for tls in (ing.spec.tls or [])
                    ],
                    "rules": [
                        {
                            "host": rule.host,
                            "paths": [
                                {
                                    "path": path.path,
                                    "backend": {
                                        "service_name": path.backend.service_name,
                                        "service_port": path.backend.service_port,
                                    },
                                }
                                for path in (rule.http.paths or [])
                            ]
                            if rule.http
                            else [],
                        }
                        for rule in (ing.spec.rules or [])
                    ],
                    "load_balancer": [
                        {
                            "ip": lb.ip,
                            "hostname": lb.hostname,
                        }
                        for lb in (
                            ing.status.load_balancer.ingress
                            if ing.status and ing.status.load_balancer
                            else []
                        )
                    ],
                    "creation_timestamp": (
                        ing.metadata.creation_timestamp.isoformat()
                        if ing.metadata.creation_timestamp
                        else None
                    ),
                }
                for ing in ingresses.items
            ],
        }
