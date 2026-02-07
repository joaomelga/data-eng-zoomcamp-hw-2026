Pre-requisites
- Create GCP account
- Create GCP bucket
- Generate `gcs.json` credentials file
- Run `./yellow_taxi_data.py`
- Create external table on BigQuery by tunning:

  ```SQL
  CREATE OR REPLACE EXTERNAL TABLE `nytaxi.tripdata`
  OPTIONS (
    format = 'parquet',
    uris = ['gs://yellow-taxi-data-jm/yellow_tripdata_2024-*.parquet']
  );
  ```

# Question 1

Run:

  ```SQL
  SELECT COUNT(*) AS record_count
  FROM `nytaxi.tripdata`
  ```

Anwser: 20332093
