import pandas as pd
import io
import base64

def load_data(contents):
    content_type, content_string = contents.split(',')
    decoded = base64.b64decode(content_string)
    if 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
        return pd.read_excel(io.BytesIO(decoded))
    else:
        raise ValueError("Unsupported file format.")

def preprocess_data(df):
    df = df.dropna(how='all', axis=1).dropna(how='all', axis=0)
    df = df.apply(lambda x: pd.to_numeric(x, errors='ignore'))
    return df.fillna(df.median(numeric_only=True))
