from dash import Dash
import dash_bootstrap_components as dbc

external_stylesheets = [dbc.themes.COSMO, dbc.icons.BOOTSTRAP]
app_title = "YT Findex"

app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = app_title
