# Pre-requisites

- Build the Spark Docker image (latest Spark + Java 17):

  ```bash
  cd workshop
  docker compose up -d --build
  ```

# Question 1

Run:

```bash
docker exec -it workshop-redpanda-1 rpk version

# Output
rpk version: v25.3.9
Git ref:     836b4a36ef6d5121edbb1e68f0f673c2a8a244e2
Build date:  2026 Feb 26 07 48 21 Thu
OS/Arch:     linux/amd64
Go version:  go1.24.3

Redpanda Cluster
  node-1  v25.3.9 - 836b4a36ef6d5121edbb1e68f0f673c2a8a244e2
```

Answer: `v25.3.9`

# Question 2

Create the topic:

```bash
docker exec workshop-redpanda-1 rpk topic create green-trips

# Output
TOPIC        STATUS
green-trips  OK
```

Run the producer script ([src/producer.py](src/producer.py)):

```bash
python src/producer.py

# Output
Sent 49416 rows
took 6.42 seconds
```

Answer: `10 seconds`

# Question 3

Run the consumer script ([src/consumer.py](src/consumer.py)):

```bash
python src/consumer.py

# Output
Total messages: 49416
Trips with trip_distance > 5.0: 8506
```

Answer: `8506`

# Question 4

Create the PostgreSQL sink table:

```sql
CREATE TABLE q4_tumbling_pickup (
    window_start TIMESTAMP(3),
    PULocationID INT,
    num_trips BIGINT,
    PRIMARY KEY (window_start, PULocationID)
);
```

Submit the Flink job ([workshop/src/job/hw_q4_tumbling_pickup.py](workshop/src/job/hw_q4_tumbling_pickup.py)):

```bash
docker exec workshop-jobmanager-1 flink run -py /opt/src/job/hw_q4_tumbling_pickup.py
```

Query results:

```sql
SELECT pulocationid, num_trips
FROM q4_tumbling_pickup
ORDER BY num_trips DESC
LIMIT 3;

-- Output
--     window_start     | pulocationid | num_trips
-- ---------------------+--------------+-----------
--  2025-10-22 08:40:00 |           74 |        15
--  2025-10-20 16:30:00 |           74 |        14
--  2025-10-08 10:35:00 |           74 |        13
```

Answer: `74`

# Question 5

Create the PostgreSQL sink table:

```sql
CREATE TABLE q5_session_streak (
    PULocationID INT,
    session_start TIMESTAMP(3),
    session_end TIMESTAMP(3),
    num_trips BIGINT,
    PRIMARY KEY (PULocationID, session_start)
);
```

Submit the Flink job ([workshop/src/job/hw_q5_session_streak.py](workshop/src/job/hw_q5_session_streak.py)):

```bash
docker exec workshop-jobmanager-1 flink run -py /opt/src/job/hw_q5_session_streak.py
```

Query results:

```sql
SELECT pulocationid, num_trips, session_start, session_end
FROM q5_session_streak
ORDER BY num_trips DESC
LIMIT 1;

-- Output
--  pulocationid | num_trips |    session_start    |     session_end
-- --------------+-----------+---------------------+---------------------
--            74 |        81 | 2025-10-08 06:46:14 | 2025-10-08 08:27:40
```

Answer: `81`

# Question 6

Create the PostgreSQL sink table:

```sql
CREATE TABLE q6_hourly_tips (
    window_start TIMESTAMP(3),
    total_tips DOUBLE PRECISION,
    PRIMARY KEY (window_start)
);
```

Submit the Flink job ([workshop/src/job/hw_q6_hourly_tips.py](workshop/src/job/hw_q6_hourly_tips.py)):

```bash
docker exec workshop-jobmanager-1 flink run -py /opt/src/job/hw_q6_hourly_tips.py
```

Query results:

```sql
SELECT window_start, total_tips
FROM q6_hourly_tips
ORDER BY total_tips DESC
LIMIT 1;

-- Output
--     window_start     |     total_tips
-- ---------------------+--------------------
--  2025-10-16 18:00:00 |  510.8599999999999
```

Answer: `2025-10-16 18:00:00`