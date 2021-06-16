import random
letras = []

def encriptarX(frase):
    global letras
    frase_encriptada = ""
    for letra in frase:
        caracter = random.randint(1,9) 
        if letra.lower() in "bgkln":
            if letra.isupper():
                frase_encriptada = frase_encriptada + str(caracter)
                letras.append(letra)
            else:
                frase_encriptada = frase_encriptada + str(caracter)
                letras.append(letra)
        else:
            frase_encriptada = frase_encriptada + letra
    return frase_encriptada


def desencriptarX(frase):
    global letras
    contador = 0
    nums = ["1","2","3","4","5","6","7","8","9"]
    frase_desencriptada =""
    for i in frase:
        if i in nums :
            frase_desencriptada += letras[contador]
            contador += 1
        else:
            frase_desencriptada += i
    return frase_desencriptada