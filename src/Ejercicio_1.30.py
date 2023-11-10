'''
Inicio

Lee num

Lee incremento
Mientras (incremento < 0) hacer
    Escribe 'El valor del incremento debe ser mayor que 0.'
    Lee incremento

Lee total
Mientras (total < 0) hacer
    Escribe 'El valor del total de la serie debe ser mayor que 0.'
    Lee total

Escribe 'Serie => ' + num + '-'
cont = 0

Mientras (cont <= total) hacer
    num = num + incremento
    cont = cont + 1

    si (cont < (total - 2))
        Escribe num + ".."

    si (cont == (total - 2)) 
        Escribe num

    si (cont == (total - 1))
        Escribe "-" + num
 

Fin

'''

num = int(input('Introduce un número de inicio: '))

incremento = int(input('Introduce un incremento: '))
while (incremento < 0):
    print('El valor del incremento debe ser mayor que 0.')
    incremento = int(input('Introduce un incremento: '))

total = int(input('Introduce un valor para el total de la serie: '))
while (total < 0):
    print('El valor del incremento debe ser mayor que 0.')
    total = int(input('Introduce un valor para el total de la serie: '))

frase = "Serie => " + str(num) + "-"
cont = 0

while (cont <= total):
    num = num + incremento
    cont = cont + 1

    if (cont < (total - 2)):
        frase = frase + str(num) + ".."

    elif (cont == (total - 2)):
        frase = frase + str(num)

    elif (cont == (total - 1)):
        frase = frase + "-" + str(num)

print(frase)