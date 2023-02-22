from dashboard.index import app 
from dash.dependencies import Input, Output
import plotly.express as px

from db.conn_init import mydb
from secret_keys import DB_GRAPH_COLLECTION

import pandas as pd


@app.callback(Output('current-week-bar', 'figure'),
            [Input('interval_db', 'n_intervals')])
def populateCPie(n_intervals):
   cBar_coll = mydb[DB_GRAPH_COLLECTION]

   df = pd.DataFrame(list(cBar_coll.find({})))
   # Remove generated id
   df = df.iloc[:, 1:]

   fig = px.bar(df, x='Sentiment', y='Sentiment_value',
               hover_data=['Sentiment_value', 'Text'], color='Sentiment_value',
               height=400, width=1200)
   return fig