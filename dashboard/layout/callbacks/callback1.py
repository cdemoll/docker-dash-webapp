from dashboard.index import app 
from dash.dependencies import Input, Output, State

from db.conn_init import mydb
from secret_keys import DB_GRAPH_COLLECTION, DB_VIDEOS_COLLECTION

from dash import dash_table
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import pandas as pd

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