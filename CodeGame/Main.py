from sympy.crypto.crypto import encipher_shift, decipher_shift



def encriptarX(frase):
    caracter = "X"
    frase_encriptada = ""
    for letra in frase:
        if letra.lower() in "bcdfghklmnpqrstvwxyz":
            if letra.isupper():
                frase_encriptada = frase_encriptada + caracter.upper()
            else:
                frase_encriptada = frase_encriptada + caracter
        else:
            frase_encriptada = frase_encriptada + letra
    return frase_encriptada


def encriptarCesar(frase):
    frase = encipher_shift(frase, -1)
    return frase


def desencriptarCesar(frase):
    frase = decipher_shift(frase, -1)
    return frase


while True:
    print(encriptarX(input("Ingrese frase a encriptar: \n")))
    print("\n Ingrese\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input(">")
    if opcion == "2":
        print("Finalizado")
        break
