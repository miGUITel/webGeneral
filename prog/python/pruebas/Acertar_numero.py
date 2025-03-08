# Ejercicio 10 del cuestionario de POO
## Pendiente repetir usando búsqueda binaria en lugar de random

import random
numeros = list(range(1, 101))
limite_inferior = 1
limite_superior = 100
acertado = False
mentira = False
intentos = 0
intento = 0
elegido = int(input("Elije número 1-100: "))
print(f"Has elegido: {elegido}")

while (acertado == False and mentira == False):
    intentos += 1
    intento = random.randint(limite_inferior, limite_superior)#El ejercicio pide que uses la búsqueda binaria!!
    if (intento == elegido):
        acertado = True
    else:
        sugerencia = input(f"No he acertado. He probado con {intento}. ¿El número que has elegido es mayor o menor? Responde con mayor o menor, por favor." )
        if sugerencia == "mayor":
            limite_inferior = intento
        else:
            limite_superior = intento
        mentira = True if (sugerencia == "mayor" and elegido < intento) else False
        mentira = True if (sugerencia == "menor" and elegido > intento) else False

print(f"He acertado es {intento}, he necesitado {intentos} intentos") if (acertado) else print("Me has mentido")

def propuesta_chat(): # búsqueda binaria
    limite_inferior = 1
    limite_superior = 100
    acertado = False
    mentira = False
    intentos = 0

    elegido = int(input("Elije un número entre 1 y 100: "))
    print(f"Has elegido: {elegido}")

    while not acertado and not mentira:
        intentos += 1
        intento = (limite_inferior + limite_superior) // 2  # Búsqueda binaria

        if intento == elegido:
            acertado = True
        else:
            sugerencia = input(f"No he acertado. He probado con {intento}. ¿Tu número es mayor o menor? (Responde con 'mayor' o 'menor'): ").strip().lower()

            if sugerencia == "mayor":
                if elegido < intento:
                    mentira = True  # Se detecta trampa
                else:
                    limite_inferior = intento + 1
            elif sugerencia == "menor":
                if elegido > intento:
                    mentira = True  # Se detecta trampa
                else:
                    limite_superior = intento - 1
            else:
                print("Por favor, responde con 'mayor' o 'menor'.")

    if acertado:
        print(f"¡He acertado! Tu número era {intento}. Me tomó {intentos} intentos.")
    else:
        print("¡Me has mentido! La información no es coherente.")
