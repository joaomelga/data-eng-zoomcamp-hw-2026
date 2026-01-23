# Solution

Compy compose services from instructions to `compose.yml`.

Run following commands

```bash
docker compose -f compose.yml up -d
docker exec -it pgadmin sh
```

Then, in `pgadmin` the container `shell`, run:

```bash
python -c "import socket; s = socket.socket(); s.connect(('db', 5433)); print('Connection successful'); s.close()"

# substitute "db" by "localhost" or "postrgres" to test
# substitue 5433 by 5432 to test
```

Anwser: db:5432 and postgres:5432