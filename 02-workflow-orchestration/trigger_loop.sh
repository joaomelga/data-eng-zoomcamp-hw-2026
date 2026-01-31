#!/bin/bash

YEAR=$1
TAXI=$2

if [ -z "$YEAR" ] || [ -z "$TAXI" ]; then
  echo "Usage: ./trigger_loop.sh <year> <taxi>"
  echo "Example: ./trigger_loop.sh 2020 green"
  exit 1
fi

for MONTH in 01 02 03 04 05 06 07 08 09 10 11 12; do
  echo "Triggering $TAXI $YEAR-$MONTH..."
  curl -X POST "http://localhost:8080/api/v1/executions/zoomcamp/09_local_taxi_scheduled" \
    -u "admin@kestra.io:Admin1234!" \
    -F "taxi=$TAXI" \
    -F "year=$YEAR" \
    -F "month=$MONTH"
  echo ""
  sleep 2
done

echo "Done!"
