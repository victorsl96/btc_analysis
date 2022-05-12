#!/usr/bin/env python3

import dash
from dash import dcc
from dash import html
from dash.dependencies import Input,Output
import dash_bootstrap_components as dbc

import plotly.express as px
import plotly.graph_objects as go

import numpy as np
import pandas as pd

df = pd.read_csv('data.csv')
# print(df)

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CYBORG])

# fig = px.line(df,x='Date', y='Close')
# fig.update_layout(
#     bargap=0.2
#     )
# fig.show()
h,l = df['High'],df['Low']
fig = go.Figure()
fig.add_trace(go.Scatter(x=df['Date'],
                         y=df['Close'],
                         mode='lines',
                         hovertemplate = 'Date: %{x}' + 
                                         '<br>Closing Price: %{y:$.2f}<extra></extra>',
                         line=dict(color='orange')))

fig.update_layout(title='Bitcoin price history',
                  xaxis_title='Date',
                  yaxis_title='Closing Price',
                  plot_bgcolor='#242424'                 
                                   ) 

# fig.update_traces(fillpattern_shape=[df['High'],df['Low']], selector=dict(type='scatter'))

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line_chart',figure=fig)
        ])

    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)