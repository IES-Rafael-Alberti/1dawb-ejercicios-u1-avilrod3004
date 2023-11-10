# Escribir un programa que pregunte el nombre de un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.

producto = input('Nombre del producto: ')
precio = float(input('Precio unitario: '))
unidades = int(input('Número de unidades: '))

total = precio + unidades

print('Nombre del producto {}, precio unitario {:9.2f}, número de unidades {:3.0f} y el coste total es {:11.2f}'.format(producto, precio, unidades, total))