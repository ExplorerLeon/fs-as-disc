# Big Query

Before you start:
https://cloud.google.com/bigquery/docs/cloud-storage-transfer#:~:text=Storage%20to%20BigQuery.-,Before%20you%20begin,BigQuery%20Data%20Transfer%20Service%2C%20see%20Specify%20encryption%20key%20with%20transfers.,-Limitations


## To make Dataset
Command required to create the dataset in big query. Will eventually be added to a bash script or cloud build yaml that will be executed from Cloud Build or bash command. TBD

```
bq --location=europe-west2 mk \
--dataset \
--description="test dataset with all datatypes ingest with data transfer from gcs" \
--label=datatype:sample_test \
assetinsure-surety-data-models:asset_secure_test_dataset
```

## Create Data transfer
Can't specify the schedule - it is standard 24 hours. Edit in console.

```
bq mk --transfer_config --project_id=assetinsure-surety-data-models --data_source=google_cloud_storage --display_name=test_cs_bq_sample_data --target_dataset=asset_secure_test_dataset  --params='{"destination_table_name_template":"test_sample_1", "data_path_template": "gs://fs-assetsecure-testing/test_bg_df_sample_delta_data.parquet", "write_disposition": "APPEND", "file_format": "PARQUET" }'
```

### Cloud Storage Bucket sample data URI
gs://fs-assetsecure-testing/test_bg_df_sample_data.parquet
