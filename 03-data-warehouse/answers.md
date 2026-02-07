Pre-requisites
- Create GCP account
- Create GCP bucket
- Generate `gcs.json` credentials file
- Run `./yellow_taxi_data.py`
- Create external and regular tables by running:

  ```SQL
  CREATE OR REPLACE EXTERNAL TABLE `nytaxi.external_tripdata`
  OPTIONS (
    format = 'PARQUET',
    uris = ['gs://yellow-taxi-data-jm/yellow_tripdata_2024-*.parquet']
  );

  CREATE OR REPLACE TABLE `nytaxi.tripdata`
  AS
  SELECT * FROM `nytaxi.external_tripdata`;
  ```

# Question 1

Run:

  ```SQL
  SELECT COUNT(*) AS record_count
  FROM `nytaxi.tripdata`
  ```

Anwser: 20332093

# Question 2

Paste the queries separatelly:

  ```SQL
  SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations
  FROM `nytaxi.external_tripdata`;

  SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations
  FROM `nytaxi.tripdata`;
  ```

Results: 0 MB for the External Table and 155.12 MB for the Materialized Table
