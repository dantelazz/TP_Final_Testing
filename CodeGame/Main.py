import random
import csv
from CifradoD import Cesar, EncriptarX, Geringoso



# Lee el archivo .csv y busco por nivel, luego busco una palabra ramdon y la retorno.
def seleccionoPalabrasPorNivel(nivel):
    listPalabras = []
    reader = csv.reader(
        open("Frases.csv"))
    for row in reader:
        listPalabras.append(row)
    # Obtengo palabra al azar
    frase = obtenerPalabraAlAzar(listPalabras[nivel])
    return frase


# Recibo una lista de palabras y selecciono una random
def obtenerPalabraAlAzar(listaDePalabras):
    return random.choice(listaDePalabras)


# Toma los lenguajes de encriptacion y los cifra segun el nivel elegido
def funcionEncriptarFrase(nivel, frase):
    arrayFrase = frase.split(" ")
    fraseString = ""
    for palabra in arrayFrase:
        if nivel == 0:
            fraseString += EncriptarX.encriptarX(Geringoso.encriptarGeringoso(palabra)) + " "
        elif nivel == 1:
            fraseString += EncriptarX.encriptarX(Cesar.encriptarCesar(palabra)) + " "
        elif nivel == 2:
            fraseString += EncriptarX.encriptarX(Cesar.encriptarCesar(Geringoso.encriptarGeringoso(palabra))) + " "
    return fraseString


# Segun la opcion elegida desencripta
def intentoDeDesencripcion(opcion,frase_encriptada):
    if opcion == 0:
        frase_encriptada = Geringoso.desencriptarGeringoso(frase_encriptada)
    elif opcion == 1:
        frase_encriptada = EncriptarX.desencriptarX(frase_encriptada)
    elif opcion == 2:
        frase_encriptada = Cesar.desencriptarCesar(frase_encriptada)

    return frase_encriptada

    # Intentos mientras las vidas sean mayor a cero, el juego corre, muestra un menu y se selecciona que lenguaje usar para desencriptar, ademas finaliza el juego


def intentos(vida, frase_encriptada, frase):
    juego = True
    while juego:
        if vida > 0:
            print("La frase a desencriptar es: {} \n".format(frase_encriptada))
            print("Seleccione lenguaje para desencriptar: \n 0.Geringoso\n 1.Numeros\n 2.Cesar \n  ")
            numeros = [0,1,2]
            jugada = input()
            try:
                jugada = int(jugada)
                if jugada in numeros:
                    frase_encriptada = intentoDeDesencripcion(jugada,frase_encriptada)
                    if frase == frase_encriptada.strip().lower():
                        print("Ganaste !! La frase era: {}".format(frase))
                        juego = False
                        print("Desea Jugar de nuevo? (s/n)")
                        opcion = input()
                        if opcion == "s":
                            vida = 4
                            menu()
                        else:
                            break
                    else:
                        vida -= 1
                else:
                    print("Debe ingresar los numeros correspondientes a la opcion (0 , 1 y 2)")
                    intentos(vida, frase_encriptada, frase)
            except :
                    print("La opcion debe ser un numero")
                    intentos(vida, frase_encriptada, frase)
        else:
            print("Perdiste :( la frase era: {}".format(frase))
            juego = False


def menu():
    vida = 4
    nivel = (input("Ingrese el numero dificultad:\n 0 Facil\n 1 Medio\n 2 Dificil\n"))
    try:
        nivel = int(nivel)
        numeros = [0, 1, 2]
        if nivel in numeros:
            frase_seleccionada = seleccionoPalabrasPorNivel(nivel)
            frase_encriptada = funcionEncriptarFrase(nivel,frase_seleccionada)
            intentos(vida,frase_encriptada,frase_seleccionada)
        else:
            print("La opcion debe ser 0 1 o 2")
            menu()
    except:
        print("La opcion debe ser un numero")
        menu()


print("Bienvenido a Code Game Romantic Version 1.0 \nRecomendamos jugarlo con tu vieja al lado\n")
menu()