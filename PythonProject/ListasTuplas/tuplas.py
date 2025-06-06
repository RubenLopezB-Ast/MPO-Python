alumnos = {
    "alumno1": {"nombre": "Juan", "nota":7},
    "alumno2": {"nombre": "Laura", "nota":9}
}

print(alumnos)
print(alumnos["alumno1"])
print(alumnos["alumno1"]["nombre"])

for alumno in alumnos.values():
    for clave in alumno:
        print(f"Clave: {clave}: Valor{alumno[clave]}")



inventario = {
    "manzanas": 10,
    "naranjas": 5,
    "plátanos": 7,
}

for fruta, cantidad in inventario.items():
    print(f"Tengo {cantidad} {fruta}")

mi_tupla_ejemplo = (1,2,3)
print(mi_tupla_ejemplo)

persona = ("Ana", 30, "Valencia")
nombre, edad, ciudad = persona

print(nombre)

