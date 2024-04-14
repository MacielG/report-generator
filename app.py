import dash
from dash import dcc, html, Output, Input, State
import dash_bootstrap_components as dbc
from data_processing import load_data, preprocess_data
from visualizations import create_figures

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([
    dcc.Upload(
        id='upload-data',
        children=html.Div(['Drag and Drop or ', html.A('Select Files')]),
        style={
            'width': '100%', 'height': '60px', 'lineHeight': '60px',
            'borderWidth': '1px', 'borderStyle': 'dashed', 'borderRadius': '5px',
            'textAlign': 'center', 'margin': '10px'
        },
        multiple=False  # Allows only one file to be uploaded
    ),
    html.Div(id='status-indicators', style={'margin': '20px'}),
    html.Div(id='graph-container')  # This will hold the graphs
])

@app.callback(
    [Output('graph-container', 'children'), Output('status-indicators', 'children')],
    [Input('upload-data', 'contents')],
    [State('upload-data', 'filename'), State('upload-data', 'last_modified')]
)
def update_output(contents, filename, last_modified):
    if contents is not None:
        content_type, content_string = contents.split(';base64,')
        if 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
            df = load_data(content_string, content_type)
            df = preprocess_data(df)
            figures = create_figures(df)
            graphs = [dcc.Graph(figure=fig) for fig in figures]
            return graphs, f'Loaded {len(figures)} graphs from the uploaded data.'
        else:
            return [], 'Unsupported file format.'
    else:
        return [], 'No data uploaded yet.'

if __name__ == '__main__':
    app.run_server(debug=True)
