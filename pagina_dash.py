import dash
from dash import Dash, html
from dash import dcc
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy as stats
import matplotlib.cbook as cbook
import math
import re
import plotly.express as px
import plotly.graph_objects as go
import warnings
from funciones import *

sns.set_palette("deep", desat=.6)
sns.set_context(rc={"figure.figsize":(8,4)} )





app = dash.Dash()

app.layout = html.Div([
    html.H1("Gráficos de la Comisión Nacional de Seguros y Fianzas (CNSF)"),
    html.Hr(),
    html.H2("Instituciones"),
    html.P("Como se puede observar no hay algún tipo de sesgo al momento de las institusiones emitir los seguros, quiza la mayor variación se debe simplemente al hecho de que hay más personas interesadas en contratar con una organización y como hay mayor número de inscritos a esto se debe la diferencia entre hombres y mujeres donde se ve como hay una tendencia más marcada en NA40044."),
    dcc.Graph(id="Instituciones", figure = grouped_bar_chart(dfco,'MODALIDAD DE LA POLIZA')),
    html.Hr(),
    html.P("Como se puede observar no hay algún tipo de sesgo al momento de las institusiones emitir los seguros, quiza la mayor variación se debe simplemente al hecho de que hay más personas interesadas en contratar con una organización y como hay mayor número de inscritos a esto se debe la diferencia entre hombres y mujeres donde se ve como hay una tendencia más marcada en NA40044."),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ]),
    html.H5("Lista sin numeros"),
    html.Ul([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    html.H5("Lista enumerada"),
    html.Ol([
        html.Li("Coffee"),
        html.Li("Tea"),
        html.Li("Milk"),
    ]),
    ])

if __name__ == '__main__':
    app.run_server()

    app.layout = html.Div([
    html.H1("Hola Dash!"),
    html.H3("Mi primera app de Dash"),
    html.P("Esta es la muestra de una aplicacion de dash, no hemos creado gráficos pero estamos poniendo información"),
    html.Table([
        html.Tr([
            html.Th("Company"),
            html.Th("Contact"),
            html.Th("Country")
        ]),
        html.Tr([
            html.Td("Alfreds Futterkiste"),
            html.Td("Maria Anders"),
            html.Td("Germany")
        ]),
        html.Tr([
            html.Td("Centro comercial Moctezuma"),
            html.Td("Francisco Chang"),
            html.Td("Mexico")
        ]),
    ])
    ])