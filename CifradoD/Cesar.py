
abc = "abcdefghijklmnopqrstuvwxyz"
clave = -1

def encriptarCesar(frase):

    array = frase.strip().split(" ")
    fraseEncriptada =""

    for i in array:
        encriptado =""
        for letra in i:
            suma = abc.find(letra) + clave
            modulo = int(suma) %len(abc)
            encriptado += str(abc[modulo])
        fraseEncriptada += encriptado + " "
    return fraseEncriptada.strip()


def desencriptarCesar(frase):

    array = frase.strip().split(" ")
    fraseEncriptada = ""

    for i in array:
        encriptado = ""
        for letra in i:
            suma = abc.find(letra) - clave
            modulo = int(suma) % len(abc)
            encriptado += str(abc[modulo])
        fraseEncriptada += encriptado + " "
    return fraseEncriptada.strip()


