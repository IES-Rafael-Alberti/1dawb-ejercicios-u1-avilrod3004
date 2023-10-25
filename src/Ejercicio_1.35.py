# Pide dos números. Después pide un tercer número del 1 al 4, dependiendo de este número el algoritmo debe hacer lo siguiente:
#	- Si no es un número correcto, escribir un mensaje de error.
#	- Si es un 1, escribir la suma de los dos primeros números.
#	- Si es un 2, escribir la resta de los dos primeros números.
#	- Si es un 3, escribir la multiplicación de los dos primeros números.
#	- Si es un 4, escribir la división de los dos primeros números, siempre que el segundo no sea un 0. Si el segundo número es un 0 escribe un mensaje de error "división por cero no es posible".

print('Introduce dos números: ')
n1 = int(input())
n2 = int(input())

opcion = 0

while (opcion < 1 or opcion > 4):
    opcion = int(input('Introduce una opción (1 = suma / 2 = resta / 3 = multiplicación / 4 = resta): '))

    if (opcion < 1 or opcion > 4):
        print('Error - No es una opción correcta (1-4)')

if (opcion == 1):
    print(f'{n1} + {n2} = {n1 + n2}')

elif (opcion == 2):
    print(f'{n1} - {n2} = {n1 - n2}')

elif (opcion == 3):
    print(f'{n1} * {n2} = {n1 * n2}')

else:
    if (n2 == 0):
        print('La división por cero no es posible')
    
    else:
        print(f'{n1} / {n2} = {n1 / n2}')