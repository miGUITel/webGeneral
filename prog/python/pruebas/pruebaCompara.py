def contar_frecuencia_palabras(cadena):
    resultado = {}
    palabras = cadena.split()
    for palabra in palabras:
        if palabra in resultado:
            resultado[palabra] += 1
        else:
            resultado[palabra] = 1
    return resultado

texto = "el perro ladra y el gato maulla el perro corre"
salida = contar_frecuencia_palabras(texto)
print(salida)