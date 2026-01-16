texto = input("Texto: ")

texto_minus = texto.lower()

palabras = [p for p in texto_minus.split() if p]

num_palabras = len(palabras)
print(f"Número de palabras: {num_palabras}")

palabra_mas_larga = max(palabras, key=len)
print(
    f"Palabra más larga: {palabra_mas_larga} ({len(palabra_mas_larga)} caracteres)")

vocales = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

for letra in texto_minus:
    if letra in vocales:
        vocales[letra] += 1

print(f"Vocales: a={texto_minus.count('a')}, e={texto_minus.count('e')}, i={texto_minus.count('i')}, o={texto_minus.count('o')}, u={texto_minus.count('u')}")
top3 = sorted(palabras, key=len, reverse=True)[:3]

for i, palabra in enumerate(top3, 1):
    print(f"  {i}. {palabra} ({len(palabra)} caracteres)")
