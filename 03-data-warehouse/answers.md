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
  -- External
  SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations
  FROM `nytaxi.external_tripdata`;

  -- Regular
  SELECT COUNT(DISTINCT PULocationID) AS distinct_pu_locations
  FROM `nytaxi.tripdata`;
  ```

Results: 0 MB for the External Table and 155.12 MB for the Materialized Table

# Question 3

Estimate queries:

  ```SQL
  -- query 1
  SELECT PULocationID
  FROM `nytaxi.tripdata`;

  -- query 2
  SELECT PULocationID, DOLocationID
  FROM `nytaxi.tripdata`;
  ```

Obs: query 2 estimates approximately double the bytes of query 1.

Answer: BigQuery is a columnar database, and it only scans the specific columns requested in the query. Querying two columns (PULocationID, DOLocationID) requires 
reading more data than querying one column (PULocationID), leading to a higher estimated number of bytes processed.

# Question 4

Run:

  ```SQL
  SELECT COUNT(*) AS zero_fare_count
  FROM `nytaxi.tripdata`
  WHERE fare_amount = 0;
  ```

Answer: 8333
