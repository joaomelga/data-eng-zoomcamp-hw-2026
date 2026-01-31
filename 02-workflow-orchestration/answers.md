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
