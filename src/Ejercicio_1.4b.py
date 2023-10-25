# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida.

temp = float(input('Dame una temperatura en Celsius: '))

far = (temp * 9 / 5) + 32

print('La temperatura en grados Farenheit es {:.2f}ºF ({:.2f}ºC)'.format(far, temp))