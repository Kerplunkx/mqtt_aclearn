import influxdb_client
from dotenv import load_dotenv
from os import getenv

load_dotenv()

bucket = getenv("INFLUX_BUCKET")
org = getenv("INFLUX_ORG")
token = getenv("INFLUX_TOKEN")
url = getenv("INFLUX_URL")

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)


def count_people():
    query_api = client.query_api()
    query = 'from(bucket:"ocupancia")\
    |> range(start: -10m)'
    result = query_api.query(org=org, query=query)
    results = []
    for table in result:
        for record in table.records:
            results.append((record.get_field(), record.get_value()))
    try:
        return results[-1][1]
    except:
        return 0
