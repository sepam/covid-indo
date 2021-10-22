import altair as alt


def daily_cases(df, region):
    if region == "id":
        region_col = 'Positif Harian (Indonesia)'
    elif region == "jkt":
        region_col = 'Positif Harian (Jakarta)'
    else:
        raise ValueError("Specify region argument as either 'id' or 'jkt'")

    chart = alt.Chart(df).mark_area(
        color="lightblue",
        line=True,
        interpolate='step-after'
    ).encode(
        x=alt.X('Tanggal', title='Date'),
        y=alt.Y(region_col, title='Daily Positive Cases'),
    )

    # Create a selection that chooses the nearest point & selects based on x-value
    nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['Tanggal'], empty='none')

    # Transparent selectors across the chart. This is what tells us
    # the x-value of the cursor
    selectors = alt.Chart(df).mark_point().encode(
        x='Tanggal',
        opacity=alt.value(0),
    ).add_selection(
        nearest
    )

    # Draw points on the line, and highlight based on selection
    points = chart.mark_point(color='#F63366').encode(
        opacity=alt.condition(nearest, alt.value(1), alt.value(0))
    )

    # Draw text labels near the points, and highlight based on selection
    text = chart.mark_text(align='left', dx=-30, dy=-25, color='#F63366').encode(
        text=alt.condition(nearest, region_col, alt.value(' '))
    )

    # Draw a rule at the location of the selection
    rules = alt.Chart(df).mark_rule(color='#F63366').encode(
        x='Tanggal',
    ).transform_filter(
        nearest
    )

    # Put the layers into a single chart and bind the data
    layered_chart = alt.layer(
        chart, selectors, points, rules, text
    )
    return layered_chart
