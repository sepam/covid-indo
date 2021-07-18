from datetime import datetime

import pandas as pd
import streamlit as st

from data.get_data import fetch, URL, SHEET
from plots.daily_cases import plot_daily_cases_id, plot_daily_cases_jkt


st.set_page_config(
    page_title="COVID-19 Indonesia",
    # layout="wide"
)

# logic to run up front
@st.cache(ttl=60*60)
def fetch_data():
    data = fetch(URL, SHEET)
    return data


df = fetch_data()

# calculate summary statistics
total_cases_id = df['Positif (Indonesia)'].iloc[-1].astype(int)
total_cases_id_yd = df['Positif (Indonesia)'].iloc[-2].astype(int)
incr_id = total_cases_id - total_cases_id_yd

total_cases_jkt = df['Positif (Jakarta)'].iloc[-1].astype(int)
total_cases_jkt_yd = df['Positif (Jakarta)'].iloc[-2].astype(int)
incr_jkt = total_cases_jkt - total_cases_jkt_yd

current_date = datetime.now().date().__str__()
last_date = pd.to_datetime(df['Tanggal']).dt.date.iloc[-1]

# Title of the app
st.title("COVID-19 in Indonesia")
st.text("Data Source: https://corona.jakarta.go.id/")
st.text(f"Current date: {current_date}")
st.text(f"Last updated: {last_date}")

# Indonesia
st.title('Indonesia')
st.markdown('---')

incr_id_text = f'<span style="color:Red; font-size: 20px;">(+{incr_id:,})</span>'

st.markdown(f'## **Total Positive Cases**: {total_cases_id:,} {incr_id_text}',
            unsafe_allow_html=True)

chart1 = plot_daily_cases_id(df)
st.altair_chart(chart1.properties(width=800))

# Jakarta
st.title('Jakarta')
st.markdown('---')

incr_jkt_text = f'<span style="color:Red; font-size: 20px;">(+{incr_jkt:,})</span>'

st.markdown(
    f'## **Total Positive Cases**: {total_cases_jkt:,} {incr_jkt_text}',
    unsafe_allow_html=True)

chart2 = plot_daily_cases_jkt(df)
st.altair_chart(chart2.properties(width=800))
