"""Ejercicio 1 - Capitales y países¶
Escribe un programa que almacene en un diccionario las capitales de varios países, se introducirán los datos con la
forma PAIS-CAPITAL. Esto debe ejecutarse indefinidamente hasta que el usuario introduzca "FIN INSERCIONES".
El programa debe permitir al usuario consultar la capital de un país introduciendo su nombre. Si el país no está
en el diccionario, el programa debe informar al usuario.
1. variables
2. bucle que lee y registra las entradas de pais-capital
3.pedir un país y mirar si existe en el diccionario"""


paises = {}
entradaej1 = input("Indica un valor de la forma ´Pais:Capital´ o escribe FIN INSERCIONES para finalizar").lower()

while entradaej1 != "FIN INSERCIONES".lower():
    pais = entradaej1.split("-")[0]
    capital = entradaej1.split("-")[1]
    paises[pais]= capital
    entradaej1 = input("Indica un valor de la forma ´Pais:Capital´ o escribe FIN INSERCIONES para finalizar").lower()

print(paises)

pais_usuario = input("Introduce el nombre del país que quieres consultar").lower()
if pais_usuario in paises:
    print(f"La capital de {pais_usuario} es {paises[pais_usuario]}")
else:
    print("No existe esa entrada en el diccionario o el formato no es el correcto.")