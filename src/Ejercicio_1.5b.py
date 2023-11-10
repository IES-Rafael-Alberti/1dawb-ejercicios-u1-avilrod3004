# Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

importe = float(input('¿Cuál es el importe sin IVA del artículo? '))
iva = float(input('¿Qué tipo de IVA hay que aplicarle? '))

total = importe + (importe * (iva / 100))

print('El precio final del producto es {:.2f}€'.format(total))