# Escribe un programa que le pida al usuario una temperatura en grados Celsius, la convierta a grados Fahrenheit e imprima por pantalla la temperatura convertida. 

def far():
    temp = float(input('Dame una temperatura en Celsius: '))
    return (temp * 9 / 5) + 32

print(f'Son {far():.2f} grados en Fahrenheit')