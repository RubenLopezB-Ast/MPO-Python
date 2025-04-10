#Ejercicio 4 - Múltiplos de 3 y 5¶
#Escribe un programa que pida al usuario un número entero y determine si es múltiplo de 3 o de 5.
#El programa debe imprimir un mensaje indicando el resultado. Si el número es múltiplo de ambos, debe imprimir
#"Múltiplo de 3 y 5". Si no es múltiplo de ninguno, debe imprimir "No es múltiplo de 3 ni de 5".

numero_entero = int(input("Escribe un número entero: "))

if numero_entero % 3 == 0 and numero_entero % 5 == 0:
    print("Es multiplo de tres y de cinco.")
elif numero_entero % 3 == 0:
    print(f"{numero_entero} es múltiplo de tres.")
elif numero_entero % 5 == 0:
    print(f"{numero_entero} es múltiplo de cinco")
else:
    print(f"{numero_entero} no es múltiplo ni de tres ni de cinco")


