#Creame un diccionario
persona = {
    "nombre" : "Mario",
    "edad" : 32,
    "registrado" : True
}

print(persona)
#Accedeme a un valor por su clave
print(persona["edad"])

#Añadir una nueva clave-valor

persona["ciudad"] = "Burgos"
persona["Numero de hijos"] = 3
print(persona)

#Cambiar el valor de una clave
persona["ciudad"] = "Burgos"
persona["Numero de hijos"] = 7
print(persona)

#Eliminar una clave
#del persona["registrado"]
print(persona)

#Comprobar si una clave ya exite
existe_nombre = "nombre" in persona
print(existe_nombre)

existe_mario = "Mario" in persona["nombre"]
print(existe_mario)

#Comparar dos valores booleanos Acordarse que anteriormente hemos quitado registrado así que para que no de error podemos
#esa línea de del antes.
es_menor_y_registrado = persona["edad"]<18 and persona["registrado"]
print((es_menor_y_registrado))

#Usar NOT cin un booleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#Creame un conjunto a partir de una listra con duplicados
numeritos = [1,2,3,4,4,5,4,6,7,8]

#Convierto a conjunto. Poque así elimino duplicidades
conjuntito = set(numeritos)
print(conjuntito)

#Comparar si dos colecciones tienen los mismos elementos únicos
coleccion_a =set([1,2,2,3])
coleccion_b =set([3,2,1])

mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)

