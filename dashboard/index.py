from dash import Dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.COSMO, dbc.icons.BOOTSTRAP]
app_title = "YT Findex"

app = Dash(__name__, external_stylesheets=external_stylesheets,
            meta_tags=[{'name': 'viewport'},
               {'content': 'width=device-width, initial-scale=1.0'}
            ]
)
app.title = app_title
