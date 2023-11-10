# Escribir un programa que pregunte el correo electrónico del usuario en la consola y muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante de la arroba @) pero con dominio ceu.es.

correo = str(input('Correo electrónico: '))
dominio = correo.find('@')
correo_nuevo = correo.replace(correo[dominio:], "@ceu.es")

print(correo_nuevo)