import pandas as pd

datos_sucios = {
    'nombre': ['Ana García', ' Pedro López', 'María Ruiz', 'Ana García'],
    'edad': [25, None, 30, 25],
    'email': ['ana@mail.com', 'pedro@mail.com', None, 'ana@mail.com'],
    'ciudad': ['Madrid', 'barcelona', 'VALENCIA', 'Madrid']
}
df = pd.DataFrame(datos_sucios)

print(df, "\n")

df['nombre'] = df['nombre'].str.strip()
df['edad'] = df['edad'].fillna(df['edad'].mean())
df = df.dropna(subset=['email'])
df['ciudad'] = df['ciudad'].str.title()
df = df.drop_duplicates()

print(df)