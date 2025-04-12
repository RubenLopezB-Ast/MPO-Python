"""Ejercicio 10¶
Escribe un programa que, dados dos números enteros, imprima su división decimal, si división entera y su resto.
El segundo número no puede ser cero."""

numero_n = int(input("Escribe un número: "))
numero_o = int(input("Escribe otro número"))

print(f"Dando el número {numero_n} como dividendo y el número {numero_o} como divisor. El resultado de la división decimal"
      f"es {numero_n/numero_o} el de la división entera es {numero_n//numero_o} y el resto es {numero_n%numero_o} .")