# Solution

Repeat steps from question-3, then connect to pgadmin on `localhost:8085`, login, and add the pgadmin database.

On pgadmin query-tool run: 

```SQL
SELECT z."Zone" AS pickup_zone,
       SUM(g.total_amount) AS total_amount_sum
FROM green_taxi_data g
JOIN taxi_zones z ON g."PULocationID" = z."LocationID"
WHERE DATE(g.lpep_pickup_datetime) = '2025-11-18'
GROUP BY z."Zone"
ORDER BY total_amount_sum DESC
LIMIT 1;
```

Anwser: East Harlem North