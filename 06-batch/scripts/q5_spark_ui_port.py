import os
from pyspark.sql import SparkSession


def main() -> None:
    os.environ.setdefault("SPARK_LOCAL_IP", "127.0.0.1")

    spark = (
        SparkSession.builder
        .appName("hw6-q5-ui-port")
        .master("local[2]")
        .config("spark.driver.host", "127.0.0.1")
        .config("spark.driver.bindAddress", "127.0.0.1")
        .getOrCreate()
    )

    url = spark.sparkContext.uiWebUrl
    port = "0000"

    if url and ":" in url:
        port = url.rsplit(":", 1)[-1]

    print(f"spark_ui_url={url}")
    print(f"spark_ui_port={port}")
    spark.stop()


if __name__ == "__main__":
    main()
