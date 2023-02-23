from dashboard.content import html, dcc

resume_text = html.Div([
   html.Br(),
   html.Div(id = 'output-resume-text'),
   dcc.Interval(id='interval_db', interval=86400000 * 7, n_intervals= 0)
])
