import os
from pyspark.sql import SparkSession


def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    spark = (
        SparkSession.builder
        .appName("hw6-q1-spark-version")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )
    print(f"spark.version={spark.version}")
    spark.stop()


if __name__ == "__main__":
    main()
