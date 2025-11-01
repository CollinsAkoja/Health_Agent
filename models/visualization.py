## Visualisation.py

import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def plot_idp_trends(df):
    plt.figure(figsize=(10,6))
    plt.bar(df["country"], df["idp_count"], color="skyblue")
    plt.title(f"IDP Population overview({datetime.now().strftime('%Y-%m-%d')})")
    plt.xlabel("Country")
    plt.ylabel("Internally Displaced  Persons(IDPs)")
    plt.show()


