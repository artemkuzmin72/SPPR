import pandas as pd
import numpy as np

data = {
    'Phone': ['Iphone 17', 'Samsung S25', 'XIAOMI 15'],
    'Price': [130000, 70000, 130000],
    'Battery': [80, 62, 85],
    'Perfomance': [8, 4, 10],
    'weight': [2.9, 3.5, 4.2],
    'diagonal': [5.5, 4.6, 6.0]
}

weights = {
    'Price': 0.2,
    'Battery': 0.3,
    'Perfomance': 0.3,
    'weight': 0.1,
    'diagonal': 0.1
}

df = pd.DataFrame(data)

df_norm = df.copy()

df_norm['Price_norm'] = (df['Price'].max() - df['Price']) / (df['Price'].max() - df['Price'].min())
df_norm['Battery_norm'] = (df['Battery'] - df['Battery'].min()) / (df['Battery'].max() - df['Battery'].min())
df_norm['Perfomance_norm'] = (df['Perfomance'] - df['Perfomance'].min()) / (df['Perfomance'].max() - df['Perfomance'].min())
df_norm['weight_norm'] = (df['weight'].max() - df['weight']) / (df['weight'].max() - df['weight'].min())
df_norm['diagonal_norm'] = (df['diagonal'] - df['diagonal'].min()) / (df['diagonal'].max() - df['diagonal'].min())

features = df_norm[['Price_norm', 'Battery_norm', 'Perfomance_norm', 'weight_norm', 'diagonal_norm']].values

w = np.array([weights['Price'], weights['Battery'], weights['Perfomance'], weights['weight'], weights['diagonal']])

df_norm['Score'] = features.dot(w)

print(df_norm[['Phone', 'Score']])
