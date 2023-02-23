from dashboard.index import app 
from dash.dependencies import Input, Output

from db.conn_init import mydb
from secret_keys import DB_VIDEOS_COLLECTION

from dash import dash_table
import pandas as pd
from datetime import datetime


@app.callback(Output('random_record', 'children'),
            [Input('interval_db', 'n_intervals')])
def populate_random_record(n_intervals):
    collection =  mydb[DB_VIDEOS_COLLECTION]
    df = pd.DataFrame(list(collection.find({})))
    # Remove generated id
    df = df.iloc[:, 1:]
    df = df[['uploader', 'title', 'duration', 'upload_date']]
    df.rename(columns={'duration':'duration (sec)'}, inplace=True)
    df['upload_date'] = df['upload_date'].apply(lambda x: datetime.strptime(x,"%Y%m%d").date())

    return[dash_table.DataTable(
        id='my-table',
          columns=[{'id': x, 'name': x, 'presentation': 'markdown'} if x in ['uploader', 'title'] else {'id': x, 'name': x} for x in df.columns],
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
