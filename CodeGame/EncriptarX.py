letras = []

'Este funcion es un mero ejemplo'
def encriptarX(frase):
    global letras
    caracter = "X"
    frase_encriptada = ""
    for letra in frase:
        if letra.lower() in "bgkln":
            if letra.isupper():
                frase_encriptada = frase_encriptada + caracter.upper()
                letras.append(letra)
            else:
                frase_encriptada = frase_encriptada + caracter
                letras.append(letra)
        else:
            frase_encriptada = frase_encriptada + letra
    return frase_encriptada


def desencriptarX(frase):
    global letras
    frase_desencriptada =""
    contador = 0
    for i in frase:
        if i == "X":
            frase_desencriptada += letras[contador]
            contador += 1
        else:
            frase_desencriptada += i
            
    return frase_desencriptada