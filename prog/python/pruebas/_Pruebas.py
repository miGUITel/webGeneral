# La conjetura de Collatz indica que, dado un número cualquiera entero positivo mayor a 1, si le aplicamos repetidamente una simple transformación que consiste en:
# Si el número es par, se divide entre 2
# Si el número es impar, se multiplica por 3 y se suma 1

def collatz(numero):
    if (numero == 1):
        return 1
    elif (numero % 2 == 0):
        return collatz(numero / 2)
    else:
        return collatz(numero * 3 + 1)

prueba = 0
while (prueba <= 0):
    prueba = int(input(f"Dame un número entero mayor que 0: "))

resultado = collatz(prueba)

print(f"El resultado es {resultado}")