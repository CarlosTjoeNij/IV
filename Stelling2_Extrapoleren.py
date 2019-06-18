test=df[df["Regions"]=="Nederland"]
test

full = go.Scatter(
    x = test["Periods"],
    y = test["gemiddelde huizenprijs"],
        name=provincie,
    line = dict(
        color = ('rgb(12, 140, 36)'),
        width = 9,)
)

schatting =  go.Scatter(
    x = [2017, 2018, 2019, 2020],
    y = [263295, 278000, 290000, 300000],
    line = dict(
        color = ('rgb(249, 38, 164)'),
        width = 9,)

)


data = [full, schatting]

layout = go.Layout(
    showlegend = False,
    title = 'Extrapolatie gemiddelde huizenprijzen van NL'
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)
