import os
from pathlib import Path

from pyspark.sql import SparkSession

def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    base_dir = Path("06-batch/data")
    input_path = base_dir / "yellow_tripdata_2025-11.parquet"
    output_dir = base_dir / "q2_repartition_4"

    spark = (
        SparkSession.builder
        .appName("hw6-q2-repartition")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )

    df = spark.read.parquet(str(input_path))

    if output_dir.exists():
        import shutil
        shutil.rmtree(output_dir)

    df.repartition(4).write.mode("overwrite").parquet(str(output_dir))

    parquet_files = sorted(output_dir.rglob("*.parquet"))
    sizes_mb = [f.stat().st_size / (1024 * 1024) for f in parquet_files]
    avg_mb = sum(sizes_mb) / len(sizes_mb)

    print(f"parquet_files={len(parquet_files)}")
    print(f"average_size_mb={avg_mb:.4f}")

    spark.stop()


if __name__ == "__main__":
    main()
