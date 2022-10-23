from databricks import sql
import os

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi

api_client = ApiClient(
    host=os.getenv("DATABRICKS_PROJECT_3_HOST"),
    token=os.getenv("DATABRICKS_PROJECT_3_TOKEN"),
)

clusters_api = ClusterApi(api_client)
clusters_list = clusters_api.list_clusters()
print(clusters_api)
print(clusters_list)

print("Cluster name, cluster ID")

# for cluster in clusters_list['clusters']:
#   print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")

# with sql.connect(
#     server_hostname=os.getenv("DATABRICKS_SERVER_HOSTNAME"),
#     http_path=os.getenv("DATABRICKS_HTTP_PATH"),
#     access_token=os.getenv("DATABRICKS_TOKEN"),
# ) as connection:

#     with connection.cursor() as cursor:
#         cursor.execute("CREATE TABLE IF NOT EXISTS squares (x int, x_squared int)")

#         squares = [(i, i * i) for i in range(100)]
#         values = ",".join([f"({x}, {y})" for (x, y) in squares])

#         cursor.execute(f"INSERT INTO squares VALUES {values}")

#         cursor.execute("SELECT * FROM squares LIMIT 10")

#         result = cursor.fetchall()

#         for row in result:
#             print(row)
