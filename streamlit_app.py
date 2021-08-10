from datetime import datetime

import pandas as pd
import streamlit as st

from data.get_data import fetch, URL, SHEET
from plots.daily_cases import daily_cases


# Specify default page config
st.set_page_config(
    page_title="COVID-19 Jakarta",
)


# Fetch data
@st.cache(ttl=60*60, show_spinner=False)
def fetch_data():
    data = fetch(URL, SHEET)
    return data


with st.spinner(text="Fetching data"):
    df = fetch_data()

# Calculate summary statistics
total_cases_id = df['Positif (Indonesia)'].iloc[-1].astype(int)
total_cases_id_yd = df['Positif (Indonesia)'].iloc[-2].astype(int)
incr_id = total_cases_id - total_cases_id_yd

total_cases_jkt = df['Positif (Jakarta)'].iloc[-1].astype(int)
total_cases_jkt_yd = df['Positif (Jakarta)'].iloc[-2].astype(int)
incr_jkt = total_cases_jkt - total_cases_jkt_yd

current_date = datetime.now().date().__str__()
last_date = pd.to_datetime(df['Tanggal']).dt.date.iloc[-1]

# Top layout
st.title("COVID-19 in Jakarta")
st.text("Data Source:")
st.markdown("[https://corona.jakarta.go.id/](https://corona.jakarta.go.id/)")
st.text(f"Current date: {current_date}")
st.text(f"Last updated: {last_date}")

# data_button = st.checkbox('Show data')
# if data_button:
#     st.dataframe(df)

# Indonesia statistics
st.title('Indonesia')
st.markdown('---')

incr_id_text = f'<span style="color:Red; font-size: 20px;">(+{incr_id:,})</span>'
st.markdown(f'## **Total Positive Cases**: {total_cases_id:,} {incr_id_text}', unsafe_allow_html=True)

chart_id = daily_cases(df, 'id')
st.altair_chart(chart_id.properties(width=800))

# Jakarta statistics
st.title('Jakarta')
st.markdown('---')

incr_jkt_text = f'<span style="color:Red; font-size: 20px;">(+{incr_jkt:,})</span>'
st.markdown(f'## **Total Positive Cases**: {total_cases_jkt:,} {incr_jkt_text}', unsafe_allow_html=True)

chart_jkt = daily_cases(df, 'jkt')
st.altair_chart(chart_jkt.properties(width=800))
