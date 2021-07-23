import altair as alt


def daily_cases(df, region):
    if region == "id":
        region_col = 'Positif Harian (Indonesia)'
        title = 'Daily New Cases Indonesia'
    elif region == "jkt":
        region_col = 'Positif Harian (Jakarta)'
        title = 'Daily New Cases Jakarta'
    else:
        raise ValueError("Specify region argument as either 'id' or 'jkt'")

    chart = alt.Chart(df, title=title).mark_bar().encode(
        x=alt.X('Tanggal', title='Date'),
        y=alt.Y(region_col, title='Daily Positive Cases'),
        tooltip=[
            alt.Tooltip('Tanggal', title='Date'),
            alt.Tooltip(region_col, format=',', title='Daily Cases')
        ]
    )
    return chart
