# Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

# Calcula el interés: capital * (1 + interes)

interes = 0.04
capital = float(input('Cantidad de dinero depositado en la cuenta de ahorros: '))

primer = capital * (1 + interes)

segundo = primer * (1 + interes)

tercer = segundo * (1 + interes)

print('La cantidad de ahorros tras el primer año es {:.2f}€ \nLa cantidad de ahorros tras el segundo año es {:.2f}€ \nY la cantidad de ahorros tras el tercer año es {:.2f}€'.format(primer, segundo, tercer))
