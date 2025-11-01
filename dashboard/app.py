## __app.py__

import streamlit as st
import pandas as pd
from datetime import datetime
import altair as alt


## setting up parameters

st.set_page_config(page_title = "Health_Agent Live Dashboard", layout = "wide")

st.title(" Health_ai Live IDP and Health Monitoring Dashboar ")
st.markdown("This Dashboard visualizes real-time IDP and health data stream")

upload = st.file_uploader("Upload csv data(IDP/Health)", type = ["csv"])
if upload:
    df =pd.read_csv(upload)
    st.write(df.head())

    chart = (
        alt.chart(df)
        .mark_bar()
        .encode(
            x = "country",
            y = "idps_count"
            tooltip = ["region", "health_cases"]
        )
    .properties(width = 600, )
    )
    st.altair_chart(chart)
else:
    st.info("Upload or connect to live data to view charts.")