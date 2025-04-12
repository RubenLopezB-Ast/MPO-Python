"""Ejercicio 7¶
Escribe un programa que pida dos números y un operador (+, -, *, /) y muestre el resultado de la operación."""

num1= float(input("Escribe un número: "))
num2= float(input("Escribe otro número:"))
oper= input("Escribe un operador aritmético (+,-,*,/). : ")

if oper == "+":
    print(f"Suma {num2} más {num1} resultado {num1+num2} . ")
elif oper == "-":
    print(f"Resta {num1} menos {num2} resultado {num1-num2}. ")
elif oper == "*":
    print(f"Multiplicación {num1} por {num2} resultado {num1*num2}. ")
elif oper == "/":
    if num2 == 0:
        print(f"Si divides {num1} entre 0 el resultado es cero. Prueba con otros números. ")
    elif num1 == 0:
        print(f"Cero no se puede dividir ni entre {num2} ni entre nada. Prueba con otros números. ")
    else:
        print(f"División {num1} entre {num2} resultado {num1 / num2}. ")
else:
    print(f"Algo falla inténtalo de nuevo con otros números.")


#Otra manera:

nu1 = float(input("Introduce el primer número: "))
nu2 = float(input("Introduce el segundo número: "))
operado = input("Introduce un operador (+, -, *, /): ")

if operado == "+":
    resultado = nu1 + nu2
elif operado == "-":
    resultado = nu1 - nu2
elif operado == "*":
    resultado = nu1 * nu2
elif operado == "/":
    if nu2 != 0:
        resultado = nu1 / nu2
    else:
        resultado = "Error: División por cero."
else:
    resultado = "Operador no válido."

print(f"Resultado: {resultado}")