# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd
from pymongo import MongoClient
from secret_keys import *

#######################################SERVER#######################################
# Connect to remote MongoDB database
client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.yvr1zwc.mongodb.net/?retryWrites=true&w=majority",ssl=True, tlsAllowInvalidCertificates=True)
mydb = client[DB_NAME]
PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

#######################################COMPONENTS#######################################
navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=PLOTLY_LOGO, height="30px")),
                        dbc.Col(dbc.NavbarBrand("Youtube Financial Sentiment Index", className="ms-2")),
                    ],
                    align="center",
                    class_name="g-0",
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            dbc.Row([
                dbc.Col(
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/cdemoll/docker-dash-webapp", external_link=True)),
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/in/cl%C3%A9ment-demolliere/", external_link=True)),
                    ])
                )],
                style={'color':'white'}
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid = True
    ),
    color="dark",
    dark=True,
)

#######################################APP#######################################
app = Dash(__name__, external_stylesheets=[dbc.themes.COSMO, dbc.icons.BOOTSTRAP])
server = app.server

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

#######################################CALLBACKS#######################################
# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("navbar-toggler", "n_clicks")],
    [State("navbar-collapse", "is_open")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(Output('current-week-pie', 'figure'),
            [Input('interval_db', 'n_intervals')])
def populateCPie(n_intervals):
    print(n_intervals)
    cPie_coll = mydb[DB_GRAPH_COLLECTION]

    df = pd.DataFrame(list(cPie_coll.find({})))
    # Remove generated id
    df = df.iloc[:, 1:]
    print(df)

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], 
                    subplot_titles=['Sentiment split', 'Weighted Sentiment split'])

    fig.add_trace(go.Pie(labels=df['Sentiment'].unique().tolist(),
                        values=df['Sentiment'].value_counts(sort=False)),
                1,1)

    fig.add_trace(go.Pie(labels=df['Sentiment'].values,
                        values=df['Sentiment_value'].values),
                1,2)

    return fig


@app.callback(Output('random_record', 'children'),
            [Input('interval_db', 'n_intervals')])
def populate_random_record(n_intervals):
    print(n_intervals)
    collection =  mydb[DB_VIDEOS_COLLECTION]
    df = pd.DataFrame(list(collection.find({})))
    # Remove generated id
    df = df.iloc[:, 1:]
    print(df)

    return[dash_table.DataTable(
        id='my-table',
          columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x in ['channel', 'name'] else {'id': x, 'name': x} for x in df.columns],
            data=df.to_dict('records'),
            editable=False,
            row_deletable=False,
            fill_width=True,
            filter_action="native",
            filter_options={"case": "insensitive"},
            sort_action="native",  # give user capability to sort columns
            sort_mode="multi",  # sort across 'multi' or 'single' columns
            page_current=0,  # page number that user is on
            page_size=10,  # number of rows visible per page
            style_cell={'textAlign': 'center', 'minWidth': '100px',
                        'width': '100px', 'maxWidth': '100px',
                        'color': 'black'},
            style_header={
                'color': 'black'
            },
            style_data={
                'color': 'black', 'text-decoration': 'none'
            },
            markdown_options={"html": True},
            virtualization=False
        )]

if __name__ == '__main__':
    app.run_server(debug=True)