#Ejercicio 5 - Puede entrar en el servidor de Discord?¶
#Escribe un programa que pida un rol y una academia de estudios, si el rol es "alumno" y la academia es "Prometeo"
#el programa debe darle acceso al servidor de Discord oficial y al de los alumnos, donde se critica a los profes.
#Si el rol es "profesor" y la academia es "Prometeo" el programa debe darle acceso al servidor de Discord oficial,
#pero no al de los alumnos. En cualquier otro caso, el programa debe imprimir "No tienes acceso al servidor de Discord".

rol = input("Dime rol del usuario: ").lower()


if rol == "estudiante":
    print("Acceso ofcial a Chill y Oficial")
elif rol == "trabajo":
    print("Acceso al desde profes")
else:
    print("Decidete")

academia = input("¿En que academia  estudias/trabajas? ").lower()
if academia == "estudias":
    print("Acceso al Discord Oficial Estudiantes")
elif academia == "trabajas":
    print("Acceso al Discod de profes")
else:
    print("Aceso a los servidores")