from dashboard.index import app 
from dash.dependencies import Input, Output
from dashboard.layout import data_charts
from dashboard.layout import data_table

'''
   Definition of our 'router'
'''
@app.callback(Output('page-content', 'children'),
            [Input('url', 'pathname')])
def update_page_layout(pathname):
   if pathname == '/charts':
      return data_charts.layout
   if pathname == '/explore-data':
      return data_table.layout
   else:
      return data_charts.layout
