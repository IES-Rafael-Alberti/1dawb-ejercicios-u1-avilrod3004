# Escribe un programa que pida el nombre del usuario para luego darle la bienvenida.

def cadena(nombre):
    nombre = input('Escribe tu nombre: ')
    return nombre

print(f'Hola, {cadena()}')