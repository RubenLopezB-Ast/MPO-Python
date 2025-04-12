"""Ejercicio 6¶
Escribe un programa que pida al usuario un número entero e imprima:

Su doble
Su triple
Su mitad
Su cuadrado
Su raíz cuadrada"""
import math

numero_h = int(input("Díme un númro de sin decimales"))
h_doble = numero_h*2
h_triple = numero_h*3
h_mitad = numero_h/2
h_cuadrado = numero_h**2
h_raiz = math.sqrt(numero_h)

print(f"Dado el número {numero_h} su doble es {h_doble} su triple {h_triple} su mitad {h_mitad} su cuadrado {h_cuadrado} "
      f"y su raiz cuadrada {h_raiz} .")
