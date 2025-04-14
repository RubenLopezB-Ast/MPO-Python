"""Reto 2 abril - Calendario
Enunciado
Tu misión es simple, soldado: crear un calendario que muestre todos los meses del año y sus semanas de forma clara y
organizada. Nada de efectos especiales ni complicaciones innecesarias, solo un buen código que haga el trabajo.
Crea un programa que:

Itere los meses del año
Itere las semanas del mes
PISTA: Bucle for anidad.
Ejemplo
Enero Semana 1 Semana 2 Semana 3 …"""

meses = ["Enero","Febrero","Marzo","Abril","Mayo","Junio","Julio","Agosto","Septiembre","Octubre","Noviembre","Diciembre"]

for mes in meses:
    dias = 0
    print(mes)
    if mes in ["Enero","Marzo","Julio","Agosto","Octubre","Diciembre"]:
        dias =31
    elif mes in ["Abril", "Junio", "Septiembre", "Noviembre"]:
        dias = 30
    else:
        dias = 28

        for i in range(1,dias+1):
            print(i, end="\t")
            if i % 7 == 0:
                print()
