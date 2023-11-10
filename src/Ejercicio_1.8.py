# Escribir el programa del ejercicio 1.7 usando solamente dos variables diferentes.

num1y2y3 = input('Dime tres números (separados por un espacio): ')

suma = int(num1y2y3[0]) + int(num1y2y3[2]) + int(num1y2y3[-1])

print(f'La suma de los tres números es {suma}')