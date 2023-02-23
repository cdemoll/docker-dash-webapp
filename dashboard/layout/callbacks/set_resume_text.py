from dashboard.index import app 
from dash.dependencies import Input, Output
from dashboard.content import html
from db.conn_init import mydb
from secret_keys import DB_VIDEOS_COLLECTION

import pandas as pd


@app.callback(Output('output-resume-text', 'children'),
            [Input('interval_db', 'n_intervals')])
def populateCPie(n_intervals):
   collection =  mydb[DB_VIDEOS_COLLECTION]
   df = pd.DataFrame(list(collection.find({})))
   # Remove generated id
   df = df.iloc[:, 1:]

   nb_videos = len(df)
   nb_tot_hours = round(df.duration.sum()/3600)

   # return "By running our financial sentiment analysis on" + '<b>'+  f"{nb_videos}" + '</b>' +  f"videos, we spared you {nb_tot_hours} hours </b> of watchtime."
   return html.P(
         [
            "By running our financial sentiment analysis on ",
            html.B(f"{nb_videos} videos "),
            "we spared you ",
            html.B(f"{nb_tot_hours} hours "),
            "of watchtime."
         ])
   