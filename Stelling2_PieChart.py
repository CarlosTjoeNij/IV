df2 = pd.read_csv('New.csv', sep=';')
tijdens = df2[df2["Perioden"] == "2010 december"]
na = df2[df2["Perioden"] == "2016 december"]

fig = {
  "data": [
    {
      "values": tijdens["Banen van werknemers in december (x 1 000)"],
      "labels": tijdens["Regio's"],
      "domain": {"column": 0},
      "name": "value",
      "hoverinfo":"label",
      "hole": .4,
      "type": "pie",
      "marker": {"colors": ['rgb(23, 176, 193)','rgb(0, 55, 255)','rgb(56, 105, 255)',   
                            'rgb(29, 53, 127)', 'rgb(94, 71, 178)','rgb(65, 101, 211)', 'rgb(255, 0, 93)',
                            'rgb(255, 0, 220)','rgb(110, 140, 234)', 
                            'rgb(170, 191, 255)', 'rgb(141, 153, 188)',
                           ]},
    },
    {
      "values": na["Banen van werknemers in december (x 1 000)"],
      "labels": na["Regio's"],
      "text":["Na"],
      "textposition":"inside",
      "domain": {"column": 1},
      "name": "value",
      "hoverinfo":"label",
      "hole": .4,
      "type": "pie",
      "marker": {"colors": ['rgb(23, 176, 193)','rgb(0, 55, 255)','rgb(56, 105, 255)',   
                            'rgb(29, 53, 127)', 'rgb(94, 71, 178)','rgb(65, 101, 211)', 'rgb(255, 0, 93)',
                            'rgb(255, 0, 220)','rgb(110, 140, 234)', 
                            'rgb(170, 191, 255)', 'rgb(141, 153, 188)',
                           ]},
    }],
  "layout": {
        "title":"Verdeling aantal banen in Nederland tijdens en na de crisis",
        "grid": {"rows": 1, "columns": 2},
        "annotations": [
            {
                "font": {
                    "size": 28,
                    "family":"Century Gothic",
                    "color":"rgb(68, 38, 153)"
                },
                "showarrow": False,
                "text": "Tijdens",
                "x": 0.17,
                "y": 0.5
            },
            {
                "font": {
                    "size": 31,
                    "family":"Century Gothic",
                    "color":"rgb(68, 38, 153)"
                },
                "showarrow": False,
                "text": "Na",
                "x": 0.8,
                "y": 0.5
            }
        ]
    }
}
iplot(fig)
