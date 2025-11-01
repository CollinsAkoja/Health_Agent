## __app.py__

import streamlit as st
import pandas as pd
from datetime import datetime
import altair as alt


## setting up parameters

st.set_page_config(page_title = "Health_Agent Live Dashboard", layout = "wide")

st.title("This Dashboard visualizes real-time IDP and health data stream ")