from plotly.offline import init_notebook_mode, iplot
import plotly.graph_objs as go
init_notebook_mode(connected=True)
import pandas as pd
import numpy as np
df = pd.read_csv('Bestaande_koopwoningen_regio_2015_100_11062019_105814.csv', sep=';')
test=df[df["Regions"]=="Nederland"]
data=[]
for provincie in df['Regions'].unique():
    randstad=["Noord-Holland (PV)","Zuid-Holland (PV)","Utrecht (PV)"]
    if '(PV)'in provincie:
        test=df[df["Regions"]==provincie]
        if provincie in randstad:
            data.append(go.Scatter(
            x = test["Periods"],
            y = test["gemiddelde huizenprijs"],
                name=provincie,
                line = dict(
                    width = 7)
            ))
        else:
            data.append(go.Scatter(
            x = test["Periods"],
            y = test["gemiddelde huizenprijs"],
                name=provincie))
                
# import geopandas as gpd
# geodf = gpd.read_file("")

iplot(data)
