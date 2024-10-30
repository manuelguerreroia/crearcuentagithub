import string

frase = input("Ingresa una frase o párrafo")

texto_procesado = frase.lower()
texto_procesado = ''.join(char for char in texto_procesado if char not in string.punctuation)

palabras = texto_procesado.split()

frecuencia_palabras = {}

for palabra in palabras:
    if palabra in frecuencia_palabras:
        frecuencia_palabras[palabra] += 1
    else:
        frecuencia_palabras[palabra] = 1

for palabra, frecuencia in sorted(frecuencia_palabras.items()):
    print(f"{palabra}: {frecuencia}")