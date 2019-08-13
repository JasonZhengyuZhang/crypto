from google.cloud import bigquery
client = bigquery.Client()


query = (
    "SELECT timestamp FROM `bigquery-public-data.crypto_bitcoin.blocks` ORDER BY timestamp ASC LIMIT 10"
)
query_job = client.query(
    query,
    # Location must match that of the dataset(s) referenced in the query.
    location="US",
)  

# SELECT
#   `hash`,
#   input_count,
#   output_count,
#   input_value,
#   output_value,
#   fee,
#   i.addresses as ia,
#   o.addresses as oa,
#   i.value as iv,
#   o.value as ov
# FROM
#   `bigquery-public-data.crypto_bitcoin.transactions`, UNNEST(inputs) as i, UNNEST(outputs) as o
# WHERE
#   block_hash = '000000000000000000d6cdda66edb65e8969566ca65fe3c2a7470e553439c0b0'
# ORDER BY `hash` ASC



for row in query_job: 
    print(row)
