# Pre-requisites

- Build the Spark Docker image (latest Spark + Java 17):

  ```bash
  docker compose -f 06-batch/docker-compose.yml build
  ```

- Download homework data:

  ```bash
  docker compose -f 06-batch/docker-compose.yml run --rm spark download
  ```

# Question 1

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q1
```

Answer: `spark.version=4.1.1`

# Question 2

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q2
```

Answer: `average_size_mb=25.3313` => 25 is the closest

# Question 3

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q3
```

Answer: `162604`

# Question 4

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q4
```

Answer: `90.6467`

# Question 5

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q5
```

Answer: `4040`

# Question 6

Run:

```bash
docker compose -f 06-batch/docker-compose.yml run --rm spark q6
```

Answer:

- Governor's Island/Ellis Island/Liberty Island: 1
- Arden Heights: 1
