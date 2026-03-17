import json
from time import time

import pandas as pd
from kafka import KafkaProducer

# Download green taxi trip data for October 2025
url = "https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2025-10.parquet"
columns = [
    'lpep_pickup_datetime',
    'lpep_dropoff_datetime',
    'PULocationID',
    'DOLocationID',
    'passenger_count',
    'trip_distance',
    'tip_amount',
    'total_amount',
]
df = pd.read_parquet(url, columns=columns)

# Convert datetime columns to strings
df['lpep_pickup_datetime'] = df['lpep_pickup_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')
df['lpep_dropoff_datetime'] = df['lpep_dropoff_datetime'].dt.strftime('%Y-%m-%d %H:%M:%S')

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8'),
)

t0 = time()

for _, row in df.iterrows():
    producer.send('green-trips', value=row.to_dict())

producer.flush()

t1 = time()
print(f'Sent {len(df)} rows')
print(f'took {(t1 - t0):.2f} seconds')
