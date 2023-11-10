'''
Inicio

Lee num1
Lee num2

Mientras (num2 == num1) hacer
    Escribe "Los números no pueden ser iguales"
    Lee num2

Si (num1 < num2) entonces
    Escribe 'El número menor es el ' + num1 + ' y entre ellos existen ' + (num2 - num1) + ' números enteros'
Sino
    Escribe 'El número menor es el ' + num2 + ' y entre ellos existen ' + (num1 - num2) + ' números enteros'

Fin
'''

num1 = int(input('Número 1: '))
num2 = int(input('Número 2: '))

while (num2 == num1):
    print('Los números no puede ser iguales')
    num2 = int(input('Número 2: '))

if (num1 < num2):
    print(f"El número menor es el {num1} y entre ellos existen {num2 - num1} números enteros.")
else:
    print(f'El número menor es el {num2} y entre ellos existen {num1 - num2} números entero.')