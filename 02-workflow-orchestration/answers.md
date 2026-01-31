# Question 1

cd 02-workflow-orchestration

docker compose up

curl -X POST "http://localhost:8080/api/v1/flows" \
  -H "Content-Type: application/x-yaml" \
  -u "admin@kestra.io:Admin1234!" \
  --data-binary @./flows/flow.yml


curl -X POST "http://localhost:8080/api/v1/executions/zoomcamp/09_local_taxi_scheduled" \
  -u "admin@kestra.io:Admin1234!" \
  -F "taxi=yellow" \
  -F "year=2020" \
  -F "month=12"

Download the output CSV from Kestra UI (extract task), then:

stat --printf="%s" yellow_tripdata_2020-12.csv
> 134481400 bytes (~128.3 MiB)

# Question 2

curl -X POST "http://localhost:8080/api/v1/executions/zoomcamp/09_local_taxi_scheduled" \
  -u "admin@kestra.io:Admin1234!" \
  -F "taxi=green" \
  -F "year=2020" \
  -F "month=04"

Open the execution in Kestra UI (example):
http://localhost:8080/ui/main/executions/zoomcamp/09_local_taxi_scheduled/5Ql9J5d7vj82ugwtPZZFEo

Rendered value for `file`: {{inputs.taxi}}_tripdata_{{inputs.year}}-{{inputs.month}}.csv

# Question 3

./trigger_loop.sh 2020 yellow

3007292 + 237993 + 348371 + 549760 + 800412 + 1007284 + 
1341012 + 1681131 + 1508985 + 1461897 + 6405008 + 6299354

= 24648499

# Question 4

./trigger_loop.sh 2020 green

83130 + 88605 + 95120 + 87987 + 81063 + 72257 + 
63109 + 57360 + 35612 + 
223406 + 398632 + 447770

= 1734051
