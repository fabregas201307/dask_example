import pandas as pd
from dask import delayed
from sklearn.linear_model import LinearRegression
from dask_kubernetes import KubeCluster, make_pod_spec
from dask.distributed import Client

def model_one_run(insample_data, outsample_data, features, insample_end_date):
    xx_train, yy_train = insample_data[features], insample_data[["target"]]
    xx_test, yy_test = outsample_data[features], outsample_data[["target"]]
    xx_test = xx_test.head(2)

    model_obj = LinearRegression()
    model_obj.fit(xx_train, yy_train)
    yy_test_predicted = model_obj.predict(xx_test)
    return yy_test_compare_piece

def rolling_compare(y, all_data_dates):
    r = pd.concat(y)
    return r

def run_rolling_model(all_data):
    count = 0
    while True:
        print(count)
        if count > 20:
            break
        count += 1

    total = delayed(rolling_compare)([1, 2, 3], [2, 5, 6])
    r = total.compute()
    return r

def main():
    all_data = pd.read_csv("data.csv", index_col=0)
    pod_spec = make_pod_spec(image="my_docker_image_name",
        memory_limit="1G", memory_request="1G",
        cpu_limit=1, cpu_request=1,
        extra_pod_config={"imagePullSecrets": [{"name": "my_docker_image_pull_secret"}]}
    )
    cluster = KubeCluster(pod_spec, namespace="my_k8s_namespace")
    cluster.scale(5)
    # client = Client(cluster)
    test = run_rolling_model(all_data)
    print(test.shape)

if __name__ == "__main__":
    main()
