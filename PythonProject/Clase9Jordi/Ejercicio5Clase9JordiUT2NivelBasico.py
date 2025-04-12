"""Ejercicio 5¶
Escribe un programa que pida el nombre de un día de la semana y muestre si es "laborable" o "fin de semana"."""

dia = input("¿Que día de la semana quieres comprobar? ").upper()
if dia in ["SABADO", "DOMINGO"]:
    print(f"El {dia} es fin de semana.")
elif dia in ["LUNES","MARTES","MIERCOLES","JUEVES","VIERNES"]:
    print(f"El {dia} es laborable.")
else:
    print("Eso no es un día de la semana.")