"""@bruin
name: ingestion.trips
type: python
image: python:3.11
connection: duckdb-default

materialization:
  type: table
  strategy: append

columns:
  - name: pickup_datetime
    type: timestamp
    description: "When the meter was engaged"
  - name: dropoff_datetime
    type: timestamp
    description: "When the meter was disengaged"
@bruin"""

import os
import json
import pandas as pd

def materialize():
    start_date = os.environ["BRUIN_START_DATE"]
    end_date = os.environ["BRUIN_END_DATE"]
    taxi_types = json.loads(os.environ["BRUIN_VARS"]).get("taxi_types", ["yellow"])

    # Generate list of months between start and end dates
    start = pd.to_datetime(start_date)
    end = pd.to_datetime(end_date)
    months = pd.date_range(start=start, end=end, freq='MS')
    
    all_dataframes = []
    
    for taxi_type in taxi_types:
        for month in months:
            year = month.year
            month_num = month.month
            
            # Construct URL
            url = f"https://d37ci6vzurychx.cloudfront.net/trip-data/{taxi_type}_tripdata_{year}-{month_num:02d}.parquet"
            
            try:
                # Fetch parquet file
                df = pd.read_parquet(url)
                
                # Rename columns to match the schema
                # Common column names vary by taxi type, standardize them
                column_mapping = {
                    'tpep_pickup_datetime': 'pickup_datetime',
                    'tpep_dropoff_datetime': 'dropoff_datetime',
                    'lpep_pickup_datetime': 'pickup_datetime',
                    'lpep_dropoff_datetime': 'dropoff_datetime',
                    'pickup_datetime': 'pickup_datetime',
                    'dropoff_datetime': 'dropoff_datetime'
                }
                
                df = df.rename(columns=column_mapping)
                
                # Select only required columns
                required_cols = ['pickup_datetime', 'dropoff_datetime']
                df = df[[col for col in required_cols if col in df.columns]]
                
                all_dataframes.append(df)
                
            except Exception as e:
                print(f"Warning: Could not fetch {url}: {e}")
                continue
    
    # Combine all dataframes
    if all_dataframes:
        final_dataframe = pd.concat(all_dataframes, ignore_index=True)
    else:
        # Return empty dataframe with correct schema if no data found
        final_dataframe = pd.DataFrame(columns=['pickup_datetime', 'dropoff_datetime'])
        final_dataframe['pickup_datetime'] = pd.to_datetime(final_dataframe['pickup_datetime'])
        final_dataframe['dropoff_datetime'] = pd.to_datetime(final_dataframe['dropoff_datetime'])

    return final_dataframe