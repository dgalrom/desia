import numpy as np

# a) Array del 0 al 9
array_z = np.arange(10)

# b) Array 3x4 de ceros
array_y = np.zeros((3, 4))

# c) Array 2x5 de unos
array_x = np.ones((2, 5))

# d) Matriz identidad 4x4
array_d = np.eye(4)

# e) Explorar propiedades de cada array
arrays = {'Z': array_z, 'Y': array_y, 'X': array_x, 'D': array_d}

for nombre, arr in arrays.items():
    print(arr)
    print(f"Forma: {arr.shape}")
    print(f"Dimensiones: {arr.ndim}")
    print(f"Tipo de dato: {arr.dtype}\n")
