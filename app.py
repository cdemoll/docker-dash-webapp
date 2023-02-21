# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
from dash.dependencies import Input, Output, State
from dash import dash_table
import dash_bootstrap_components as dbc
import plotly.express as px
from plotly.subplots import make_subplots
import pandas as pd
from pymongo import MongoClient
from secret_keys import *

# Connect to remote MongoDB database
client = MongoClient(f"mongodb+srv://{DB_USER}:{DB_PASSWORD}@cluster0.yvr1zwc.mongodb.net/?retryWrites=true&w=majority",ssl=True, tlsAllowInvalidCertificates=True)

mydb = client[DB_NAME]

collection = mydb[DB_VIDEOS_COLLECTION]


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

# # Create subplots: use 'domain' type for Pie subplot
# fig2 = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], 
#                     subplot_titles=['Sentiment split', 'Weighted Sentiment split'])

# fig2.add_trace(go.Pie(labels=edited_result['Sentiment'].unique().tolist(),
#                      values=edited_result['Sentiment'].value_counts(sort=False)),
#               1,1)

# fig2.add_trace(go.Pie(labels=edited_result['Sentiment'].values,
#                      values=edited_result['Sentiment_value'].values),
#               1,2)
# fig2.update_layout(width=1200)




app.layout = html.Div(children=[
    html.H1(children='Youtube Financial Sentiment Index'),


    html.Div(children='''
        Scalpex Index but further'''),


    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(id='random_record',children=[]),
    dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0)
])

@app.callback(Output('random_record', 'children'),
            [Input('interval_db', 'n_intervals')])
def populate_random_record(n_intervals):
    print(n_intervals)
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
            markdown_options={"html": True}
        )]

if __name__ == '__main__':
    app.run_server(debug=True)