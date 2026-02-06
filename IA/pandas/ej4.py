import pandas as pd

ventas = {
    'producto': ['Laptop', 'Mouse', 'Teclado', 'Monitor'],
    'precio_base': [800, 20, 45, 200],
    'cantidad': [1, 3, 2, 1]
}
df = pd.DataFrame(ventas)

print("ORIGINAL:")
print(df, "\n")

df['subtotal'] = df['precio_base'] * df['cantidad']
df['iva'] = df['subtotal'] * 0.21
df['total'] = df['subtotal'] + df['iva']

def categorizar_precio(precio):
    if precio < 50:
        return 'Económico'
    elif precio < 300:
        return 'Medio'
    else:
        return 'Premium'

df['categoria_precio'] = df['precio_base'].apply(categorizar_precio)

print("FINAL:")
print(df)