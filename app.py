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

fig = px.line(df,x='Date', y='Close')
fig.update_layout(bargap=0.2)
fig.show()