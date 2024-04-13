import plotly.express as px

def create_figure(df):
    if 'X' in df.columns and 'Y' in df.columns:
        return px.scatter(df, x='X', y='Y')
    else:
        return px.scatter(df, x=df.columns[0], y=df.columns[1] if len(df.columns) > 1 else df.columns[0])
