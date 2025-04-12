"""Ejercicio 8¶
Escribe un programa que pida el nombre de un mes y muestre cuántos días tiene (puedes simplificar febrero a 28 días siempre)."""

mes = input("Nombra un mes: ").upper()

if mes in ["ENERO", "MARZO", "MAYO", "JULIO", "AGOSTO", "OCTUBRE", "DICIEMBRE" ]:
    num_dias = 31
elif mes in ["ABRIL", "JUNIO", "SEPTIEMBRE", "NOVIEMBRE"]:
    num_dias = 30
elif mes == "FEBRERO":
    num_dias = 28
else:
    num_dias = "Error"

print(f"El mes de {mes} tiene {num_dias} . ")


#Otra opción:

mes = input("Introduce el nombre de un mes: ").lower()
if mes in ["enero", "marzo", "mayo", "julio", "agosto", "octubre", "diciembre"]:
    dias = 31
elif mes in ["abril", "junio", "septiembre", "noviembre"]:
    dias = 30
elif mes == "febrero":
    dias = 28
else:
    dias = "Mes no válido."

print(f"{mes.capitalize()} tiene {dias} días.")