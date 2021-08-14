from datetime import datetime

import pandas as pd
import streamlit as st

from data.get_data import fetch, URL, SHEET
from plots.daily_cases import daily_cases


# Specify default page config
st.set_page_config(
    page_title="COVID-19 Indonesia",
    layout='wide'
)


# Fetch data
@st.cache(ttl=60*60, show_spinner=False)
def fetch_data():
    data = fetch(URL, SHEET)
    return data


with st.spinner(text="Fetching data ..."):
    df = fetch_data()

last_date = pd.to_datetime(df['Tanggal']).dt.date.iloc[-1]

# Top layout
st.title("COVID-19 in Indonesia")
st.text(f"Last updated: {last_date}")
st.markdown('---')

# Column layout
col1, col2 = st.columns(2)

# Indonesia chart
col1.title('Indonesia')
chart_id = daily_cases(df, 'id')
col1.altair_chart(chart_id.properties(width=600))

# Jakarta chart
col2.title('Jakarta')
chart_jkt = daily_cases(df, 'jkt')
col2.altair_chart(chart_jkt.properties(width=600))
