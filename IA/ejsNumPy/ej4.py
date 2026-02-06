import numpy as np

ventas = np.array([
    [1000, 1200, 1100, 1300],
    [900, 1000, 950, 1050],
    [1500, 1600, 1550, 1700]
])

# a) Shape
print(ventas.shape)

# b) Ventas Tienda 2
ventas_tienda_2 = ventas[1]
print(ventas_tienda_2)

# c) Ventas Trimestre 3
ventas_trimestre_3 = ventas[:, 2]
print(ventas_trimestre_3)

# d) Total por tienda (suma por filas)
total_por_tienda = ventas.sum(axis=1)
print(total_por_tienda)

# e) Total por trimestre (suma por columnas)
total_por_trimestre = ventas.sum(axis=0)
print(total_por_trimestre)

# f) Media por tienda
media_por_tienda = ventas.mean(axis=1)
print(media_por_tienda)

# g) Tienda con mayores ventas
tienda_top = np.argmax(total_por_tienda)
print(total_por_tienda)

# h) Trimestre con menores ventas
trimestre_peor = np.argmin(total_por_trimestre)
print(trimestre_peor)
