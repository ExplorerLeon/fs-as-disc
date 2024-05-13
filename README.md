# Big Query

Before you start:
https://cloud.google.com/bigquery/docs/cloud-storage-transfer#:~:text=Storage%20to%20BigQuery.-,Before%20you%20begin,BigQuery%20Data%20Transfer%20Service%2C%20see%20Specify%20encryption%20key%20with%20transfers.,-Limitations

```
bq --location=europe-west2 mk \
--dataset \
--description="test dataset with all datatypes ingest with data transfer from gcs" \
--label=datatype:sample_test \
assetinsure-surety-data-models:asset_secure_test_dataset
```




gs://fs-assetsecure-testing/test_bg_df_sample_data.parquet
