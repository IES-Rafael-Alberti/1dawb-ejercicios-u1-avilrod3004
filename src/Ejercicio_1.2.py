# Escribe un programa para pedirle al usuario las horas de trabajo y el precio por hora y calcule el importe total del servicio.

horas = int(input('Horas de trabajo: '))
coste = int(input('Coste por horas: '))

total = horas * coste

print(f'Importe total: {total}')