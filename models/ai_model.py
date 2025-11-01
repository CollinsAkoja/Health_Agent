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


