inventario = {}


def agregar_producto(nombre, precio, cantidad):
    inventario[nombre] = {'precio': precio, 'cantidad': cantidad}


def actualizar_precio(nombre, nuevo_precio):
    if nombre in inventario:
        inventario[nombre]['precio'] = nuevo_precio


def actualizar_stock(nombre, nueva_cantidad):
    if nombre in inventario:
        inventario[nombre]['cantidad'] = nueva_cantidad


def eliminar_producto(nombre):
    inventario.pop(nombre, None)


def mostrar_inventario():
    ordenados = sorted(inventario.items(), key=lambda x: x[1]['precio'])
    for nombre, datos in ordenados:
        print(f"{nombre}: ${datos['precio']} - Stock: {datos['cantidad']}")


def valor_total_inventario():
    total = 0
    for datos in inventario.values():
        total += datos['precio'] * datos['cantidad']
    return round(total, 2)


agregar_producto("Teclado", 45.50, 15)
agregar_producto("Monitor", 199.99, 8)

print(valor_total_inventario())
mostrar_inventario()
