# Escribe un programa que solicite tres números al usuario y calcule e imprima por pantalla su suma.

num1 = float(input('Dime el primer número: '))
num2 = float(input('Dime el segundo número: '))
num3 = float(input('Dime el tercer número: '))

suma = num1 + num2 + num3

print('La suma de los tres números es {:.2f}'.format(suma))