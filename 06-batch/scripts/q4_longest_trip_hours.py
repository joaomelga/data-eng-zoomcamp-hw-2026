import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    input_path = Path("06-batch/data/yellow_tripdata_2025-11.parquet")

    spark = (
        SparkSession.builder
        .appName("hw6-q4-longest-trip")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )

    df = spark.read.parquet(str(input_path))
    max_hours = (
        df.select(
            (
                (F.unix_timestamp("tpep_dropoff_datetime") - F.unix_timestamp("tpep_pickup_datetime"))
                / F.lit(3600.0)
            ).alias("trip_hours")
        )
        .agg(F.max("trip_hours").alias("max_hours"))
        .first()["max_hours"]
    )

    print(f"longest_trip_hours={float(max_hours):.4f}")
    spark.stop()


if __name__ == "__main__":
    main()
