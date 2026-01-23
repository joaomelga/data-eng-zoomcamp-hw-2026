#!/usr/bin/env python
# coding: utf-8

import os
import click
import pandas as pd
from sqlalchemy import create_engine


@click.command()
@click.option('--pg-user', default='root', help='PostgreSQL user')
@click.option('--pg-pass', default='root', help='PostgreSQL password')
@click.option('--pg-host', default='localhost', help='PostgreSQL host')
@click.option('--pg-port', default=5432, type=int, help='PostgreSQL port')
@click.option('--pg-db', default='ny_taxi', help='PostgreSQL database name')
@click.option('--taxi-table', default='green_taxi_data', help='Green taxi data table name')
@click.option('--zones-table', default='taxi_zones', help='Taxi zones table name')
def run(pg_user, pg_pass, pg_host, pg_port, pg_db, taxi_table, zones_table):
    """Ingest NYC taxi data and zones into PostgreSQL database."""
    
    script_dir = '/code'
    parquet_file = os.path.join(script_dir, 'green_tripdata_2025-11.parquet')
    zones_file = os.path.join(script_dir, 'taxi_zone_lookup.csv')

    engine = create_engine(f'postgresql://{pg_user}:{pg_pass}@{pg_host}:{pg_port}/{pg_db}')

    # Ingest green taxi data from parquet
    print(f"Reading parquet file: {parquet_file}")
    df_taxi = pd.read_parquet(parquet_file)
    print(f"Loaded {len(df_taxi)} taxi trip records")
    
    print(f"Ingesting taxi data into table '{taxi_table}'...")
    df_taxi.to_sql(
        name=taxi_table,
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"Successfully ingested taxi data into '{taxi_table}'")

    # Ingest taxi zones from CSV
    print(f"Reading zones file: {zones_file}")
    df_zones = pd.read_csv(zones_file)
    print(f"Loaded {len(df_zones)} zone records")
    
    print(f"Ingesting zones data into table '{zones_table}'...")
    df_zones.to_sql(
        name=zones_table,
        con=engine,
        if_exists='replace',
        index=False
    )
    print(f"Successfully ingested zones data into '{zones_table}'")

    print("Data ingestion complete!")


if __name__ == '__main__':
    run()