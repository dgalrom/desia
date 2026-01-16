def calcular_estadisticas(numeros):
    media = sum(numeros) / len(numeros)

    ordenados = sorted(numeros)
    n = len(numeros)
    if n % 2 == 0:
        mediana = (ordenados[n//2 - 1] + ordenados[n//2]) / 2
    else:
        mediana = ordenados[n//2]

    conteo = {}
    for num in numeros:
        conteo[num] = conteo.get(num, 0) + 1
    moda = max(conteo, key=conteo.get)

    rango = max(numeros) - min(numeros)

    suma_cuadrados = sum((x - media) ** 2 for x in numeros)
    varianza = suma_cuadrados / (len(numeros) - 1)

    return {
        'media': round(media, 2),
        'mediana': mediana,
        'moda': moda,
        'rango': rango,
        'varianza': round(varianza, 2)
    }


datos = [23, 45, 67, 45, 89, 12, 45, 34, 56, 78]
print(calcular_estadisticas(datos))
