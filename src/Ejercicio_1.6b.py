# Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

total = float(input('¿Cuál es el precio final del prodcuto? '))
iva = 0.10


importe = (100 * total) / 110

iva_pagado = total - importe

print('El IVA pagado es {:.2f} y el importe sin IVA es {:.2f}'.format(iva_pagado, importe))