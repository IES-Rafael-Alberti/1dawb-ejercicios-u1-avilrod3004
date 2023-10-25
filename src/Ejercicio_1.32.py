# Lee dos números y crea la serie que los une de 1 en 1...

x = int(input('Introduce un número: '))
y = int(input('Introduce otro: '))

if (x < y):
    num_ini = x
    num_fin = y

else:
    num_ini = y
    num_fin = x

serie = ''

while (num_ini <= num_fin):
    serie = serie + str(num_ini)

    if (num_ini != num_fin):
        serie = serie + '-'

    num_ini = num_ini + 1

print(serie)
