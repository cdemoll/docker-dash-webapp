# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.
from dashboard.content import app

server = app.server
if __name__ == '__main__':
    app.run_server(debug=True)