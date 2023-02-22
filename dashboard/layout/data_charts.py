from dashboard.content import html, dcc

layout = html.Div([
   html.H1("Charts"),

   dcc.Graph(
      id='current-week-pie'
   ),

   dcc.Graph(
      id='current-week-bar'
   ),

   dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0)
])