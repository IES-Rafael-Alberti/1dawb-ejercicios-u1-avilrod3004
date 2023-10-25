# Calcula la media de las notas de un curso.
# Píde el número de notas que va a introducir al principio.
# El número de notas no puede ser un número superior a 100, o inferior a 1.
# Si no introduce un número de notas correcto escribimos el mensaje "Error - el número de notas debe ser un número entero entre 1 y 100" 

total = int(input('¿Cuántas notas vas a introducir? '))

while (total < 1 or total > 100):
    print('Error - El número de notas debe ser un número entero entre 1 y 100')
    total = int(input('¿Cuántas notas vas a introducir? '))

print(f'Dame las {total} notas del curso: ')
media = 0
cont = 1

while (cont <= total):
    nota = float(input())
    media = media + nota
    cont = cont + 1

media = media / total
print('La media es {:.2f}'.format(media))