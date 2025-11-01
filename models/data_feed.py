## Data_feed.py

import os
import pandas
import pandas as pd
import requests
import datetime

data_dir = "/data/raw"

def fetch_sample():

    """fetch placeholder: simulating live humanitarian or health data feed. from kaggle and other sources
    i will also link chatgptAPI here to enable the chatresponse faster"""

    os.makedirs(DATA_DIR, exist_ok=True)

    # Simulated data
    data = {
        "country": ["Nigeria", "Chad", "Sudan", "Cameroon"],
        "region": ["Borno", "Lac", "Darfur", "Far North"],
        "date": [datetime.now().strftime("%Y-%m-%d")] * 4,
        "idps_count": [53000, 23000, 91000, 17000],
        "health_cases": [400, 120, 700, 230],
    }

    df = pd.DataFrame(data)
    csv_path = os.path.join(DATA_DIR, f"idp_data_{datetime.now().strftime('%Y%m%d')}.csv")
    df.to_csv(csv_path, index = False)
    print(f"Data saved to {csv_path}")
    return df














