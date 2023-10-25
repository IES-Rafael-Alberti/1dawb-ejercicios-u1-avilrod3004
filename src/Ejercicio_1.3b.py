# Suponiendo que se han ejecutado las siguientes sentencias de asignación:
# ancho = 17
# alto = 12.0
# Para cada una de las expresiones siguientes, intenta adivinar el valor de la expresión y su tipo sin ejecutarlas en el intérprete:
# ancho / alto --> 1.4... --> float
# ancho // 2 --> 1 --> float
# ancho / 2 --> 8.5 --> float
# ancho * 2 --> 34 --> int
# ancho * alto --> 204 --> float
# (5 + 1) * 3 --> 18 --> int
# (5 + 1) / 3 --> 2 --> int

ancho = 17
alto = 12.0

expresion = ancho / alto
print(f'ancho / alto = {expresion} y es de tipo {type(expresion)}')

expresion = ancho // alto
print(f'ancho // alto = {expresion} y es de tipo {type(expresion)}')

expresion = ancho / 2
print(f'ancho / 2 = {expresion} y es de tipo {type(expresion)}')

expresion = ancho * 2
print(f'ancho * 2 = {expresion} y es de tipo {type(expresion)}')

expresion = ancho * alto
print(f'ancho * alto = {expresion} y es de tipo {type(expresion)}')

expresion = (5 + 1) * 3
print(f'(5 + 1) * 3 = {expresion} y es de tipo {type(expresion)}')

expresion = (5 + 1) / 3
print(f'(5 + 1) / 3 = {expresion} y es de tipo {type(expresion)}')