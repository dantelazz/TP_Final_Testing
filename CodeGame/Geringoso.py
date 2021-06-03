palabra = input("ingresa una palabra")

frase=""

for letra in palabra:
    if letra in "AEIOUaeiou":
        frase += letra +"p" + letra


print(frase)