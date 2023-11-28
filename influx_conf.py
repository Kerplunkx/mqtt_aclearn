import influxdb_client

bucket = 'BUCKET'
org = "ORG"
token = "TOKEN"
url = "URL"

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
    return results[-1][1]
