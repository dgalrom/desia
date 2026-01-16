import numpy as np

temperaturas = np.array([18, 22, 25, 19, 30, 15, 28, 23, 17, 31, 20, 26])

# a) Máscara > 25
mascara_gt_25 = temperaturas > 25
print(mascara_gt_25)

# b) Filtrar temperaturas > 25
filtradas = temperaturas[mascara_gt_25]
print(filtradas)

# c) Contar temperaturas > 25
contadas = np.sum(mascara_gt_25)

# d) Máscara entre 20 y 25
mascara_rango = (temperaturas >= 20) & (temperaturas <= 25)

# e) Reemplazar valores > 28 con 28
temp_limite = temperaturas.copy()
temp_limite[temp_limite > 28] = 28

# f) Clasificar temperaturas
condiciones = [
    (temperaturas < 20),
    (temperaturas >= 20) & (temperaturas <= 25),
    (temperaturas > 25)
]
categorias = ["Frío", "Templado", "Calor"]

clasificacion = np.select(condiciones, categorias)
print(clasificacion)
