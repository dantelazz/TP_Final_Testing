from sympy.crypto.crypto import encipher_shift, decipher_shift

mensaje="AHORA"
cifrado = encipher_shift(mensaje,-1)
print(cifrado)
decifrar= decipher_shift(cifrado,-1)
print(decifrar)