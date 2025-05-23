"""Ejercicio 1
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química,
Historia y Lengua) en una lista y la muestre por pantalla."""

asignaturas = ["Matemáticas","Física","Química","Historia","Lengua"]
print(asignaturas)

"""Ejercicio 2
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde 
<asignatura> es cada una de las asignaturas de la lista."""

asignaturas2 = ["Matemáticas","Física","Química","Historia","Lengua"]
print(f"Yo estudio {asignaturas2[3]}")

"""Para que me lo marque con todas las asignaturas el siguiente código"""

for asignatura in asignaturas2:
    print(f"Yo estudio {asignatura}")

"""Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después 
las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des 
las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario."""

materias = ["CSS", "HTML", "Python", "Java", "JavaScript"]
notas = []
for materia in materias:
    nota = input(f"¿Qué no ta has sacado en {materia}?")
    notas.append(nota)
for i in range(len(materias)):
    print(f"En {materias[i]} has sacado {notas[i]}")

"""Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden 
inverso separados por comas."""