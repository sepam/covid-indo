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

# Jakarta chart
st.markdown('**Jakarta**')
chart_jkt = daily_cases(df, 'jkt')
st.altair_chart(chart_jkt)

# Indonesia chart
st.markdown('**Indonesia**')
chart_id = daily_cases(df, 'id')
st.altair_chart(chart_id)
