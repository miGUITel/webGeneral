import string
signos = string.punctuation
print(signos)
texto = "Hola, ¿cómo estás? Hola mundo."
texto = texto.lower()

def contar_frecuencia_palabras(cadena):
    for char in signos:
        if (char in cadena):
            cadena = cadena.replace(char, "")
    if ("¿" in cadena):
            cadena = cadena.replace("¿", "")
    lista = cadena.split()
    diccionario = {}
    for palabra in lista:
        if palabra in diccionario:
            diccionario[palabra] += 1
        else:
            diccionario[palabra] = 1
    return diccionario

resultado = contar_frecuencia_palabras(texto)
print(resultado)
# Salida esperada: {'hola': 2, 'cómo': 1, 'estás': 1, 'mundo': 1}