import plotly.express as px
import pandas as pd

def create_figures(df):
    figures = []

    # Histogramas para variáveis demográficas
    demographic_cols = ['âge ?', 'Sexe?', 'Situation familiale?', 'Quel est votre profession ?', 'Quel est votre niveau d\'éducation ?']
    for col in demographic_cols:
        if col in df.columns:
            fig_hist = px.histogram(df, x=col, title=f'Histogram of {col}', color=col)
            figures.append(fig_hist)

    # Gráficos de barras para renda
    if 'Quel est votre revenu net mensuel ( en dinars tunisien) / ou de votre ménage ?' in df.columns:
        fig_bar = px.bar(df, x='Quel est votre revenu net mensuel ( en dinars tunisien) / ou de votre ménage ?', title='Distribution of Income')
        figures.append(fig_bar)

    return figures
