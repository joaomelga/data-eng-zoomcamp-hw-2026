# Solution

Repeat steps from question-3, then connect to pgadmin on `localhost:8085`, login, and add the pgadmin database.

On pgadmin query-tool run: 

```SQL
SELECT dz."Zone" AS dropoff_zone,
       MAX(g.tip_amount) AS max_tip
FROM green_taxi_data g
JOIN taxi_zones pz ON g."PULocationID" = pz."LocationID"
JOIN taxi_zones dz ON g."DOLocationID" = dz."LocationID"
WHERE pz."Zone" = 'East Harlem North'
  AND g.lpep_pickup_datetime >= '2025-11-01'
  AND g.lpep_pickup_datetime < '2025-12-01'
GROUP BY dz."Zone"
ORDER BY max_tip DESC
LIMIT 1;
```

Anwser: Yorkville West