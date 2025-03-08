#1
print (3 + 2 == 5)
#2
lista = [5, 6, 2, 1]
ordenada = sorted(lista)
print(ordenada)
#2
eleva2 = lambda x : x * x
print(eleva2(2))
#2 solución
tuplas = [(1, 3), (2, 1), (3, 5)]
ordenado = sorted(tuplas, key=lambda x: x[0])
print(ordenado)  # [(2, 1), (1, 3), (3, 5)]
print ('Hola {} Mi nombre es Miguel'.format("Carlos"))
# 6
from functools import reduce
a = lambda b: reduce(lambda x, y: x * y, range(1, b+1)) 
numero = 4
print('%d' %( a(numero)))
# 6 error
# x = str(3) 
# x+=1
# print(x)

#6
z = 12 
y=5
z //= y 
print(z)

x = -7
y = 3

resultado_int = int(x / y)
resultado_floor = x // y

print("int(x / y)  ->", resultado_int) #trunca
print("x // y      ->", resultado_floor) #redondea

vocales = ('a', 'e', 'i', 'o') 
v_set = frozenset(vocales) 
v_set.add('u')
print(v_set)

