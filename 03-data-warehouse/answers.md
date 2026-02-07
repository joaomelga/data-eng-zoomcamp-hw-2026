# Pre-requisites

- Create GCP account
- Create GCP bucket named `yellow-taxi-data-jm`
- Generate `gcs.json` credentials file
- Run `./yellow_taxi_data.py`
- Create external and regular tables by running:

  ```SQL
  -- Create external table
  CREATE OR REPLACE EXTERNAL TABLE `nytaxi.external_tripdata`
  OPTIONS (
    format = 'PARQUET',
    uris = ['gs://yellow-taxi-data-jm/yellow_tripdata_2024-*.parquet']
  );

  -- Create regular table
  CREATE OR REPLACE TABLE `nytaxi.tripdata`
  AS
  SELECT * FROM `nytaxi.external_tripdata`;
  ```

# Question 1

Run query:

  ```SQL
  SELECT COUNT(*) AS record_count
  FROM `nytaxi.tripdata`
  ```

Anwser: 20332093

# Question 2

Estimate the queries separatelly:

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

Run query:

  ```SQL
  SELECT COUNT(*) AS zero_fare_count
  FROM `nytaxi.tripdata`
  WHERE fare_amount = 0;
  ```

Answer: 8333

# Question 5

Answer: Partition by tpep_dropoff_datetime and Cluster on VendorID

# Question 6

First, run query:

  ```SQL
  SELECT DISTINCT VendorID
  FROM `nytaxi.tripdata`
  WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15 23:59:59';
  ```

Estimated size: 310,24 Mo.

Then, run command:

  ```SQL
  CREATE OR REPLACE TABLE `nytaxi.tripdata_partitioned`
  PARTITION BY DATE(tpep_dropoff_datetime)
  CLUSTER BY VendorID
  AS
  SELECT * FROM `nytaxi.tripdata`;
  ```

Now run the same query, but for the partitioned table:

  ```SQL
  SELECT DISTINCT VendorID
  FROM `nytaxi.tripdata_partitioned`
  WHERE tpep_dropoff_datetime BETWEEN '2024-03-01' AND '2024-03-15 23:59:59';
  ```

Estimated size: 26,84 Mo.

Answer: 310.24 MB for non-partitioned table and 26.84 MB for the partitioned table

# Question 7

Answer: GCP Bucket

# Question 8

Answer: false, in databases with size smaller then 1 Go clustering might not affect performance.

# Question 9

Answer: it estimates 0, because COUNT(*) without filters is essentially free, as it uses cached metadata rather than scanning table data.
