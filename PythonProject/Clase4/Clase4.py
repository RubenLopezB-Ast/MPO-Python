"""Ejercicio 1: Operaciones numéricas complejas
Define cinco variables numéricas distintas (int, float, complex) y realiza diversas operaciones matemáticas (potenciación,
división entera, módulo). Imprime los resultados formateados en una cadena clara y descriptiva.

numero1, numero2, numero3, numero4, numero5 = 10, 3, 2.5, 7.1, 4+2j
resultado = (f"Potencia: {numero1**numero2}, Division entera: {numero1//numero2},"
             f"Modulo: {numero1%numero2}, Multiplicacion: {numero3*numero4}, Complejo: {numero5}")
print(resultado)


Ejercicio 2: Combinación de cadenas y números
Define dos variables numéricas (int, float) y tres cadenas diferentes. Genera una nueva cadena combinando texto con el 
resultado de operaciones aritméticas entre estas variables. Usa conversión explícita (str()) para insertar valores numéricos 
en la cadena final.

numero_int, numero_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado: ", "la suma es ", "y la division es "
resultado = cadena1 + "" +cadena2 + "" + cadena3 +"" + str(numero_int/numero_float)
print(resultado)
 

Ejercicio 3: Manipulación avanzada de cadenas
Crea una cadena larga que contenga espacios en blanco al inicio, final, y en medio. Realiza varias operaciones encadenadas
como eliminar espacios extremos, convertir todo a mayúsculas, y dividir la cadena en varias subcadenas usando un separador
específico.

cadena = " Esto es una cadena para manipular "
nueva_cadena= cadena.strip().upper().split()
print(nueva_cadena)


Ejercicio 4: Índices y subcadenas
Define una cadena extensa (mínimo 50 caracteres). Obtén varias subcadenas usando la indexación por rangos (slicing)
y genera una nueva cadena combinando estas subcadenas en orden inverso. Imprime la nueva cadena resultante.

cadena_extensa = "Python es un super lenguaje que me re encanta"
subcadena = cadena_extensa[0:6] + "" + cadena_extensa[11:20]
resultado = subcadena [::-1]
print(resultado)


Ejercicio 5: Formato y conversión numérica
Define variables numéricas (entero, flotante, complejo). Crea una cadena con formato avanzado (f-strings) que muestre
estos números con precisión definida (dos decimales, notación científica, etc.). Evita concatenar directamente números
y texto.


entero, flotante, complejo = 12, 332.312423, 5+3j
formato = (f"Entero: {entero}, Flotante: {flotante:.2f},"
           f"Notacion cientifica: {flotante:.2e}, Complejo: {complejo}")
print(formato)

Ejercicio 6: Operaciones combinadas entre números y cadenas
Define dos variables numéricas enteras y dos cadenas. Realiza cálculos matemáticos diversos y genera una cadena
formateada que explique cada operación (sumas, restas, multiplicaciones, módulo) claramente utilizando métodos de cadenas.


numero_a, numero_b = 15, 4
cadena_a, cadena_b = "La multiplicación da: " , "y el resto es: "
resultado = f"{cadena_a}{numero_a*numero_b}"
print(resultado)


Ejercicio 7: Cálculo del área y perímetro
Define variables numéricas que representen dimensiones (largo, ancho, radio, altura). Calcula el área y perímetro de
distintas figuras geométricas (rectángulo, círculo, triángulo rectángulo) y presenta todos los resultados claramente en
una sola cadena formateada usando conversiones explícitas.

largo, ancho, radio, altura = 10, 5, 3, 4
area_rectangulo = largo*ancho
perimetro_rectangulo = 2*(largo+ancho)
area_circulo = 3.14 * radio **2
perimetro_circulo = 2*3.14*radio
area_triangulo = (largo*altura)/2
resultado =(f"Area de un rectangulo: {area_rectangulo},"
f"perimetro del rectangulo {perimetro_rectangulo}, "
f"\nCirculo: Area:{area_circulo} y perimetro: {perimetro_circulo},"
f"\nTriangulo: Area: {area_triangulo}")
print(resultado)

Ejercicio 8: Análisis de texto complejo
Define una cadena extensa que represente un párrafo completo. Utilizando únicamente métodos de cadenas y funciones
integradas (len, upper, split), obtén el número total de caracteres, palabras y el resultado de transformar el texto
completamente a mayúsculas, presentándolo claramente en una cadena nueva.

parrafo = "Soy un ejemplo de parrafo largo de narices para ocupar todo el espacio que quiero si si eso es soy tan largo aquí estoy"
caracteres = len(parrafo)
palabroides = len(parrafo.split())
mayusculas = parrafo.upper()
resultado = (f"Total de palabras: {caracteres}, "
             f"Total de caracteres: {palabroides},"
             f"Parrafo en mayusculas: {mayusculas},")
print(resultado)


Ejercicio 9: Fórmula cuadrática
Dados tres números que representan los coeficientes (a, b, c) de una ecuación cuadrática, resuelve la fórmula cuadrática
para obtener las raíces reales o complejas. Imprime claramente en una cadena formateada los coeficientes y las raíces
encontradas.

numero_a, numero_b, numero_c = 12, 45, 56

nuero_b_cuadrado = numero_b*2
parte_superior = (-numero_b)+(nuero_b_cuadrado-(4*numero_a*numero_c))
parte_inferior = 2*numero_a
resultado = parte_superior / parte_inferior

print(resultado)


Ejercicio 10: Manejo y transformación de datos personales
Crea variables para representar datos personales (nombre, edad, peso, altura). Calcula el índice de masa corporal (IMC)
sin usar bucles, y presenta un resumen detallado y formateado de todos estos datos personales, incluyendo el IMC con dos
decimales.
Estos ejercicios te permitirán profundizar en la teoría básica de números y cadenas en Python de manera práctica y sin
recurrir a estructuras repetitivas.
"""
nombre = "Rubén"
edad = 41
peso = 83
altura = 1.81

IMC =  peso / (altura*altura)

print(f"\nTabla :"
      f"\n{nombre}"
      f"\n{edad} años"
      f"\n{peso} Kilogramos"
      f"\n{altura} Metros"
      f"\n Con los datos anteriores su IMC es: {IMC}")


"""
RESPUESTAS

Ejercicio 1
num1, num2, num3, num4, num5 = 10, 3, 2.5, 7.2, 4+2j
resultado = f"Potencia: {num1 ** num2}, División entera: {num1 // num2}, Módulo: {num1 % num2}, Multiplicación: {num3 * num4}, Complejo: {num5}"
print(resultado)

Ejercicio 2
num_int, num_float = 8, 3.5
cadena1, cadena2, cadena3 = "Resultado:", "La suma es", "y la división es"
resultado = cadena1 + " " + cadena2 + " " + str(num_int + num_float) + " " + cadena3 + " " + str(num_int / num_float)
print(resultado)

Ejercicio 3
cadena = "   Este es un ejemplo de cadena para manipular    "
nueva_cadena = cadena.strip().upper().split(" ")
print(nueva_cadena)

Ejercicio 4
cadena_extensa = "Python es un lenguaje potente, versátil y muy fácil de aprender."
subcadena = cadena_extensa[0:6] + " " + cadena_extensa[11:20] + " " + cadena_extensa[-9:]
resultado = subcadena[::-1]
print(resultado)

Ejercicio 5
entero, flotante, complejo = 12, 345.6789, 5+3j
formato = f"Entero: {entero}, Flotante: {flotante:.2f}, Notación científica: {flotante:.2e}, Complejo: {complejo}"
print(formato)

Ejercicio 6
num_a, num_b = 15, 4
cad_a, cad_b = "La multiplicación da", "y el resto es"
resultado = f"{cad_a} {num_a * num_b}, {cad_b} {num_a % num_b}"
print(resultado)


Ejercicio 7
largo, ancho, radio, altura = 10, 5, 3, 4
area_rectangulo = largo * ancho
perimetro_rectangulo = 2 * (largo + ancho)
area_circulo = 3.14159 * radio ** 2
perimetro_circulo = 2 * 3.14159 * radio
area_triangulo = (largo * altura) / 2
resultado = f"Rectángulo: área {area_rectangulo}, perímetro {perimetro_rectangulo}; Círculo: área {area_circulo:.2f}, perímetro {perimetro_circulo:.2f}; Triángulo: área {area_triangulo}"
print(resultado)

Ejercicio 8
parrafo = "Este es un párrafo de ejemplo que será usado para probar métodos de cadenas en Python."
caracteres = len(parrafo)
palabras = len(parrafo.split())
mayusculas = parrafo.upper()
resultado = f"Total caracteres: {caracteres}, total palabras: {palabras}, texto en mayúsculas: {mayusculas}"
print(resultado)

Ejercicio 9
a, b, c = 1, -3, 2
discriminante = (b ** 2 - 4 * a * c) ** 0.5
raiz1 = (-b + discriminante) / (2 * a)
raiz2 = (-b - discriminante) / (2 * a)
resultado = f"Coeficientes: a={a}, b={b}, c={c}. Raíces: {raiz1}, {raiz2}"
print(resultado)

Ejercicio 10
nombre, edad, peso, altura = "Mario", 30, 70, 1.75
imc = peso / altura ** 2
resultado = f"Nombre: {nombre}, Edad: {edad}, Peso: {peso} kg, Altura: {altura} m, IMC: {imc:.2f}"
print(resultado)

"""
