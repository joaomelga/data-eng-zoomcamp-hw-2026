# Pre-requisites

- Build the Spark Docker image (latest Spark + Java 17):

  ```bash
  cd workshop
  docker compose up -d --build
  ```

# Question 1

Run:

```bash
docker exec -it workshop-redpanda-1 rpk topic create green-trips

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