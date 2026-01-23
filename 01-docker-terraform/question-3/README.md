# Solution

Install uv by running:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Download data:

```bash
wget https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-11.parquet

wget https://github.com/DataTalksClub/nyc-tlc-data/releases/download/misc/taxi_zone_lookup.csv
```


Run following commands on `/question-3` dir:

```bash
uv lock

docker compose -f compose.yml up -d

docker build -t taxi_ingest:v001 .

docker run -it \
  --network=pg-network \
  taxi_ingest:v001 \
    --pg-user=root \
    --pg-pass=root \
    --pg-host=pgdatabase \
    --pg-port=5432 \
    --pg-db=ny_taxi
```

Connect to pgadmin on `localhost:8085`, login, and add the pgadmin database.

On pgadmin query-tool run: 

```SQL
SELECT COUNT(*) AS short_trips_count
FROM green_taxi_data
WHERE lpep_pickup_datetime >= '2025-11-01'
  AND lpep_pickup_datetime < '2025-12-01'
  AND trip_distance <= 1;
```

Anwser: 8007