# Usa un bucle for para sumar solo los números pares del 1 al 20
# Imprime el resultado final
suma=0
for i in range(1,20):
    if i%2==0:
        suma+=i
print(suma)