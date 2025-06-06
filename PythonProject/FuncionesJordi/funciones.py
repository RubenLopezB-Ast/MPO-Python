print("Bienvenida")

def operaciones (a, b):
    suma = a + b
    resta = a - b
    return suma, resta

x, y = operaciones(10, 4)
print("Suma: ", x)
print("Resta: ", y)

"""Verificar si un número es primo"""

def es_primo(numero):
    """Un numero es primo si solo es divisible entre uno y si mismo"""
    for i in range(2, numero):
        if numero%i == 0:
            return False
    return True

"""Icrementar cada elemento en un lista"""

def incrementa_lista(lista, numero):
    for i in range(len(lista)):
        lista[i] += numero
    return lista

numeros = input("Introduce una lista de numeros separados por coma\n").split()
lista = [int(num) for num in numeros]