from google.cloud import bigquery
client = bigquery.Client()


query = (
    "SELECT timestamp FROM `bigquery-public-data.crypto_bitcoin.blocks` ORDER BY timestamp ASC LIMIT 10"
)
query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
)  # API request - starts the query

for row in query_job:  # API request - fetches results
    print(row)
