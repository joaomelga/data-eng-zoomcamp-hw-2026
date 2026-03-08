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
