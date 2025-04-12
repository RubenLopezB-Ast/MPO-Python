"""Ejercicio 9¶
Escribe un programa que pida el precio de un producto y, si supera los 100€, aplique un descuento del 10%.
Muestra el precio final.
"""
price = float(input("Dime el precio (Solo cantidad sin moneda)"))

if price > 100:
    discount = price * 0.10
    print(f"Tu producto cuesta {price}€  te vamos a aplicar un descuento de {discount}€ así que se te queda en: {price-discount}€ .")
else:
    print(f"Tu producto cuesta {price}€.")