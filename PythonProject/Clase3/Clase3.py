""""#1. Longitud de una cadena
import random
from collections.abc import Reversible
from dataclasses import replace
"""
"""nombre = "Rubén López"
print("Longitud del nombre: ", len (nombre))

"""
#2. Convertir texto a mayúsculas y minúsculas
#upper"""

"""print("Esto sale en mayusculas: ", nombre.upper())
#lower
print("ESTO ES EN MINUSCULAS: ", nombre.lower())

print("Esto sale en mayusculas: ".upper())
#lower
print("ESTO ES EN MINUSCULAS: ".lower())

"""
#3. Slicing
"""
print("Primeros 3 caracteres: ", nombre[:3])
print("Ultimos 3 caracteres: ", nombre[-4:])

"""
#4 Reemplazar palabras de una cadena
"""

frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java","Phyton"))
print(frase)

"""
#5. Verificar si una cadena existe en otra
"""

print("Python" in frase)
print("Java" in frase)

"""
#6. Unir varias palabras en una cadena
"""

palabras = ["Hola", "Mundo", "en", "Python"]
print("Frase completa con join: ", " ".join(palabras)) # Vas metiendo espacios segun se quiera

"""
#7. Split
"""

oracion = "Python es divertido"
palabritas = oracion.split()
print(palabritas)

"""
#8. Redondear un número decimal
"""

numero = 3.1416
print("Mi número redondeado es: ", round(numero,3))

"""
#9. Formateo de número decimales
"""

precio = 19.99
print("Precio con dos decimales: {:.2f}".format(precio))

"""
#10. Obtener el valor ASCII de un carácter
"""

print("Esto es el código ASCII de 'A': ", ord('A'))

"""
#11. Elevar al cuadrado y al cubo
"""

numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado ** 2)

numero_al_cubo = 2
print("2 al cuadrado es: ", numero_al_cubo ** 3)

"""
#12. Raiz cuadrada
"""
print("Raiz cuadrada de 25 es: ", 25 ** 0.5)

import math
numerito = 100
raiz = math.sqrt(numerito)
print("Raiz cuadrada de 100: ", raiz )

"""
#13. Divisioes enteras y resto
"""

print("División normal: ", 10/3)
print("División entera: ", 10//3)
print("Resto: ", 10%3)

"""
#14. Generar un numero aleatorio
"""

#print("Número aleatorio entre 1 y 10: ") random.randint(1,10)

"""
#15. Convertir numeros a cadenas y viceversa.
"""
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)

print (type(texto))
"""
#Lo siguiente da error
"""cadena = "200"
numerajo = int(cadena)
print("Convertido a numero soy: ", numerajo)
print(numerajo+texto

#16. Redondear hacia arriba
"""
"""
print("Redondeo ahia arriba 3.2: ", math.ceil(3.6))
print("Redondero hacia abajo del numero 3.2", math.floor(3.2))
"""
"""
#17. Convertir una lista en un conjunto, es decir, eliminar duplicados.
"""

"""numeroides = [1, 2, 3, 3, 4, 5, 5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", sin_duplicados)

"""
#18. Repetir una cadena
"""

print("Money!"*3)

"""
#19. El tipo de dato
"""

dato = 3.14
print("El tipo de dato es: ", type(dato))

"""
#20. Combinar cadenas y variables en un print
"""

name = "Rubén"
edad = 32
print(f"Hola, soy {name} y tengo {edad} años.")

"""
"""
Ejercicios
1 Generador de nombres de usuario
Pide al usuario su nombre y apellido.
Genera un nombre de usuario en minúsculas, sin espacios.
Añade un número aleatorio al final.
Muestra el nombre de usuario generado.
"""
"""
import random

print("Introduce nombre:")
name = input()
print("Introduce tu primer apellido:")
surname1 = input()
print("Introduce tu segundo apellido: ")
surname2 = input()


nombre_e=name.replace("é","e")
nombre_a=nombre_e.replace("á","a")
nombre_i=nombre_a.replace("í","i")
nombre_o=nombre_i.replace("ó","o")
nombre_u_final=nombre_o.replace("ú","u")

apellido1_e=surname1.replace("é","e")
apellido1_a=apellido1_e.replace("á","a")
apellido1_i=apellido1_a.replace("í","i")
apellido1_o=apellido1_i.replace("ó","o")
apellido1_u_final=apellido1_o.replace("ú","u")

apellido2_e=surname2.replace("é","e")
apellido2_a=apellido2_e.replace("á","a")
apellido2_i=apellido2_a.replace("í","i")
apellido2_o=apellido2_i.replace("ó","o")
apellido2_u_final=apellido2_o.replace("ú","u")

nombre=nombre_u_final.lower()
apellido1=apellido1_u_final.lower()
apellido2=apellido2_u_final.lower()

nombreNoEspacio=nombre.replace(" ","")
apellido1noEspacio=apellido1.replace(" ","")
apellido2noEspacio=apellido2.replace(" ","")

numero_aleatorio = random.randint(1,999)


print(f"Su USUARIO es: {nombreNoEspacio}{apellido2noEspacio}{apellido2noEspacio}{numero_aleatorio}")



"""
""""
2️⃣ Analizador de frases
Pide al usuario que ingrese una frase.
Muestra la cantidad de caracteres de la frase.
Indica si la frase contiene la palabra "Python".
Convierte la frase a mayúsculas.
Muestra la frase invertida.
"""
"""

print("Introduce una frase: ")
frase = input()

caracter_number = len(frase)
print(f"Tu frase contiene {caracter_number} caracteres.")

if "Python" in frase:
    print("Esta frase contiene la palabra Python.")
else:
    print("Python no parece estar en esta frase.")

    fraseMayusculas=frase.upper()
    print(fraseMayusculas)

    frase_sep=frase.split()
    frase_sep.reverse()
    print(" ".join(frase_sep))
"""
"""3️⃣ Cálculo de descuentos
Pide al usuario el precio de un producto.
Aplica un 15% de descuento.
Muestra el precio final con dos decimales.
Muestra el precio redondeado hacia arriba.
"""
"""
print("¿Cuanto cuestan estos pantalones?")
precio_pantalones  = int(input())
float = precio_pantalones
porcentaje_descuento = 15
descuento = precio_pantalones * (porcentaje_descuento / 100)
precio_oferta_pantalones = precio_pantalones - descuento
print(f"Estos pantalones que antes costababan {precio_pantalones}€  ahora cuestan tan solo {precio_oferta_pantalones}€")

precio_oferta_pantalones_dos_dec = print("%2f." % precio_oferta_pantalones) # añadimos dos 0
precio_oferta_pantalones_dos_dec = round(precio_oferta_pantalones,2) # acotamos a dos decimales
print(f"Precio de la oferta con dos decimales: {precio_oferta_pantalones_dos_dec}")

precio_redondeo = math.ceil(precio_oferta_pantalones_dos_dec)
print(f"El precio de {precio_oferta_pantalones_dos_dec} lo redondeo hacia arriba hasta {precio_redondeo}")

"""
"""
4️⃣ Generador de etiquetas de productos
Pide el nombre de un producto y su precio.
Convierte el nombre del producto a mayúsculas.
Muestra el precio con dos decimales.
Genera un código basado en el valor ASCII de la primera letra del producto.
"""
"""
def productos ():
    producto = input("Dime nombre del producto: ")
    price = int(input("Pon el precio"))
    producto_mayusculas = producto.upper()
    precio_oper1= price - 1.5
    precio_float = precio_oper1 + 1.5
    precio_dos_dec = "{:.2f}".format(precio_float)
    codigo = ord(producto[0])

    print(f"Producto: {producto_mayusculas} Precio: {precio_dos_dec} € Codigo: {codigo}")
productos()

"""
"""5️⃣ Conversión de tipos y manipulación de listas
Pide al usuario una lista de números separados por comas.
Convierte cada número a entero.
Elimina los números repetidos.
Muestra la lista ordenada sin duplicados.
"""
"""
print("Escribe una lista de numeros separados por comas #,#: ")
lista = input().split(",")
lista_ent = [int(x) for x in lista]
lista_sin_duplicados = set(lista_ent)
lista_ordenada = sorted(lista_sin_duplicados)
print(f"Ahí tienes tu lista ordenada y sin duplicados: {lista_ordenada}")

"""
"""
6️⃣ Creación de mensajes personalizados
Pide al usuario su nombre, edad y ciudad.
Muestra un mensaje con toda la información.
Si la edad es menor de 18, redondea hacia arriba hasta la mayoría de edad. """
"""
print("¿Cual es tu nombre ?")
nombre_ejer6 = input()

print("¿Cual es tu edad?")
edad_ejer6 = int(input())

print("¿En que ciudad vives?")
ciudad_ejer6 = input()

print(f"Tus datos son los siguientes nombre:{nombre_ejer6}, edad:{edad_ejer6} y vives en {ciudad_ejer6}.")
if edad_ejer6 < 18:
    edad_ejer6 = 18
    print(f"En esta frase tu edad pasa a ser:{edad_ejer6}")
"""
"""7️⃣ Generador de contraseñas aleatorias
Pide al usuario su nombre.
Genera una contraseña segura con la primera letra en mayúscula, un número aleatorio y un símbolo especial.
Muestra la contraseña generada.
"""
"""
print("Vamos a proporcionarte tu contraseña personal, ¿Cual es tu  nombre?")
nombre_contra = input().upper()
especial_caracter =["|","@","#","$","&",]
especial = random.choice(especial_caracter)
aleatorio_numero = random.randint(1,999)
contra_segura = (f"{nombre_contra[0]}{aleatorio_numero}{especial}")
print(f"Esta es tu contraseña segura: {contra_segura}")

"""
"""8️⃣ Verificación de nombres en listas
Pide al usuario su nombre.
Verifica si su nombre está en una lista de invitados predefinida.
Si está en la lista, muestra su posición.
"""
""""
list = ["ROBERTO", "ELADIO", "SATURNINO", "LORETO", "MACARENA"]

print("Dime tu nombre: ")
nome_in = input().upper()


if nome_in in list:
    posicion_lista = (list.index(nome_in))
    print(f"El nombre {nome_in} esta en la lista en la posición {posicion_lista}")
else:
    print("El nombre no aparece en la lista.")
"""
"""9️⃣ Manipulación de nombres
Pide al usuario su nombre y apellido.
Convierte el nombre a minúsculas y el apellido a mayúsculas.
Genera un alias combinando las primeras 3 letras del nombre y del apellido.
Muestra el alias generado.
"""
"""
print("Dime tu nombre: ")
usuario_nombre = input().lower()

print("Ahora intruduce tu primer apellido: ")
usuario_apellido = input().upper()

usunom_e=usuario_nombre.replace("é","e")
usunom_a=usunom_e.replace("á","a")
usunom_i=usunom_a.replace("í","i")
usunom_o=usunom_i.replace("ó","o")
usunom_u_final=usunom_o.replace("ú","u")

usuape1_e=usuario_apellido.replace("É","E")
usuape1_a=usuape1_e.replace("Á","A")
usuape1_i=usuape1_a.replace("Í","I")
usuape1_o=usuape1_i.replace("Ó","O")
usuape1_u_final=usuape1_o.replace("Ú","U")

print(f"Alias: {usunom_u_final[:3]}{usuape1_u_final[:3]}")
"""
"""🔟 Formatear y mostrar datos matemáticos
Pide al usuario un número decimal.
Muestra el número redondeado a dos decimales.
Calcula y muestra su cuadrado.
Calcula y muestra su raíz cuadrada.
"""
""""
print("Escribe un número decimal: ")

numero_decimal = float(input())

print(f"Numero redondeado a dos decimales: {round(numero_decimal,2)}")

print(f"El cuadrado de:  {round(numero_decimal,2)} es:  {(round(numero_decimal,2))**2}")

print(f"La raiz cuadrada de: {round(numero_decimal,2)} es: {(round(numero_decimal,2))**0.5}")
"""