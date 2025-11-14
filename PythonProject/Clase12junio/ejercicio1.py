import os

from Clase4.Clase4 import nombre


def listar_archivos():
    archivos =os.listdir(".")
    return archivos

def existe_archivo(archivo):
    return os.path.exists(archivo)

def crear_archivo(archivo):
    return open(nombre, "x")

def cre

def main():
    opcion = -1
    while opcion != 5:
        print("###MENÚ###")
        print("1. Listar archivos")
        print("2. Verificar si exisgte el archivo")
        print("3. Crea archivo")
        print("4. Crear directorio")
        print("5. Salir")

        if opcion == 1:
            print(listar_archivos())
        elif opcion == 2:
            archivo = input("Qué archivo quieres comprobar?\n")
            if existe_archivo(archivo):
                print("El archivo exíste")
            else:
                print("El arcivo no exíste")
        elif opcion == 3:
            nombre = input("Que nombre quires ponerle al archivo?\n")
            if existe_archivo(nombre):
                print("Este archivo ya exite")
            else:
                archivo = crear_archivo(nombre)
                print()
        elif opcion == 4:
            pass
        elif opcion == 5:
            print("Opción no válida.")


if os.name == "main":
    main()