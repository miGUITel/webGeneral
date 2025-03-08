celsius = [0, 10, 20, 30, 40]
fahrenheit = map(lambda x : x*9/5 + 32, celsius)        # Tu código aquí
print(list(fahrenheit))  # Debe imprimir: [32.0, 50.0, 68.0, 86.0, 104.0]

palabras = ["Python", "lambda", "map", "función"]
longitudes = map(lambda x : len(x), palabras)     # Tu código aquí
print(list(longitudes))  # Debe imprimir: [6, 6, 3, 7]

numeros = [1, 2, 3, 4, 5]
cadenas = map(lambda x : str(x), numeros)      # Tu código aquí
print(list(cadenas))  # Debe imprimir: ["1", "2", "3", "4", "5"]

numeros = [2, 3, 4, 5]
cubos = map(lambda x : x*x*x, numeros)
print(list(cubos))

nombres = ["ana", "pedro", "juan", "lucia"]
mayusculas = map(lambda x : x.upper(), nombres)
print(list(mayusculas))