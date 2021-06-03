import os

c = open('archivoDeTexto.txt', 'a')

nombre = str(input('Ingrese su nombre: '))
apellido = str(input('Ingrese su apellido: '))

if os.path.exists('archivoDeTexto.txt'):
    c.write(nombre + ' ')
    c.write(apellido + ' \n')
else:
    print('El documento no existe')

c = open('archivoDeTexto.txt', 'r')
print(c.read()) 