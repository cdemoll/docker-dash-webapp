from dashboard.index import app 
from dash.dependencies import Input, Output

from plotly.subplots import make_subplots
import plotly.graph_objects as go

from db.conn_init import mydb
from secret_keys import DB_GRAPH_COLLECTION

import pandas as pd


@app.callback(Output('current-week-pie', 'figure'),
            [Input('interval_db', 'n_intervals')])
def populateCPie(n_intervals):
    cPie_coll = mydb[DB_GRAPH_COLLECTION]
    df = pd.DataFrame(list(cPie_coll.find({})))
    # Remove generated id
    df = df.iloc[:, 1:]

    fig = make_subplots(rows=1, cols=2, specs=[[{'type':'domain'}, {'type':'domain'}]], 
                    subplot_titles=['Sentiment split', 'Weighted Sentiment split'])

    fig.add_trace(go.Pie(labels=df['Sentiment'].unique().tolist(),
                        values=df['Sentiment'].value_counts(sort=False)),
                1,1)

    fig.add_trace(go.Pie(labels=df['Sentiment'].values,
                        values=df['Sentiment_value'].values),
                1,2)

    return fig
