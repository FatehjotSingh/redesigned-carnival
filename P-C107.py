import pandas as pd
import plotly.graph_objects as po
import csv

file=pd.read_csv('7.csv')
s1= file.loc[file['student_id']=='TRL_abc']

mn=s1.groupby('level')['attempt'].mean()
print(mn)

fig= po.Figure(po.Line(x= mn, y=['Level 1','Level 2','Level 3','Level 4'],orientation='h'))
fig.show() 
