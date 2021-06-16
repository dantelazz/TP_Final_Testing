import Geringoso
import random
import csv
from sympy.crypto.crypto import encipher_shift, decipher_shift
import EncriptarX

nivel = 2
frase = ""
frase_encriptada = ""
vida = 3


# Leo el archivo .csv y busco por nivel, luego busco una palabra ramdon y la retorno.
def seleccionoPalabrasPorNivel():
    global nivel, frase, frase_encriptada
    listPalabras = []
    reader = csv.reader(
        open("C:/Users/El Poshi/Desktop/TareaTestingConDante/CodeGame/Frases.csv"))
    for row in reader:
        listPalabras.append(row)
    # Obtengo palabra al azar
    frase = obtenerPalabraAlAzar(listPalabras[nivel])
    frase_encriptada = funcionEncriptarFrase()
    return frase_encriptada


def funcionEncriptarFrase():
    global nivel, frase
    arrayFrase = frase.split(" ")
    fraseString = ""
    for palabra in arrayFrase:
        if nivel == 0:
            fraseString += EncriptarX.encriptarX(
                Geringoso.encriptarGeringoso(palabra)) + " "
        elif nivel == 1:
            fraseString += EncriptarX.encriptarX(palabra) + " "
        elif nivel == 2:
    return fraseString


def intentoDeDesencripcion(opcion):
    global frase_encriptada
    if opcion == 0:
        frase_encriptada = Geringoso.desencriptarGeringoso(frase_encriptada)
    if opcion == 1:
        frase_encriptada = EncriptarX.desencriptarX(frase_encriptada)


def intentos():
    global vida, frase_encriptada, frase
    juego = True
    while juego:
        if vida > 0:
            print(
                "Seleccione lenguaje para desencriptar: \n 0.Geringoso\n 1.X\n 2.Cesar \n  ")
            jugada = int(input())
            intentoDeDesencripcion(jugada)
            if frase == frase_encriptada:
                print("Ganaste !!")
            else:
                vida -= 1
        else:
            print("Perdiste :( ")
            juego = False


# Recibo una lista de palabras y selecciono una random
def obtenerPalabraAlAzar(listaDePalabras):
    palabraSeleccionada = random.choice(listaDePalabras)
    return palabraSeleccionada


def encriptarCesar(frase):
    frase = encipher_shift(frase, -1)
    return frase


def desencriptarCesar(frase):
    frase = decipher_shift(frase, -1)
    return frase


while True:
    nivel = int(
    input("Ingrese el numero dificultad:\n 0 Facil\n 1 Medio\n 2 Dificil\n"))
    print("La frase a desencriptar es: ")
    print(seleccionoPalabrasPorNivel())
    intentos()
