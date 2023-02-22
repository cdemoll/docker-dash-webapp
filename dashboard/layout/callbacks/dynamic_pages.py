from dashboard.index import app 
from dash.dependencies import Input, Output
from dashboard.layout import data_charts



@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def update_page_layout(pathname):
   if pathname == '/charts':
      return data_charts.layout
   else:
      return "404"
