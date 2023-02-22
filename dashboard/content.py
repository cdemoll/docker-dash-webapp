from dashboard.index import app
from dash import html, dcc
from dashboard.index import dbc
from dashboard.layout.callbacks import nav_toggler
from dashboard.layout.callbacks import populate_dashtable
from dashboard.layout.callbacks import populate_cstm_pchart
from dashboard.layout.callbacks import populate_barchart
from dashboard.layout.navbar import navbar

app.layout = dbc.Container(children=[
    navbar,
    # Dynamic content of our page (SPA)
    html.Div(id='page-content', children=[]),

    dcc.Graph(
        id='current-week-pie'
    ),
    dcc.Graph(
        id='current-week-bar'
    ),

    html.Div(id='random_record',children=[]),
    dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0),
    dcc.Location(id='url', refresh=False)

],
fluid=True)
