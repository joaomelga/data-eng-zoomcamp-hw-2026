#!/bin/bash

MONTH_START=01
MONTH_END=12
ARGS=()

usage() {
  echo "Usage: ./trigger_loop.sh <year> <taxi> [--month-start MM] [--month-end MM]"
  echo "Example: ./trigger_loop.sh 2020 green --month-start 01 --month-end 09"
}

while [ $# -gt 0 ]; do
  case "$1" in
    --month-start)
      MONTH_START="$2"
      shift 2
      ;;
    --month-end)
      MONTH_END="$2"
      shift 2
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --)
      shift
      break
      ;;
    *)
      ARGS+=("$1")
      shift
      ;;
  esac
done

YEAR="${ARGS[0]}"
TAXI="${ARGS[1]}"

if [ -z "$YEAR" ] || [ -z "$TAXI" ]; then
  usage
  exit 1
fi

if ! [[ "$MONTH_START" =~ ^(0[1-9]|1[0-2])$ ]]; then
  echo "Invalid --month-start: $MONTH_START (expected 01-12)"
  exit 1
fi

if ! [[ "$MONTH_END" =~ ^(0[1-9]|1[0-2])$ ]]; then
  echo "Invalid --month-end: $MONTH_END (expected 01-12)"
  exit 1
fi

START_NUM=$((10#$MONTH_START))
END_NUM=$((10#$MONTH_END))

if [ "$START_NUM" -gt "$END_NUM" ]; then
  echo "--month-start must be <= --month-end"
  exit 1
fi

for ((m=START_NUM; m<=END_NUM; m++)); do
  MONTH=$(printf "%02d" "$m")
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
