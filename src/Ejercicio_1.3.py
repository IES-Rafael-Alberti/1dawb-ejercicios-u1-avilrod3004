# Suponiendo que se han ejecutado las siguientes sentencias de asignación:
# ancho = 17
# alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
# 1. ancho / 2 --> 8.5 --> float
# 2. ancho // 2 --> 8 --> int
# 3. alto / 3 --> 4.0 --> float
# 4. 1 + 2 * 5 --> 11 --> int

ancho = 17
alto = 12.0

resultado1 = ancho / 2
print(f'ancho / 2 = {resultado1}')
print(type(resultado1))

resultado2 = ancho // 2
print(f'ancho // 2 = {resultado2}')
print(type(resultado2))

resultado3 = alto / 3
print(f'alto / 3 = {resultado3}')
print(type(resultado3))

resultado4 = 1 + 2 * 5
print(f'1 + 2 * 5 = {resultado4}')
print(type(resultado4))