## Lambda
```py
potencia = lambda x,y : x**y # Tu código aquí
print(potencia(2, 3))  # Debe imprimir: 8
```

## if condensado
```py
resultado = "Menor que 3" if x < 3 else "Mayor o igual a 3"

par_o_impar = lambda x: "par" if x%2 == 0 else "impar"# Tu código aquí
print(par_o_impar(7))  # Debe imprimir: "Impar"
```

## sorted
```py
palabras = ["banana", "kiwi", "manzana", "uva"]
palabras_ordenadas = lambda x: sorted(x, key=len) # Tu código aquí
print(palabras_ordenadas(palabras))  # Debe imprimir: ['uva', 'kiwi', 'banana', 'manzana']
```

## filter
```py
numeros = [5, 12, 3, 20, 8, 15]
mayores_10 = filter(lambda x: x if x > 10 else None, numeros)# Tu código aquí
print(list(mayores_10))  # Debe imprimir: [12, 20, 15]
```

