#!/usr/bin/env python3
"""
Load FHV trip data into DuckDB for dbt processing
"""

import duckdb
from pathlib import Path

def load_fhv_data():
    """Load FHV csv.gz files into DuckDB"""
    
    db_path = "taxi_rides_ny.duckdb"
    data_dir = Path("data/fhv")
    
    if not data_dir.exists():
        print(f"Error: {data_dir} does not exist. Run download_fhv_data.py first.")
        return
    
    # Connect to DuckDB
    conn = duckdb.connect(db_path)
    
    # Create schema if it doesn't exist
    conn.execute("CREATE SCHEMA IF NOT EXISTS prod")
    
    # Drop existing table if it exists
    conn.execute("DROP TABLE IF EXISTS prod.fhv_tripdata")
    
    # Load all FHV csv.gz files
    csv_files = list(data_dir.glob("fhv_tripdata_2019-*.csv.gz"))
    
    if not csv_files:
        print(f"Error: No FHV csv.gz files found in {data_dir}")
        return
    
    print(f"Loading {len(csv_files)} FHV csv.gz files into DuckDB...")
    
    # Create table from csv.gz files
    pattern = str(data_dir / "fhv_tripdata_2019-*.csv.gz").replace('\\', '/')
    
    conn.execute(f"""
        CREATE TABLE prod.fhv_tripdata AS 
        SELECT * FROM read_csv('{pattern}', 
            auto_detect=true,
            compression='gzip',
            timestampformat='%Y-%m-%d %H:%M:%S'
        )
    """)
    
    # Get record count
    result = conn.execute("SELECT COUNT(*) FROM prod.fhv_tripdata").fetchone()
    record_count = result[0]
    
    print(f"✓ Loaded {record_count:,} FHV trip records into prod.fhv_tripdata")
    
    # Show sample data
    print("\nSample data:")
    sample = conn.execute("SELECT * FROM prod.fhv_tripdata LIMIT 5").fetchdf()
    print(sample)
    
    # Show column info
    print("\nColumn information:")
    columns = conn.execute("DESCRIBE prod.fhv_tripdata").fetchdf()
    print(columns)
    
    conn.close()
    print("\n✓ FHV data loaded successfully!")

if __name__ == "__main__":
    load_fhv_data()
