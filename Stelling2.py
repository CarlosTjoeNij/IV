# Barchart met 0-lijn, aanduiding crisis


test=df[df["Regions"]=="Nederland"]

full = go.Bar(
    x = test["Periods"],
    y = test["verschil in % in aantal verkochte huizen vergeleken met vorig jaar"],
    name=provincie,
    base = 0,
    width = [0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.6,0.9,0.9,0.9,0.9,0.9,0.9,0.6,0.6,0.6,0.6,0.6],
    marker=dict(
        color=['rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(206, 20, 29)',
               'rgb(206, 20, 29)', 'rgb(206, 20, 29)',
               'rgb(206, 20, 29)', 'rgb(206, 20, 29)',
               'rgb(206, 20, 29)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)', 'rgb(80, 66, 244)',
               'rgb(80, 66, 244)'])
               
)

data = [full]

layout = go.Layout(
    showlegend = False,
    title = 'Aanduiding crisis vanaf 2008 d.m.v. verschil in % in verkochte huizen',
    yaxis = go.layout.YAxis(
        title='Verandering in %'
    ),
    plot_bgcolor='rgb(219, 241, 233)'
    
)

fig = go.Figure(data=data, layout=layout)
iplot(fig)
