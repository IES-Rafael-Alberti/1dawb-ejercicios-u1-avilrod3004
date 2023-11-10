# Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.

precio = input('Introduce el precio de un producto: ')

punto = precio.find('.')

euros = precio[0:punto]
centimos = precio[(punto + 1):(punto + 3)]

print(f'Euros {euros} \nCéntimos: {centimos}')