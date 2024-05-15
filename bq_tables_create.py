import sys

from google.cloud import bigquery

def create_parquet_table(table_name, cloud_storage_file_uri, ):
    """
    Main Load function from parquet Google Cloud Storage file to
    Big Query dataset with no tables initially.
    """

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Set table_id to the ID of the table to create.
    table_id = f"assetinsure-surety-data-models.asset_secure_test_dataset.{table_name}"

    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.PARQUET,
    )

    load_job = client.load_table_from_uri(
        cloud_storage_file_uri, table_id, job_config=job_config
    )  # Make an API request.

    load_job.result()  # Waits for the job to complete.

    destination_table = client.get_table(table_id)
    print("Loaded {} rows.".format(destination_table.num_rows))


def get_table_metadata(table_name):

    # Construct a BigQuery client object.
    client = bigquery.Client()

    # Set table_id to the ID of the model to fetch.
    table_id = f"assetinsure-surety-data-models.asset_secure_test_dataset.{table_name}"
    table = client.get_table(table_id)  # Make an API request.

    # View table properties
    print(
    "Got table '{}.{}.{}'.".format(table.project, table.dataset_id, table.table_id)
    )
    print("Table schema: {}".format(table.schema))
    print("Table description: {}".format(table.description))
    print("Table has {} rows".format(table.num_rows))

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python bq_tables_create.py <table_name> <cloud_storage_file_uri>")
        sys.exit(1)

    table_name = sys.argv[1]
    cloud_storage_file_uri = sys.argv[2]

    create_parquet_table(table_name, cloud_storage_file_uri)

    get_table_metadata(table_name)
