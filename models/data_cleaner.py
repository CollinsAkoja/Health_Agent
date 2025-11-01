## Data_cleaner.py

import os
import pandas as pd

raw_dir = "/data/raw"
processed_dir = "/data/processed/"

def clean_idp_data():
    os.makedirs(processed_dir, exist_ok=True)

    ## combining csv files

    all_data = []
    for file in os.listdir(raw_dir):
        if file.endswith(".csv"):
            df = pd.read_csv(os.path.join(raw_dir, file))
            all_data.append(df)

    if not all_data:
        print("[!] no raw data found")
        return None

    # noinspection PyArgumentList
    merged_df = pd.read_csv(all_data,ignore_index = True)
    merged_df.drop_duplicates(inplace = True)
    merged_df.to_csv(os.path.join(processed_dir,"idp_data_cleaned.csv"),index = False)
    print("CLean data saved to processed folder")
    return merged_df