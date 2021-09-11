import dash
import dash_bootstrap_components as dbc
from dash import dcc, html
from dash.dependencies import Input, Output

external_stylesheets = [dbc.themes.DARKLY]
dash_app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app = dash_app.server

dash_app.layout = dbc.Container(
    children=[
        dbc.Row([
            html.H2('Dagbog')
        ]),
        dbc.Row([
            dbc.Col([
                dbc.Textarea(
                    id='text-area',
                    bs_size="lg",
                    placeholder="Write notes here.",
                    style={"height": 500},
                ),
            ], lg = 6),
            dbc.Col([
                dcc.Markdown(
                id='markdown-area')
            ])
        ])
    ]
)

@dash_app.callback(
    Output('markdown-area', 'children'),
    Input('text-area', 'value')
)
def populate_markdown(text):
    if text is None:
        text = ""
    return str(text)

if __name__ == '__main__':
    dash_app.run_server(debug=True)