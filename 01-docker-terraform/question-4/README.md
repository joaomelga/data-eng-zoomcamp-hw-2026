# Solution

Repeat steps from question-3, then connect to pgadmin on `localhost:8085`, login, and add the pgadmin database.

On pgadmin query-tool run: 

```SQL
SELECT DATE(lpep_pickup_datetime) AS pickup_day,
       trip_distance
FROM green_taxi_data
WHERE trip_distance < 100
ORDER BY trip_distance DESC
LIMIT 1;
```

Anwser: 2025-11-14