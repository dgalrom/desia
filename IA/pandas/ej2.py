import pandas as pd

df = pd.read_csv('../datasets/ejemplo_datos.csv')

df.info()

df.describe()

total_ventas = len(df)

precio_medio = df['precio'].mean()

producto_mas_caro = df.loc[df['precio'].idxmax(), 'producto']
precio_mas_caro = df['precio'].max()

ventas_madrid = df[df['ciudad'] == 'Madrid']

ventas_por_ciudad = df.groupby('ciudad')['precio'].sum()

ventas_por_ciudad_ordenado = df.groupby('ciudad')['precio'].sum().sort_values(ascending=False)