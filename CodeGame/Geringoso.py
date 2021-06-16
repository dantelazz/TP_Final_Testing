def encriptarGeringoso(frase):
    palabraNueva =""
    for letra in frase:
        if letra=="a" or letra=="á":
            palabraNueva += "apa"

        elif letra=="e" or letra=="é":
            palabraNueva +="epe"

        elif letra=="i" or letra=="í":
            palabraNueva +="ipi"

        elif letra=="o" or letra=="ó":
            palabraNueva += "opo"

        elif letra=="u" or letra=="ú":
            palabraNueva += "upu"

        else:
            palabraNueva += letra
    return palabraNueva

def desencriptarGeringoso(frase):
    return frase.replace("apa","a").replace("epe","e").replace("ipi","i").replace("opo","o").replace("upu","u")
