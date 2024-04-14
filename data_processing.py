import pandas as pd
import base64
import io

def load_data(encoded_content, content_type):
    decoded = base64.b64decode(encoded_content)
    if 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' in content_type:
        df = pd.read_excel(io.BytesIO(decoded))
        return df
    else:
        raise ValueError("Unsupported file format.")

def preprocess_data(df):
    df.dropna(how='all', axis=1, inplace=True)  # Remove all empty columns
    df.fillna(method='ffill', inplace=True)     # Forward fill to handle missing values

    # Convert columns to categorical or numeric as appropriate
    categorical_cols = ['Sexe?', 'Situation familiale?', 'âge ?', 'Quel est votre profession ?', 'Quel est votre niveau d\'éducation ?', 'Quelle est votre ville de résidence ?']
    for col in categorical_cols:
        if col in df.columns:
            df[col] = df[col].astype('category')

    # Mapping income to categories
    if 'Quel est votre revenu net mensuel ( en dinars tunisien) / ou de votre ménage ?' in df.columns:
        income_mapping = {
            'Entre 200 DT et 400 DT': '200-400',
            'Entre 1000 DT et 1400 DT': '1000-1400',
            'Entre 1400 DT et 1800 DT': '1400-1800',
            'Entre 800 DT et 1000 DT': '800-1000'
        }
        df['Quel est votre revenu net mensuel ( en dinars tunisien) / ou de votre ménage ?'] = df['Quel est votre revenu net mensuel ( en dinars tunisien) / ou de votre ménage ?'].map(income_mapping).astype('category')
    
    return df
