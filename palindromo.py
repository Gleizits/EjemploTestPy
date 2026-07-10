import time

def es_palindromo(cadena):
    cadena = cadena.lower()
    punto_medio = len(cadena)

    for i in range(punto_medio):
        indice_negativo = -(i + 1)

        if cadena[i] != cadena[indice_negativo]:
            return False
        else:
            return True

def funcion_sin_usar():
    return time.time()
