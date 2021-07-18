import pandas as pd
import streamlit as st

from data.get_data import fetch, URL, SHEET
from plots.daily_cases import plot_daily_cases_id, plot_daily_cases_jkt


# logic to run up front
@st.cache
def fetch_data():
    data = fetch(URL, SHEET)
    return data


df = fetch_data()

# calculate summary statistics
total_cases_id = df['Positif (Indonesia)'].iloc[-1].astype(int)
total_cases_id_yd = df['Positif (Indonesia)'].iloc[-2].astype(int)
diff_id = total_cases_id - total_cases_id_yd

total_cases_jkt = df['Positif (Jakarta)'].iloc[-1].astype(int)
total_cases_jkt_yd = df['Positif (Jakarta)'].iloc[-2].astype(int)
diff_jkt = total_cases_jkt - total_cases_jkt_yd

last_date = pd.to_datetime(df['Tanggal']).dt.date.iloc[-1]

# Title of the app
st.title("COVID-19 in Indonesia")
st.text("Data Source: https://corona.jakarta.go.id/")
st.text(f"Last updated: {last_date}")

# Indonesia
st.title('Indonesia')
st.markdown('---')

if diff_id > 0:
    diff_id_text = f'<span style="color:Red; font-size: 20px;">(+{diff_id:,})</span>'
else:
    diff_id_text = f'<span style="color:Green; font-size: 20px;">({diff_id:,})</span>'

st.markdown(f'## **Total Positive Cases**: {total_cases_id:,} {diff_id_text}',
            unsafe_allow_html=True)

chart1 = plot_daily_cases_id(df)
st.altair_chart(chart1.properties(width=800))

# Jakarta
st.title('Jakarta')
st.markdown('---')

if diff_id > 0:
    diff_jkt_text = f'<span style="color:Red; font-size: 20px;">(+{diff_jkt:,})</span>'
else:
    diff_jkt_text = f'<span style="color:Green; font-size: 20px;">({diff_jkt:,})</span>'

st.markdown(
    f'## **Total Positive Cases**: {total_cases_jkt:,} {diff_jkt_text}',
    unsafe_allow_html=True)

chart2 = plot_daily_cases_jkt(df)
st.altair_chart(chart2.properties(width=800))
