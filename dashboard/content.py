from dashboard.index import app
from dash import html, dcc
from dashboard.index import dbc
from dashboard.layout.callbacks import callback1
from dashboard.layout.navbar import navbar
#######################################COMPONENTS#######################################

#######################################APP#######################################


app.layout = dbc.Container(children=[
    navbar,
    html.Div(children='''
        Scalpex Index but further'''),

    dcc.Graph(
        id='current-week-pie'
    ),

    html.Div(id='random_record',children=[]),
    dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0)
],
fluid=True)

