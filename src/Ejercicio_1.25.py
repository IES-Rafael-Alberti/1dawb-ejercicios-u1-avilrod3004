# Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.

fecha = input('Introduce tu fecha de nacimiento (dd/mm/aaaa): ')

barra1 = fecha.find('/')
barra2 = fecha.find('/', (barra1 + 1))

dia = fecha[0:barra1]
mes = fecha[(barra1 + 1):barra2]
year = fecha[(barra2 + 1):]

print(f'Día {dia}, mes {mes} y año {year}')