# Ejercicios - Tipos básicos, Números, Cadenas y Booleanos
# Parte 1: Booleanos y Operaciones con Números
# Ejercicio 1: Evaluación de Expresiones Booleanas
# 📌 Objetivo: Evaluar expresiones numéricas que devuelvan valores booleanos.
# Crea variables con expresiones matemáticas y convierte los resultados en booleanos.
# Muestra el valor booleano de cada una.
exp1 = (10 > 5) # True
exp2 = (3*3 == 10) # False
exp3 = (15%2 == 0) # False (15 no es múltiplo de 2)
exp4 = (0 == False) # True (0 se considera False en Python)
exp5 = bool(100) # True (cualquier número distinto de 0 es True)
exp6 = bool(0) # False (0 es False)
exp7 = bool(-5) # True números negativos también son True)

#Muestra de los valores booleanos
print("expresión 1: ", exp1)
print("expresión 2: ", exp2)
print("expresión 3: ", exp3)
print("expresión 4: ", exp4)
print("expresión 5: ", exp5)
print("expresión 6: ", exp6)
print("expresión 7: ", exp7)

#
# Ejercicio 2: Operaciones Matemáticas con Booleanos
# 📌 Objetivo: Descubrir cómo Python trata los valores True y False en operaciones matemáticas.
# Suma True + True y False + True.
# Multiplica True * 10 y False * 50.
# Muestra los resultados y explica qué ocurre.
#
exp8 = (True + True) # En Python True es 1 así que el resultado es 2
exp9 = (False + True) # En Python True es 1 y False es 0 así que el resultado es 1
exp10 = ((True + True) + (False + True))
exp11 = (True*10)
exp12 = (False*50)

#Imprimo como se comprortan las expresiones:

print("expresión 8: ", exp8)
print("expresión 9: ", exp9)
print("expresión 10: ", exp10)
print("expresión 11: ", exp11)
print("expresión 12: ", exp12)

# Ejercicio 3: Conversión entre Tipos Básicos
# 📌 Objetivo: Convertir entre tipos de datos (números, cadenas y booleanos).
# Convierte un número en cadena y muéstralo.
# Convierte una cadena numérica en un entero.
# Convierte un booleano en un número.
#
#Número a cadena
num = 42
num_str = str(num)
print("Número como cadena:", num_str, "=", type(num_str))

#Cadena numérica a entero
cadena_num = "130"
num_entero = int(cadena_num)
print("Cadena convertida en entero:", num_entero, "=", type(num_entero))

#Conversión de un booleano a número
bool_true = True
bool_false = False
num_true = int(bool_true)
num_false = int(bool_false)
print("Booleano True como número:", num_true)
print("Booleno False como número:", num_false)
# Ejercicio 4: Propiedades de las Cadenas
# 📌 Objetivo: Manipular cadenas y explorar sus propiedades.
# Crea una cadena con tu nombre.
# Muestra el primer y último carácter.
# Muestra la longitud de la cadena.
# Convierte la cadena a mayúsculas y minúsculas.

string = "Rubén"
print(string[0])
print(string[4])
print(len(string))
print(string.lower())
print(string.upper())
#
# Ejercicio 5: Operaciones con Cadenas y Números
# 📌 Objetivo: Realizar operaciones matemáticas con cadenas y números.
# Concatenar cadenas con números usando str().
# Multiplicar una cadena para repetirla varias veces.

numero = 22
string = "Prueba de concatenar con el numero "
print(string + str(numero))
print(string*5)
#
# Ejercicio 6: Operaciones con Caracteres y Códigos ASCII
# 📌 Objetivo: Explorar caracteres y su representación en ASCII.
# Obtén el código ASCII de la letra 'A'.
# Convierte un número en su carácter ASCII correspondiente.

print(ord("A"))

print(chr(622))
#
# Ejercicio 7: Evaluación de Expresiones Lógicas
# 📌 Objetivo: Trabajar con operadores lógicos (and, or, not).
# Evalúa expresiones lógicas combinando números y operadores lógicos.
# Muestra los resultados.

num1 = 10
num2 = 5
num3 = 0

exp13 = (num1 > num2) and (num2 >num3)
exp14 = (num1 < num2) or (num2 == 0)
exp15 = not (num1 == 10)
exp16 = (num2 != 5) and (num3 < num1)
exp17 = (num1 >=10) or (num3 > num2)

print("Expresión 13:", exp13)
print("Expresión 14:", exp14)
print("Expresion 15:", exp15)
print("Expresión 16:", exp16)
print("Expresión 17:", exp17)