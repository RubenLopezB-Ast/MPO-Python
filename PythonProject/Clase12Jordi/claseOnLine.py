"""Método Pop"""
from Clase9Jordi.Ejercicio7Clase9JordiUT2NivelBasico import resultado

mi_lista = [1,2,4,5,]

print(mi_lista.pop())

print(mi_lista)

"""Ejercicio 1
Escribe un progrma aque pida al usuario una lista de números enteros separados por comas y calcule todos los
elementos de la lista. El programa debe imprimir el resultado."""

lista_numeros = input("Escribe una lista de números separados por coma: ").split(",")
resultado = 0

for i in range(len(lista_numeros)):
    resultado += lista_numeros[i]
print(lista_numeros)

"""Ejercicio 2 - Contar elementos de una lista¶
Escribe un programa que pida al usuario una lista de palabras separadas por comas y cuente cuántas palabras 
hay en la  lista. El programa debe imprimir el resultado."""

print("La longitud de la lista es: ", len(input("Introduce una lita de palabra separadas por coma").split(",")))

"""Ejercicio 3 - Mayor y menor elemento de una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y encuentre el mayor y el 
menor elemento de la lista. El programa debe imprimir ambos resultados"""

lista2_numero = input("Introduce una lista de números separadas por comas").split(",")
lista2_numero = [int(num) for num in lista2_numero]
print(f"menor: {min(lista2_numero)} mayor: {max(lista2_numero)}")


"""Ejercicio 4 - Sumar dos listas de igual longitud¶
Escribe un programa que pida al usuario dos listas de números enteros separados por comas y sume los elementos 
de ambas listas. El programa debe imprimir la lista resultante. Si las listas no tienen la misma longitud, el 
programa debe imprimir un mensaje de error."""

lista_a = input("Introduce l primera lista de numeros separada por comas: ").split(",")
lista_b = input("Introduce l primera lista de numeros separada por comas: ").split(",")

if len(lista_a) != len(lista_b):
    print("La longitud es diferente")
else:
    suma_listas = []
    for i in range(len(lista_a)):
        suma_listas.append(int (lista_a[i])+int(lista_b[i]))

    print(suma_listas)

"""Ejercicio 5 - Invertir una lista¶
Escribe un programa que pida al usuario una lista de números enteros separados por comas y la invierta. El 
programa debe imprimir la lista invertida."""

lista_c = input("Introduce una lista de valores: ").split("")
lista_c.reverse()
print(lista_c)

"""Ejercicio 6 - Dias de la semana¶
Escribe un programa que reciba números hasta la introducción de un 0. Por cada número, suponiendo que el 1 
representa el lunes, el 2 el martes, etc., imprime el nombre del día correspondiente.

Ejemplo:


Ingrese un número (0 para salir): 1
Lunes
Ingrese un número (0 para salir): 3
Miércoles
Ingrese un número (0 para salir): 8
Lunes
Ingrese un número (0 para salir): 0"""
dias_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

while True:
    # Pedimos al usuario un número
    entrada = input("Ingrese un número (0 para salir): ")

    try:
        numero = int(entrada)

        if numero == 0:
            break
        else:
            # Usamos módulo 7 para ciclar entre los días (1 a 7)
            indice = (numero - 1) % 7
            print(dias_semana[indice])

    except ValueError:
        print("Por favor, ingrese un número válido.")