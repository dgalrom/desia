import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

# a) Primer elemento
primerelemento = arr[0]

# b) Último elemento
ultimoelemento = arr[-1]

# c) Elementos del índice 2 al 5
d2al5 = arr[2:5]

# d) Desde índice 5 hasta el final
d5final = arr[5:]

# e) Desde el inicio hasta índice 4
iniciohasta4 = arr[:4]

# f) Elementos en posiciones pares
pares = arr[::2]

# g) Array invertido
invertido = arr[::-1]
