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

"""Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en 
una lista y los muestre por pantalla ordenados de menor a mayor."""

loteria = []
for i in range(6):
    loteria.append(int(input("Introduce un número ganador: ")))
loteria.sort()
print("Los números ganadores son " + str(loteria))

"""Ejercicio 5
Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden 
inverso separados por comas."""

ten = [1,2,3,4,5,6,7,8,9,10]
ten.reverse()
for num in ten:
    print(num, end=",")

"""Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, 
Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura y elimine de 
la lista las asignaturas aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el 
usuario tiene que repetir."""


materias = ["Mate", "Física", "Química", "Historia", "Lengua"]
notas = []
for materia in materias:
    nota = float(input(f"¿Qué no ta has sacado en {materia}?"))
    notas.append(nota)

for i in range(len(notas) - 1, -1, -1):
    if notas[i] >= 5:
        materias.remove(materias[i])


if materias:
    print("Debes recuperar: " + ", ".join(materias))
else:
    print("¡Has aprobado todas las materias!")



