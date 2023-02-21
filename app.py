# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash import dash_table
import plotly.express as px
import pandas as pd
from pymongo import MongoClient
from secret_keys import *

# Connect to remote MongoDB database
client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.yvr1zwc.mongodb.net/?retryWrites=true&w=majority",ssl=True, tlsAllowInvalidCertificates=True)

mydb = client[DB_NAME]

collection = mydb[DB_COLLECTION]


app = Dash(__name__)
server = app.server
# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(id='random_record',children=[]),
    dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),
    html.Div(children='''lsdajlfsad'''

    ),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

@app.callback(Output('random_record', 'children'),
            [Input('interval_db', 'n_intervals')])
def populate_random_record(n_intervals):
    print(n_intervals)
    df = pd.DataFrame(list(collection.find({"GenNum": 1}, limit = 5)))
    # Remove generated id
    df = df.iloc[:, 1:]
    print(df)

    return[dash_table.DataTable(
        id='my-table',
          columns=[{
                'name': x,
                'id': x,
            } for x in df.columns],
            data=df.to_dict('records'),
            editable=True,
            row_deletable=True,
            filter_action="native",
            filter_options={"case": "sensitive"},
            sort_action="native",  # give user capability to sort columns
            sort_mode="single",  # sort across 'multi' or 'single' columns
            page_current=0,  # page number that user is on
            page_size=6,  # number of rows visible per page
            style_cell={'textAlign': 'left', 'minWidth': '100px',
                        'width': '100px', 'maxWidth': '100px'},
        )]

if __name__ == '__main__':
    app.run_server(debug=True)