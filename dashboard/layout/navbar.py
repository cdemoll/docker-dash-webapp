from dashboard.index import dbc
from dashboard.content import html
from dashboard.index import app

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src=app.get_asset_url('plotly-logomark.png'), height="30px")),
                        dbc.Col(dbc.NavbarBrand("Youtube Financial Sentiment Index", className="ms-2")),
                    ],
                    align="center",
                    class_name="g-0",
                ),
                href="http://127.0.0.1:8050/",
                style={"textDecoration": "none"},
            ),
            dbc.Row([
                dbc.Col(
                    dbc.Nav([
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-github"), href="https://github.com/cdemoll/docker-dash-webapp", external_link=True)),
                        dbc.NavItem(dbc.NavLink(html.I(className="bi bi-linkedin"), href="https://www.linkedin.com/in/cl%C3%A9ment-demolliere/", external_link=True)),
                    ])
                )],
                style={'color':'white'}
            ),
            dbc.NavbarToggler(id="navbar-toggler", n_clicks=0),
            dbc.Collapse(
                id="navbar-collapse",
                is_open=False,
                navbar=True,
            ),
        ],
        fluid = True
    ),
    color="dark",
    dark=True,
)
