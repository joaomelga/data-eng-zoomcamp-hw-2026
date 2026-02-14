#!/usr/bin/env python3
"""
Download FHV (For-Hire Vehicle) trip data for 2019 from NYC TLC
"""

import requests
import os
from pathlib import Path

def download_fhv_data():
    """Download FHV csv.gz files for all months of 2019"""
    base_url = "https://github.com/DataTalksClub/nyc-tlc-data/releases/download/fhv"
    data_dir = Path("data/fhv")
    data_dir.mkdir(parents=True, exist_ok=True)
    
    months = range(1, 13)  # January to December
    year = 2019
    
    for month in months:
        filename = f"fhv_tripdata_{year}-{month:02d}.csv.gz"
        url = f"{base_url}/{filename}"
        output_path = data_dir / filename
        
        if output_path.exists():
            print(f"✓ {filename} already exists, skipping...")
            continue
        
        print(f"Downloading {filename}...")
        try:
            response = requests.get(url, stream=True)
            response.raise_for_status()
            
            with open(output_path, 'wb') as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
            
            file_size_mb = output_path.stat().st_size / (1024 * 1024)
            print(f"✓ Downloaded {filename} ({file_size_mb:.2f} MB)")
            
        except Exception as e:
            print(f"✗ Error downloading {filename}: {e}")
    
    print("\n✓ FHV data download complete!")

if __name__ == "__main__":
    download_fhv_data()
