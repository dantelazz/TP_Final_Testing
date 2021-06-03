from sympy.crypto import encipher_shift

mensaje="AHORA"
cifrado = encipher_shift(mensaje,-1)
print(cifrado)