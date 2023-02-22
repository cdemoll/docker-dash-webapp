
from dashboard.content import html, dcc

layout = html.Div([
   html.H1("Datatable"),
   html.Div(id='random_record',children=[]),

   dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0)
])
