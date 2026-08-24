from .client import KubernetesBaseClient


def _container_detail(container) -> dict:
    resources = container.resources
    return {
        "name": container.name,
        "image": container.image,
        "image_pull_policy": container.image_pull_policy,
        "ports": [
            {
                "name": p.name,
                "container_port": p.container_port,
                "protocol": p.protocol,
            }
            for p in (container.ports or [])
        ],
        "env": [
            {
                "name": e.name,
                "value": e.value,
                "value_from": (
                    {
                        "field_ref": (
                            e.value_from.field_ref.field_path
                            if e.value_from.field_ref
                            else None
                        ),
                        "config_map_key_ref": (
                            {
                                "name": e.value_from.config_map_key_ref.name,
                                "key": e.value_from.config_map_key_ref.key,
                            }
                            if e.value_from.config_map_key_ref
                            else None
                        ),
                        "secret_key_ref": (
                            {
                                "name": e.value_from.secret_key_ref.name,
                                "key": e.value_from.secret_key_ref.key,
                            }
                            if e.value_from.secret_key_ref
                            else None
                        ),
                    }
                    if e.value_from
                    else None
                ),
            }
            for e in (container.env or [])
        ],
        "resources": {
            "requests": dict(resources.requests or {}) if resources else {},
            "limits": dict(resources.limits or {}) if resources else {},
        },
        "volume_mounts": [
            {
                "name": vm.name,
                "mount_path": vm.mount_path,
                "read_only": vm.read_only,
                "sub_path": vm.sub_path,
            }
            for vm in (container.volume_mounts or [])
        ],
        "liveness_probe": bool(container.liveness_probe),
        "readiness_probe": bool(container.readiness_probe),
        "startup_probe": bool(getattr(container, "startup_probe", None)),
        "command": container.command,
        "args": container.args,
    }


class KubernetesClient(KubernetesBaseClient):
    def get_deployment(self, namespace: str, name: str):
        deployment = self.apps_v1.read_namespaced_deployment(
            name=name,
            namespace=namespace,
        )
        selector = (
            deployment.spec.selector.match_labels if deployment.spec.selector else {}
        ) or {}
        label_selector = ",".join(f"{k}={v}" for k, v in selector.items())

        pods = self.core_v1.list_namespaced_pod(
            namespace=namespace,
            label_selector=label_selector,
        )

        strategy = deployment.spec.strategy
        conditions = []
        if deployment.status and deployment.status.conditions:
            conditions = [
                {
                    "type": c.type,
                    "status": c.status,
                    "reason": c.reason,
                    "message": c.message,
                    "last_update_time": (
                        c.last_update_time.isoformat() if c.last_update_time else None
                    ),
                }
                for c in deployment.status.conditions
            ]

        return {
            "alias": self.cluster_alias,
            "namespace": namespace,
            "name": name,
            "metadata": {
                "uid": deployment.metadata.uid,
                "labels": deployment.metadata.labels or {},
                "annotations": deployment.metadata.annotations or {},
                "creation_timestamp": (
                    deployment.metadata.creation_timestamp.isoformat()
                    if deployment.metadata.creation_timestamp
                    else None
                ),
                "generation": deployment.metadata.generation,
            },
            "spec": {
                "replicas": deployment.spec.replicas,
                "selector": selector,
                "strategy": {
                    "type": strategy.type if strategy else None,
                    "rolling_update": (
                        {
                            "max_surge": strategy.rolling_update.max_surge,
                            "max_unavailable": strategy.rolling_update.max_unavailable,
                        }
                        if strategy and strategy.rolling_update
                        else None
                    ),
                },
                "revision_history_limit": deployment.spec.revision_history_limit,
                "progress_deadline_seconds": deployment.spec.progress_deadline_seconds,
                "min_ready_seconds": deployment.spec.min_ready_seconds,
                "containers": [
                    _container_detail(c)
                    for c in (deployment.spec.template.spec.containers or [])
                ],
                "init_containers": [
                    _container_detail(c)
                    for c in (deployment.spec.template.spec.init_containers or [])
                ],
                "node_selector": deployment.spec.template.spec.node_selector or {},
                "host_aliases": [
                    {
                        "ip": ha.ip,
                        "hostnames": list(ha.hostnames or []),
                    }
                    for ha in (deployment.spec.template.spec.host_aliases or [])
                ],
                "service_account_name": deployment.spec.template.spec.service_account_name,
                "restart_policy": deployment.spec.template.spec.restart_policy,
                "volumes": [
                    {
                        "name": v.name,
                        "config_map": (
                            v.config_map.name if v.config_map else None
                        ),
                        "secret": v.secret.secret_name if v.secret else None,
                        "empty_dir": bool(v.empty_dir),
                        "persistent_volume_claim": (
                            v.persistent_volume_claim.claim_name
                            if v.persistent_volume_claim
                            else None
                        ),
                        "host_path": (
                            v.host_path.path if v.host_path else None
                        ),
                    }
                    for v in (deployment.spec.template.spec.volumes or [])
                ],
            },
            "status": {
                "replicas": deployment.status.replicas if deployment.status else None,
                "ready_replicas": (
                    deployment.status.ready_replicas if deployment.status else None
                ),
                "available_replicas": (
                    deployment.status.available_replicas if deployment.status else None
                ),
                "unavailable_replicas": (
                    deployment.status.unavailable_replicas if deployment.status else None
                ),
                "updated_replicas": (
                    deployment.status.updated_replicas if deployment.status else None
                ),
                "observed_generation": (
                    deployment.status.observed_generation if deployment.status else None
                ),
                "conditions": conditions,
            },
            "pods": [
                {
                    "name": pod.metadata.name,
                    "phase": pod.status.phase if pod.status else None,
                    "node": pod.spec.node_name if pod.spec else None,
                    "pod_ip": pod.status.pod_ip if pod.status else None,
                    "ready": all(
                        (c.ready for c in (pod.status.container_statuses or []))
                    )
                    if pod.status and pod.status.container_statuses
                    else False,
                    "restarts": sum(
                        (c.restart_count or 0)
                        for c in (pod.status.container_statuses or [])
                    )
                    if pod.status
                    else 0,
                    "start_time": (
                        pod.status.start_time.isoformat()
                        if pod.status and pod.status.start_time
                        else None
                    ),
                }
                for pod in pods.items
            ],
        }
