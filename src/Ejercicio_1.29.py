'''
Inicio

Lee nombre

Si (nombre == '') entonces
    nombre = 'Desconocido'

Lee edad

Mientras (edad < 0 or edad > 125) hacer
    Escribe 'Introduce una edad comprendida entre 0 y 125 años'
    Lee edad

Escribe 'Te llamas ' + nombre + ' y tienes ' + edad + ' años, te quedan aún ' + (125 - edad) + ' años por cumplir'

Fin

'''

nombre = input('Nombre: ')

if (nombre == ''):
    nombre = 'Desconocido'

edad = int(input('Edad: '))

while (edad < 0 or edad > 125):
    print('Introduce una edad comprendida entre 0 y 125 años')
    edad = int(input('Edad: '))

print(f'Te llamas {nombre} y tienes {edad} años, te quedan aún {125 - edad} años por cumplir.')