import distributed
import dask.array as da
from dask_kubernetes import KubeCluster


cluster = KubeCluster.from_yaml("worker-spec.yaml", deploy_mode="remote")
cluster.scale_up(10)  # specify number of nodes explicitly

client = distributed.Client(cluster)

array = da.ones((1000, 1000, 1000), chunks=5)
print(array.mean().compute()) # Should print 1.0

cluster.close()