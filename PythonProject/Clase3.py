#1. Longitud de una cadena
import random

nombre = "Rubén López"
print("Longitud del nombre: ", len (nombre))

#2. Convertir texto a mayúsculas y minúsculas
#upper
print("Esto sale en mayusculas: ", nombre.upper())
#lower
print("ESTO ES EN MINUSCULAS: ", nombre.lower())

print("Esto sale en mayusculas: ".upper())
#lower
print("ESTO ES EN MINUSCULAS: ".lower())

#3. Slicing
print("Primeros 3 caracteres: ", nombre[:3])
print("Ultimos 3 caracteres: ", nombre[-4:])

#4 Reemplazar palabras de una cadena
frase = "Me gusta Java"
print("Cambio la palabra: ", frase.replace("Java","Phyton"))
print(frase)

#5. Verificar si una cadena existe en otra
print("Python" in frase)
print("Java" in frase)

#6. Unir varias palabras en una cadena
palabras = ["Hola", "Mundo", "en", "Python"]
print("Frase completa con join: ", " ".join(palabras)) # Vas metiendo espacios segun se quiera

#7. Split
oracion = "Python es divertido"
palabritas = oracion.split()
print(palabritas)

#8. Redondear un número decimal
numero = 3.1416
print("Mi número redondeado es: ", round(numero,3))

#9. Formateo de número decimales
precio = 19.99
print("Precio con dos decimales: {:.2f}".format(precio))

#10. Obtener el valor ASCII de un carácter
print("Esto es el código ASCII de 'A': ", ord('A'))

#11. Elevar al cuadrado y al cubo
numero_al_cuadrado = 5
print("5 al cuadrado es: ", numero_al_cuadrado ** 2)

numero_al_cubo = 2
print("2 al cuadrado es: ", numero_al_cubo ** 3)

#12. Raiz cuadrada
print("Raiz cuadrada de 25 es: ", 25 ** 0.5)

import math
numerito = 100
raiz = math.sqrt(numerito)
print("Raiz cuadrada de 100: ", raiz )

#13. Divisioes enteras y resto
print("División normal: ", 10/3)
print("División entera: ", 10//3)
print("Resto: ", 10%3)

#14. Generar un numero aleatorio
print("Número aleatorio ente 1 y 10: ", random.randint(1,10))

#15. Convertir numeros a cadenas y viceversa.
numerajo = 300
texto = str(numerajo)
print("Convertido a texto, soy: ", texto)

print (type(texto))

#Lo siguiente da error
"""cadena = "200"
numerajo = int(cadena)
print("Convertido a numero soy: ", numerajo)
print(numerajo+texto)"""

#16. Redondear hacia arriba
print("Redondeo ahia arriba 3.2: ", math.ceil(3.6))
print("Redondero hacia abajo del numero 3.2", math.floor(3.2))

#17. Convertir una lista en un conjunto, es decir, eliminar duplicados.
numeroides = [1, 2, 3, 3, 4, 5, 5]
sin_duplicados = set(numeroides)
print("La lista de numeroides sin duplicados es: ", sin_duplicados)

#18. Repetir una cadena
print("Money!"*3)

#19. El tipo de dato
dato = 3.14
print("El tipo de dato es: ", type(dato))

#20. Combinar cadenas y variables en un print
name = "Rubén"
edad = 32
print(f"Hola, soy {name} y tengo {edad} años.")

