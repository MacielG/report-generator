from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import pandas as pd

def analyze_data(df):
    results = {}
    # Análise Descritiva
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        results['desc_stats'] = "No numeric data available for statistics."
    else:
        desc_stats = numeric_df.describe()
        results['desc_stats'] = desc_stats.to_html()

    # PCA para Redução de Dimensionalidade
    if not numeric_df.empty:
        scaler = StandardScaler()
        pca = PCA(n_components=min(len(numeric_df.columns), 2))
        pca.fit(scaler.fit_transform(numeric_df))
        results['pca'] = f"Explained variance ratio: {pca.explained_variance_ratio_}"
    else:
        results['pca'] = "No numeric data available for PCA."

    return results
