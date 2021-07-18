import altair as alt


def plot_daily_cases_id(df):
    chart = alt.Chart(df, title='Daily New Cases Indonesia').mark_bar().encode(
        x=alt.X('Tanggal', title='Date'),
        y=alt.Y('Positif Harian (Indonesia)', title='Daily Positive Cases'),
        tooltip=[
            alt.Tooltip('Tanggal', title='Date'),
            alt.Tooltip('Positif Harian (Indonesia)', format=',',
                        title='Daily Cases')
        ]
    )
    return chart


def plot_daily_cases_jkt(df):
    chart = alt.Chart(df, title='Daily New Cases Jakarta').mark_bar().encode(
        x=alt.X('Tanggal', title='Date'),
        y=alt.Y('Positif Harian (Jakarta)', title='Daily Positive Cases'),
        tooltip=[
            alt.Tooltip('Tanggal', title='Date'),
            alt.Tooltip('Positif Harian (Jakarta)', format=',',
                        title='Daily Cases')
        ]
    )
    return chart
