import dash
from dash import dcc, html, dash_table, callback, Output, Input
import dash_bootstrap_components as dbc
from data_processing import load_data, preprocess_data
from visualizations import create_figure
from analytics import analyze_data

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={'width': '100%', 'height': '60px', 'lineHeight': '60px',
               'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
               'textAlign': 'center', 'margin': '10px'},
        multiple=False
    ),
    html.Div(id='output-data-upload'),
    html.Div(id='analytics-output')
])

@app.callback(
    Output('output-data-upload', 'children'),
    Input('upload-data', 'contents')
)
def update_output(contents):
    if contents is None:
        return html.Div()
    df = load_data(contents)
    df = preprocess_data(df)
    figure = create_figure(df)
    return dcc.Graph(figure=figure)

@app.callback(
    Output('analytics-output', 'children'),
    Input('upload-data', 'contents')
)
def update_analytics(contents):
    if contents is None:
        return html.Div()
    df = load_data(contents)
    df = preprocess_data(df)
    results = analyze_data(df)
    return html.Div([html.P(result) for result in results])

if __name__ == '__main__':
    app.run_server(debug=True)
