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

### Cloud Storage Bucket sample data URI
gs://fs-assetsecure-testing/test_bg_df_sample_data.parquet
