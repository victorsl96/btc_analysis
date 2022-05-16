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
fig = go.Figure(layout=dict(template='plotly_dark'))

fig.add_trace(go.Scatter(x=df['Date'],
                         y=df['Close'],
                         mode='lines',
                         hovertemplate = 'Date: %{x}' + 
                                         '<br>Closing Price: %{y:$.2f}<extra></extra>',
                         line=dict(color='#F48533')))

fig.update_layout(title='Bitcoin price history',
                  xaxis=dict(title='Date',showgrid=False),
                  yaxis=dict(title='Closing Price',showgrid=False)
                #   plot_bgcolor='#1F1D1D'   ,              
                #   paper_bgcolor='#1F1D1D'  
                #   margin=go.Margin(l=15,r=15,t=20,b=20)               
                                   ) 




fig2 = go.Figure(go.Bar(y=df['Volume'],x=df['Date']),layout=dict(template='plotly_dark'))

fig2.update_layout(title='Volume',
                  xaxis=dict(title='Date',showgrid=False),
                  yaxis=dict(title='Volume',showgrid=False)
                #   plot_bgcolor='#1F1D1D'   ,             
                #   paper_bgcolor='#1F1D1D'    
                #   margin=go.Margin(l=15,r=15,t=20,b=20)               
                                   ) 

# fig.update_traces(fillpattern_shape=[df['High'],df['Low']], selector=dict(type='scatter'))

app.layout = dbc.Container(
    dbc.Row([
        dbc.Col([
            html.Div([
                html.Img(id='logo',src=app.get_asset_url('logo.png'), height=50),
                html.H5('Bitcoin price history'),
                dbc.Button('BTC',color='warning', id='btc_button',size='lg')
                     ], style={'margin-top':'40px','margin-bottom':'40px','margin-left':'40px','margin-right':'40px'}),
            
            html.Div([
                dcc.DatePickerSingle(id = 'date-picker',
                                     min_date_allowed=df['Date'].min(),
                                     max_date_allowed=df['Date'].max(),
                                     display_format='MMMM D, YYYY',
                                     date = df['Date'].max(),
                                     style={'border':'0px solid black'}
                                )
            ])
        ]),
    
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([
                    html.span #50:41 
                ])
            ])
        ]),
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='line_chart',figure=fig,style={'margin-top':'40px','margin-bottom':'40px','margin-left':'40px','margin-right':'40px'})
        ])]),

    dbc.Row([
        dbc.Col([
            dcc.Graph(id='volume_chart',figure=fig2,style={'margin-top':'40px','margin-bottom':'40px','margin-left':'40px','margin-right':'40px'})
        ])
    ])
    ])
)

if __name__ == '__main__':
    app.run_server(debug=True)