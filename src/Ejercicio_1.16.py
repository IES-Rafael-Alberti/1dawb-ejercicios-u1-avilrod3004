# Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.

BARRA = 3.49

descuento = ((BARRA * 60) / 100)
barra_no_dia = BARRA - descuento

barras_vendidas = int(input('Número de barras vendidas que no son del día: '))

total = barras_vendidas * barra_no_dia

print(f'El precio habital de una barra de pan es {BARRA}, se le aplica un descuento de {descuento} por no ser freca.')
print(f'El coste de total de todas las barras no frecas vendidas es {total}')