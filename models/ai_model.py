## app.py

import streamline as st
import pandas as pd
import altair as alt
from datetime import datetime


st.set_page_config(page_title="Heart_Disease Live Dashboard", layout = "wide")
st.title("Heart_Disease - Live IDP and Health Monitoring Dashboard")
st.markdown("This Dashboard visualizes real-time IDP and Health data streams.")

upload =st.file_uploader("Upload CSV data (IDP/Health)", type=["csv"])
if uploaded:
    df = pd.read_csv(uploaded)
    st.write(df.head())

    chart = (
        alt.chart(df)
        .mark_bar()
        .encode(
            x="country",
            y="idps_count",
            color ="country",
            tooltip = ["region","health_cases"]
        )
        .properties(width=600, height=400)

    )
    st.altair_chart(chart)

else:
    st.info("upload or connectlive data to view charts.")


import os
import pandas as pd
from sklearn.model_Selection import tran_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
import joblib

processed_data = "data/processed/idp_data_cleaned.csv"
model_path = "/models/health_risk_model.pkl"

def train_ai_model():
##  Load cleaned data

if not os.path.exists(processed_data):
    print("[!] Cleaned data not found. Run data_cleaner.py first.")
    return
df = pd.read_csv(processed_data)

# Ensure we have numeric columns
df["idps_count"] = pd.to_numeric(df["idps_count"], error = "coerce")
df["health_cases"] = pd.to_numeric(df["health_cases"], error = "coerce")
df.dropna(subset = ["idps_count", "health_cases"], inplace = True)

## Features and likely targets
X = df["idps_count"]
y = df["health_cases"]

# splitting my datas
X_train, X_test, y_train, y_test, = train_test_split(X,y, test_size = 0.2, random_state =42)
## Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_tranform(X_train)
X_test_scaled = scaler.transdform(X_test)

##  Models testing

model = LinearRegression()
model.fit(X_train_scaled, y_train)

## Evaluation
preds = model.predict(X_test, scaled)
mae = mean_absolute_error(y_test, preds)
r2 =r2_score(y_test, preds)
