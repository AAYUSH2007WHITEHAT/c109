import pandas as pd 
import csv
import plotly.figure_factory as ff 
df = pd.read_csv("data.csv")
fig=ff.create_distplot([df["Height"].tolist()],["Height"],show_hist=False)
fig.show()
fig1=ff.create_distplot([df["Weight"].tolist()],["Weight"],show_hist=False)
fig1.show()