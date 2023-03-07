import dask.array as da
from dask_kubernetes import KubeCluster, make_pod_spec
from dask.distributed import Client

pod_spec = make_pod_spec(image="my_docker_image_name",
    memory_limit="1G", memory_request="1G",
    cpu_limit=1, cpu_request=1,
    extra_pod_config={"imagePullSecrets": [{"name": "my_docker_image_pull_secret"}]}
)

cluster = KubeCluster(pod_spec, namespace="my_k8s_namespace")
cluster.scale(5)

client = Client(cluster)
# Create a large array and calculate the mean
array = da.ones((10, 100, 100))
print(array.mean().compute())