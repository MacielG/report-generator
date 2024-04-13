from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

def analyze_data(df):
    numeric_df = df.select_dtypes(include=['number'])
    if numeric_df.empty:
        return ["No numeric data available for PCA."]
    scaler = StandardScaler()
    pca = PCA(n_components=min(len(numeric_df.columns), 2))
    pca.fit(scaler.fit_transform(numeric_df))
    return [f"Explained variance ratio: {var:.2f}" for var in pca.explained_variance_ratio_]
