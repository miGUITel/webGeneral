numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filter(lambda x: x % 2 == 0, numeros)
print(list(pares))  # [2, 4, 6, 8, 10]


nombres = ["María", "Carlos", "Miguel", "Ana", "mario", "Lucía"]
empiezan_con_m = filter(lambda x: x[0].lower() == 'm', nombres)
print(list(empiezan_con_m))  # ["María", "Miguel", "mario"]


numeros = [10, 55, 30, 80, 45, 90, 20]
mayores_50 = filter(lambda x : x>50, numeros) # Tu código aquí
print(list(mayores_50))  # Debe imprimir: [55, 80, 90]

palabras = ["hola", "examen", "perro", "gato", "elefante", "casa"]
contienen_e = filter(lambda x: 'e' in x, palabras)  #### 'caracter' in "cadena" -> bool ####
print(list(contienen_e))  # ["examen", "perro", "elefante"]
