from sympy.crypto.crypto import encipher_shift, decipher_shift


def encriptarCesar(frase):
    frase = encipher_shift(frase, -1)
    return frase


def desencriptarCesar(frase):
    array = frase.strip().split(" ")
    fraseDesencriptada = ""
    for i in array:
        fraseDesencriptada += decipher_shift( i , -1) + " "
    return fraseDesencriptada.lower()


