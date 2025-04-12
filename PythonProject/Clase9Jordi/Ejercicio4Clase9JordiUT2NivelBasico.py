"""Ejercicio 4¶
Escribe un programa que pida una nota (0-10) y muestre:
"Suspenso" si es menor de 5
"Aprobado" si es entre 5 y 6
"Notable" si es entre 7 y 8
"Sobresaliente" si es 9 o 10"""

nota = float(input("Introduce tu nota del uno al diez junto con dos deimales: "))

if nota < 5:
    print(f"Tu nota es {nota} estas suspenso.")
elif nota < 7 and nota >= 5:
    print(f" Tu nota es {nota} estas aprobado.")
elif nota < 9 and nota >= 7:
    print(f" Tu nota es {nota} tienes un notable.")
elif nota < 11 and nota >= 9:
    print(f"Tu nota es {nota} tienes un sobresaliente.")
else:
    print(f"Tu nota no es correcta {nota} no está dentro de los parámetros. Vuelve a repetir el proceso correctamente.")

#Otra manera de hacerlo.

nota1 = float(input("Introduce una nota (0-10): "))
if nota1 < 5:
    print("Suspenso")
elif 5 <= nota1 < 7:
    print("Aprobado")
elif 7 <= nota1 < 9:
    print("Notable")
elif 9 <= nota1 <= 10:
    print("Sobresaliente")
else:
    print("Nota no válida.")
