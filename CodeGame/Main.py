caracter_elegido= "X"

def encriptar(frase,caracter):
    frase_encriptada =""
    for letra in frase:
        if letra.lower() in "aeiou":
            if letra.isupper():
                frase_encriptada = frase_encriptada + caracter.upper()
            else:
                frase_encriptada = frase_encriptada + caracter
        else:
            frase_encriptada = frase_encriptada + letra
    return frase_encriptada

while True:
    print(encriptar(input("Ingrese frase a encriptar: \n"),caracter_elegido))
    print("\n Ingrese\n(1) para encriptar otra frase")
    print("(2) para finalizar")
    opcion = input(">")
    if opcion == "2":
        print("Finalizado")
        break

