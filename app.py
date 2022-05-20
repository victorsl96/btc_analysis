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

fig.update_layout(title='Asset price history',
                  xaxis=dict(title='Date',showgrid=False),
                  yaxis=dict(title='Closing Price',showgrid=False)
                #   plot_bgcolor='#1F1D1D'   ,              
                #   paper_bgcolor='#1F1D1D'  
                #   margin=go.Margin(l=15,r=15,t=20,b=20)               
                                   ) 




fig2 = go.Figure(go.Bar(y=df['Volume'],x=df['Date']),layout=dict(template='plotly_dark'))

fig2.update_layout(title='Volume (abs)',
                  xaxis=dict(title='Date',showgrid=False),
                  yaxis=dict(title='Volume',showgrid=False)
                #   plot_bgcolor='#1F1D1D'   ,             
                #   paper_bgcolor='#1F1D1D'    
                #   margin=go.Margin(l=15,r=15,t=20,b=20)               
                                   ) 

# fig.update_traces(fillpattern_shape=[df['High'],df['Low']], selector=dict(type='scatter'))

app.layout = dbc.Container(
    dbc.Row([
        dbc.Row([
            dbc.Col([
                html.Div([
                    # html.Img(id='logo',src=app.get_asset_url('https://conteudo.imguol.com.br/c/noticias/c2/2022/01/14/bitcoin-grafico-economia-1642179101668_v2_4x3.jpg'), height=50),
                    html.H1('Cryptocurrency historical data'),
                    dbc.Button('BTC',color='warning', id='btc_button',size='md', style={'margin-bottom':'10px'})
                        ], style={'margin-top':'40px','margin-bottom':'10px'}),
                   ]),

        dbc.Row([
            dbc.Col([
                html.Div([
                dcc.DatePickerSingle(id = 'date-picker',
                                     min_date_allowed=df['Date'].min(),
                                     max_date_allowed=df['Date'].max(),
                                     display_format='MMMM D, YYYY',
                                     date = df['Date'].max(),
                                     style={'border':'0px solid black', 'margin-bottom':'10px','background':'#lelele','background-color':'#lelele'},
                                )
                        ])    
                    ])
                ]),
        
        



        dbc.Row([
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Span('Preço fechamento:'),
                        html.H4(style={'color':'#0D8CFF'},id='price-close-text')
                    ])
                ], color='light',outline=True,style={'margin-top':'10px','box-shadow':'0 4px 0 rgba(0,0,0,0,15), 0 4px 20px 0 rgba(0,0,0,0,0.19)',
                                                    'color':'#FFFFFF'})
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Span('Preço máximo:'),
                        html.H4(style={'color':'#0DFF67'},id='price-high-text')
                    ])
                ], color='light',outline=True,style={'margin-top':'10px','box-shadow':'0 4px 0 rgba(0,0,0,0,15), 0 4px 20px 0 rgba(0,0,0,0,0.19)',
                                                    'color':'#FFFFFF'})
            ], md=4),
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.Span('Preço mínimo:'),
                        html.H4(style={'color':'#94090D'},id='price-low-text')
                    ])
                ], color='light',outline=True,style={'margin-top':'10px','box-shadow':'0 4px 0 rgba(0,0,0,0,15), 0 4px 20px 0 rgba(0,0,0,0,0.19)',
                                                    'color':'#FFFFFF'})
            ], md=4)

        ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='line_chart',figure=fig,style={'height':'50vh','margin-top':'20px'})
                    ])
                ]),

        dbc.Row([
            dbc.Col([
                dcc.Graph(id='volume_chart',figure=fig2,style={'height':'50vh','margin-top':'20px'})
                    ])
                ])
        ])
    ], className="g-0")
, fluid=True)

@app.callback(
    [
        Output('price-close-text','children'),
        Output('price-high-text','children'),
        Output('price-low-text','children')
    ],
    [Input('date-picker','date')]
    )


def display_status(date):

    pclose = 'U$' + str(np.format_float_positional(df['Close'].loc[df['Date'] == date].values[0], precision=2))
    phigh = 'U$' + str(np.format_float_positional(df['High'].loc[df['Date'] == date].values[0], precision=2))
    plow = 'U$' + str(np.format_float_positional(df['Low'].loc[df['Date'] == date].values[0], precision=2))
    
    return (pclose,phigh,plow)


if __name__ == '__main__':
    app.run_server()
