import random
letras = []

def encriptarX(frase):
    global letras
    frase_encriptada = ""
    for letra in frase:
        character = random.randint(1,9)
        if letra.lower() in "bgkln":
            frase_encriptada += str(character)
            letras.append(letra)
        else:
            frase_encriptada += letra
    return frase_encriptada


def desencriptarX(frase):
    global letras
    contador = 0
    nums = "123456789"
    frase_desencriptada =""
    for i in frase:
        if i in nums :
            frase_desencriptada += letras[contador]
            contador += 1
        else:
            frase_desencriptada += i
    return frase_desencriptada