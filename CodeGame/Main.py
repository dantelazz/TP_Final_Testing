

def encriptar_X(frase):
    caracter="X"
    frase_encriptada =""
    for letra in frase:
        if letra.lower() in "bcdfghklmnpqrstvwxyz":
            if letra.isupper():
                frase_encriptada = frase_encriptada + caracter.upper()
            else:
                frase_encriptada = frase_encriptada + caracter
        else:
            frase_encriptada = frase_encriptada + letra
    return frase_encriptada

while True:
    print(encriptar_X(input("Ingrese frase a encriptar: \n")))
    print("\n Ingrese\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input(">")
    if opcion == "2":
        print("Finalizado")
        break

