# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

num1y2y3 = input('Dime tres números (separados por un espacio): ')

suma = float(num1y2y3[0]) + float(num1y2y3[2]) + float(num1y2y3[-1])

print('La suma de los tres números es {:.2f}'.format(suma))