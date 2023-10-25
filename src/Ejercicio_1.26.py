# Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

cesta = input('Introduce la cesta de la compra (los productos separados por comas): ')

cesta2 = cesta.replace(' ','').replace(',','\n')

print(cesta2)
