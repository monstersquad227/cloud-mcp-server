import os
from pathlib import Path

from dotenv import load_dotenv
from kubernetes import client, config
from kubernetes.config.config_exception import ConfigException

load_dotenv()

PROJECT_ROOT = Path(__file__).resolve().parents[3]


def kubeconfig_dir() -> Path:
    raw = os.getenv("KUBECONFIG_DIR", "").strip()
    if raw:
        return Path(raw).expanduser().resolve()
    return PROJECT_ROOT


def kubeconfig_filename(cluster: str | None = None) -> str:
    """fat -> fatkubeconfig；未指定 -> kubeconfig。"""
    alias = (cluster or "").strip()
    if not alias:
        return "kubeconfig"
    return f"{alias}kubeconfig"


def resolve_kubeconfig(cluster: str | None = None) -> tuple[str | None, str]:
    """返回 (cluster_alias, kubeconfig_path)。"""
    alias = (cluster or "").strip() or None
    path = kubeconfig_dir() / kubeconfig_filename(alias)
    if not path.is_file():
        raise FileNotFoundError(
            f"未找到 kubeconfig 文件: {path}（cluster={alias or '默认'}）"
        )
    return alias, str(path)


class KubernetesBaseClient:
    def __init__(self, cluster: str | None = None, context: str | None = None):
        configuration = client.Configuration()
        self.cluster_alias, kubeconfig = resolve_kubeconfig(cluster)
        self.context = context

        try:
            config.load_kube_config(
                config_file=kubeconfig,
                context=context,
                client_configuration=configuration,
            )
        except ConfigException:
            config.load_incluster_config(client_configuration=configuration)

        verify_ssl = os.getenv("KUBERNETES_VERIFY_SSL", "true").lower()
        if self.cluster_alias:
            per_cluster = os.getenv(
                f"KUBERNETES_VERIFY_SSL_{self.cluster_alias}".upper(),
                "",
            ).lower()
            if per_cluster:
                verify_ssl = per_cluster
        if verify_ssl in ("0", "false", "no"):
            configuration.verify_ssl = False

        api_client = client.ApiClient(configuration)
        self.core_v1 = client.CoreV1Api(api_client)
        self.apps_v1 = client.AppsV1Api(api_client)
        self.networking_v1beta1 = client.NetworkingV1beta1Api(api_client)
        self.custom_objects = client.CustomObjectsApi(api_client)
        self.version_api = client.VersionApi(api_client)
        self._kubeconfig = kubeconfig
