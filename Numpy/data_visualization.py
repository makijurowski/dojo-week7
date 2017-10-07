import plotly.plotly as py
import plotly.graph_objs as go
import plotly.figure_factory as FF
# import matplotlib.pyplot as plt; plt.rcdefaults()
import pandas as pd
import numpy as np
# import matplotlib.pyplot as plt


# reader = csv.reader(open("2012_Workplace_Fatalities_by_State.csv", "rb"), delimiter=",")
# x = list(reader)

# result = numpy.array(x)

# states = result[1:(-1),0]
# # result = numpy.array(x).astype("float")

# # print(result)
# print(states)


df = pd.read_csv('2012_Workplace_Fatalities_by_State.csv')

sample_data_table = FF.create_table(df.head())
py.iplot(sample_data_table, filename='sample-data-table')
