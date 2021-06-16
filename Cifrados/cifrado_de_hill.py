import numpy as np
import math

def imprimir_matriz(char):
    for i in range(2):
        for j in range(2):
            print(int(char[i][j], '\t', end = ""))
        print('\n')

rta = int(input('Cifrado de Hill. \n \n 1. Cifrar \n 2. Descifrar \n \n Rta: '))

if rta == 1:

    #Se solicitan los datos
    texto = input('Por favor introduce el texto a cifrar: ')
    texto = texto.upper().strip().replace(' ', '')
    print('Por favor introduzca la clave (matriz 2x2)')

    clave = np.empty((4, 4))
    mensaje = ''
    m_crip = np.zeros((math.ceil(len(texto)/2), 2))

    for i in range(2):
        for j in range(2):
            mensaje = 'Posicion ' + str(i) + ',' + str(j) + ': '
            clave[i][j] = input(mensaje)

    imprimir_matriz(clave)

    diccionario_letras = {'A':0, 'B':1, 'C':2, 'D':3, 'E':4, 'F':5, 'G':6, 'H':7, 'I':8, 'J':9, 
                          'K':10, 'L':11, 'M':12, 'N':13, 'O':14, 'P':15, 'Q':16, 'R':17, 'S':18, 
                          'T':19, 'U':20, 'V':21, 'W':22, 'X':23, 'Y':24, 'Z':25}

    abecedario = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'        


#Sacar determinante
determinante = clave[0][0] * clave[1][1] - clave[0][1] * clave[1][0]

adjunta = np.zeros((2, 2))
adjunta[0][0] = clave[1][1] 
adjunta[1][1] = clave[0][0] 
adjunta[0][1] = -1 * clave[1][0]
adjunta[1][1] = -1 * clave[0][1]


tadj = np.zeros((2, 2))

tadj[0][0] = adjunta[0][0]
tadj[1][1] = adjunta[1][1]
tadj[0][1] = adjunta[1][0]
tadj[1][0] = adjunta[0][1]

determinante = determinante % 26
inClave = np.zeros((2, 2))
inClave[0][0] = ((1 / determinante) * tadj[0][0]) % 26
inClave[0][1] = ((1 / determinante) * tadj[0][1]) % 26
inClave[1][0] = ((1 / determinante) * tadj[1][0]) % 26
inClave[1][1] = ((1 / determinante) * tadj[1][1]) % 26

'''
print('Determinante ', determinante)
print('Adjunta ')
for i in range(2):
    for j in range(2):
        print(adjunta[i][j], "\t,", end='')
    print("\n")
print('Adjunta Transpuerta')

for i in range(2):
    for j in range(2):
        print(tadj[i][j], "\t", end='')
    print("\n")

print('Matriz inversa a la clave ')
for i in range(2):
    for j in range(2):
        print(inClave[i][j], "\t", end='')
    print("\n")
'''

i = 0
j = 0

while True:
    try:
        if (np.size(m_crip) / 2 == j):
            break
        #print(texto[i], ' - ', texto[i + 1])
        m_crip[j][0] = diccionario_letras[texto[i]]
        m_crip[j][1] = diccionario_letras[texto[i + 1]]
        i += 2
        j += 1

    except:
        print(texto[i])
        m_crip[j][0] = diccionario_letras[texto[i]]
        break

#for i in range (m_crip.lenght)        

c1 = 0
c2 = 0
m1 = 0
m2 = 0

descipher = np.zero(m_crip.shape)
print('Texto Descrifrado: ')
for i in range (int(np.size(m_crip) / 2)):
    m1 = m_crip[i][0]
    m2 = m_crip[i][1]
    c1 = inClave[0][0] * m1 + inClave[1][0] * m2
    c2 = inClave[0][1] * m1 + inClave[1][1] * m2

#print(int(cipher[i][0]), ' - ', int(cipher[i][i]))
print(abecedario[int(descipher[i][0])], '', abecedario[int(descipher[i][1])], ' ', end='')