import os
from pathlib import Path

from pyspark.sql import SparkSession
from pyspark.sql import functions as F


def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    base_dir = Path("06-batch/data")
    trips_path = base_dir / "yellow_tripdata_2025-11.parquet"
    zones_path = base_dir / "taxi_zone_lookup.csv"

    spark = (
        SparkSession.builder
        .appName("hw6-q6-least-zone")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )

    trips = spark.read.parquet(str(trips_path))
    zones = (
        spark.read.option("header", True).csv(str(zones_path))
        .select(
            F.col("LocationID").cast("int").alias("LocationID"),
            F.col("Zone"),
        )
    )

    joined = trips.join(zones, trips.PULocationID == zones.LocationID, "left")
    counts = (
        joined.where(F.col("Zone").isNotNull())
        .groupBy("Zone")
        .count()
        .orderBy(F.col("count").asc(), F.col("Zone").asc())
    )

    row = counts.first()
    print(f"least_frequent_zone={row['Zone']}")
    print(f"least_frequent_zone_count={row['count']}")

    candidates = [
        "Governor's Island/Ellis Island/Liberty Island",
        "Arden Heights",
        "Rikers Island",
        "Jamaica Bay",
    ]
    print("candidate_counts:")
    for candidate in candidates:
        candidate_count = (
            counts.where(F.col("Zone") == F.lit(candidate)).select("count").first()
        )
        value = candidate_count["count"] if candidate_count else 0
        print(f"- {candidate}: {value}")

    spark.stop()


if __name__ == "__main__":
    main()
