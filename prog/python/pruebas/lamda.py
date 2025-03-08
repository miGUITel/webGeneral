potencia = lambda x,y : x**y # Tu código aquí
print(potencia(2, 3))  # Debe imprimir: 8

par_o_impar = lambda x: "par" if x%2 == 0 else "impar"# Tu código aquí
print(par_o_impar(7))  # Debe imprimir: "Impar"

palabras = ["banana", "kiwi", "manzana", "uva"]
palabras_ordenadas = lambda x: sorted(x, key=len) # Tu código aquí
print(palabras_ordenadas(palabras))  # Debe imprimir: ['uva', 'kiwi', 'banana', 'manzana']

numeros = [5, 12, 3, 20, 8, 15]
mayores_10 = filter(lambda x: x if x > 10 else None, numeros)# Tu código aquí
print(list(mayores_10))  # Debe imprimir: [12, 20, 15]

from functools import reduce

numeros = [2, 4, 6, 8]
suma_total = reduce((lambda x,y: x+y),numeros)# Tu código aquí
print(suma_total)  # Debe imprimir: 20

# invertir = lambda x : (for i in range(len(x)) : x[len(x)-i-1])# Tu código aquí
# print(invertir("Python"))  # Debe imprimir: "nohtyP"

def invertir(x):
    y = ""
    for i in range (len(x)):
        y = y + x[len(x)-i-1]
    return y
print(invertir("Python"))