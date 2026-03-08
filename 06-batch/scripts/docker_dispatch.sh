#!/usr/bin/env bash
set -euo pipefail

QUESTION="${1:-help}"

run_python() {
  python "06-batch/scripts/$1"
}

download_data() {
  mkdir -p 06-batch/data
  curl -fL "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2025-11.parquet" \
    -o "06-batch/data/yellow_tripdata_2025-11.parquet"
  curl -fL "https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv" \
    -o "06-batch/data/taxi_zone_lookup.csv"
  ls -lh 06-batch/data
}

case "$QUESTION" in
  download)
    download_data
    ;;
  q1)
    run_python "q1_spark_version.py"
    ;;
  q2)
    run_python "q2_repartition_avg_size.py"
    ;;
  q3)
    run_python "q3_count_2025_11_15.py"
    ;;
  q4)
    run_python "q4_longest_trip_hours.py"
    ;;
  q5)
    run_python "q5_spark_ui_port.py"
    ;;
  q6)
    run_python "q6_least_frequent_pickup_zone.py"
    ;;
  all)
    download_data
    run_python "q1_spark_version.py"
    run_python "q2_repartition_avg_size.py"
    run_python "q3_count_2025_11_15.py"
    run_python "q4_longest_trip_hours.py"
    run_python "q5_spark_ui_port.py"
    run_python "q6_least_frequent_pickup_zone.py"
    ;;
  help|*)
    cat <<'EOF'
Usage:
  docker compose -f 06-batch/docker-compose.yml run --rm spark download
  docker compose -f 06-batch/docker-compose.yml run --rm spark q1
  docker compose -f 06-batch/docker-compose.yml run --rm spark q2
  docker compose -f 06-batch/docker-compose.yml run --rm spark q3
  docker compose -f 06-batch/docker-compose.yml run --rm spark q4
  docker compose -f 06-batch/docker-compose.yml run --rm spark q5
  docker compose -f 06-batch/docker-compose.yml run --rm spark q6
  docker compose -f 06-batch/docker-compose.yml run --rm spark all
EOF
    ;;
esac
