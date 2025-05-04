"""Crear dos variables utilizando los objetos fecha
En la primera se representa la fecha (día, mes, año) actual.
En la segunda se representa la fecha de nacimiento.

Calcular cuántos años han transcurrido entre ambas fechas y muestra su resultado de maneras diferentes
Día, mes y año.
Hora, minuto y segundo.
Día de año.
Día de la semana.
Nombre del mes.
"""

from datetime import datetime

fecha_actual = datetime.now()
entra = input("Pon tu fecha de nacimiento del siguiente modo dd/mm/aaaa: ")

fecha_nacimiento = datetime.strptime(entra, "%d/%m/%Y")

diferencia = fecha_actual - fecha_nacimiento
years = diferencia.days // 365

print(f"La fecha actual es: {fecha_actual.strftime("%d/%m/%Y")}")
print(f"La fecha de nacimiento es: {fecha_nacimiento.strftime("%d/%m/%Y")}")
print(f"Tienes {years} años")

dias = diferencia.days
meses = dias // 30
print(f"Tienes, dias: {dias} Meses: {meses} Años: {years} aproximadamente")

segundos = diferencia.total_seconds()
horas = int(segundos//3600)
minutos = int((segundos % 3600) //60)
segundos_res = int(segundos % 60)
print(f"Tienes, Horas: {horas}, Minutos: {minutos}, Segundos: {segundos_res}")

print("Dia del año en el que naciste: ", fecha_nacimiento.timetuple().tm_yday)

dias_semana = ["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]
print("Día de la semana en el que nacieste: ", dias_semana[fecha_nacimiento.weekday()])

meses_year = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre", "Diciembre"]
print("Mes de nacimiento: ", meses_year[fecha_nacimiento.month-1])

