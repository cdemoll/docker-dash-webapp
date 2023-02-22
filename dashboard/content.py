from dashboard.index import app
from dash import html, dcc
from dashboard.index import dbc
# from dashboard.layout.callbacks import nav_toggler
# from dashboard.layout.callbacks import populate_dashtable
from dashboard.layout.callbacks import populate_cstm_pchart
from dashboard.layout.callbacks import populate_barchart
from dashboard.layout.callbacks import populate_dashtable

from dashboard.layout.callbacks import dynamic_pages
from dashboard.layout.navbar import navbar

app.layout = dbc.Container(children=[
    # Fixed navbar that will appear in every pages
    navbar,
    # Dynamic content of our page (SPA)
    html.Div(id='page-content', children=[]),
    # Listener for url change which triggers callback
    dcc.Location(id='url', refresh=False)
],
fluid=True)
