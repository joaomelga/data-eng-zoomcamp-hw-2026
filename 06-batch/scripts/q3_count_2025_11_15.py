import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    input_path = Path("06-batch/data/yellow_tripdata_2025-11.parquet")

    spark = (
        SparkSession.builder
        .appName("hw6-q3-count")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )

    df = spark.read.parquet(str(input_path))
    result = (
        df.where(F.to_date(F.col("tpep_pickup_datetime")) == F.lit("2025-11-15"))
        .count()
    )

    print(f"trip_count_2025_11_15={result}")
    spark.stop()


if __name__ == "__main__":
    main()
