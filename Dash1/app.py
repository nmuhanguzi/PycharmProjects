import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.express as px
import dash_auth

app = dash.Dash()
username_pairs = [
    ['Nimrod','1234'],
]
auth = dash_auth.BasicAuth(
    app,
    username_pairs
)
df = px.data.iris()
fig = px.scatter(df, x = "sepal_width", y = "sepal_length")
app.layout = html.Div(children = [
    html.H1('My first Dash app'),
    html.H2('Sub-heading'),

    dcc.Dropdown(
        options = [
            {'label': 'New York City', 'value': 'NYC' },
            {'label': 'Montreal', 'value': 'MTL' },
            {'label': 'San Francisco', 'value': 'SF' },
        ],
        value ='MTL'
    ),
    dcc.Graph(figure = fig),
]
)
if __name__ == '__main__':
    app.run_server()