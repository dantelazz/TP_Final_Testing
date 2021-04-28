import random #Hacemos uso de la libreria random para generar los precios de las acciones al azar

class Jugadores: #Definimos tanto la cantidad de jugadores, como el dinero de cada uno
    def __init__(self, jugador1, jugador2, dineroJugador1, dineroJugador2:
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.dineroJugador1 = dineroJugador1
        self.dineroJugador2 = dineroJugador2


class CantidadDeAcciones:
    def __init__(self, cantAccionesJugador1, cantAccionesJugador2):
        self.cantAccionesJugador1 = cantAccionesJugador1
        self.cantAccionesJugador2 = cantAccionesJugador2

    def cantidadDeAccionesJugadores():
        self.cantAccionesJugador1 = accionesDelJugador1
        self.cantAccionesJugador2 = accionesDelJugador2

class CompraVentaAcciones: #Definimos la compra y venta de acciones
    def __init__(self, comprarAccion, venderAccion):
        self.comprarAccion = comprarAccion
        self.venderAccion = venderAccion

class Empresas:
    def __init__(self, nombreEmpresas, precioAcciones):
        self.nombreEmpresas = nombreEmpresas
        self.precioAcciones = precioAcciones

    def Acciones_y_Empresas(): #En el __init__ como aca, asignamos el valor de cada acción
        self.nombreEmpresas = nombre_Empresas
        nombre_Empresas = ('Apple', 'Samsung')
        self.precioAcciones = range(0, 300)
        precioAcciones = random.sample(self.precioAcciones, k = 2) #Hacemos que solo imprima 2 valores de las acciones por el numero de acciones total  
        
print('******************************')
print('* El Inversionista The Game! *')
print('******************************\n')

print('Las empresas que se dedican a la compra-venta de acciones son: ')
print('Sus valores son: ')

def juego():
    contadorMovimientos = 0 
    print('Ingresar los nombres de los jugadores:')
    self.jugador1 = input(str('Jugador 1: '))  
    self.jugador2 = input(str('Jugador 2: '))
    
    buyOrSell = input(str('Comprar o Vender?: '))
    while contadorMovimientos <= 20:
        if buyOrSell == 'c' or 'C':
            buyingQuestion1 = input(str('De que compañia queres comprar acciones?: '))
            buyingQuestion2 = input(int('Cuantas acciones queres comprar?: '))
            while self.dineroJugador1 > 0:
                if buyingQuestion1 == 'apple' or 'Apple' or 'APPLE':
                    precioAcciones - self.dineroJugador1
                    contadorMovimientos = contadorMovimientos + 1
                    accionesDelJugador1 = accionesDelJugador1 + 1
                    print('A ' + self.jugador1 + ' le quedan: $' + self.dineroJugador1)
                else:   
                    precioAcciones - self.dineroJugador1
                    contadorMovimientos = contadorMovimientos + 1
                    accionesDelJugador2 = accionesDelJugador2 + 1
                    if self.dinero < 1:
                        print('No tienes suficiente dinero. Vuelva por donde vino')
                        break

        elif buyOrSell == 'v' or 'V':
            sellingQuestion1 = input(str('A que compañia queres venderle acciones?: '))
            sellingQuestion2 = input(int('Cuantas queres vender?: '))
            print('Usted esta a punto de vender ' + sellingQuestion2 + 'acciones a: ' + sellingQuestion1)
            confirmation = input('Por favor escriba "S" para confirmar: ')
            while confirmation == 's' or 'S':
                accionesDelJugador1 - sellingQuestion2
                dineroGanadoPorVentaDeAcciones = sellingQuestion2 * precioAcciones
                self.dineroJugador1 + dineroGanadoPorVentaDeAcciones
                print('Felicidades, su capital ahora es de: $', self.dineroJugador1)




runGame = juego()  #No anda
runGame()                   
                   
            

        
        
        
        
        
           
'''    
def juego(Jugadores, CompraVentaAcciones, Acciones_y_Empresas):
    contadorMovimientos = 0
    print('Ingrese los nombres de los jugadores: ')
    player1 = str(input('Jugador 1: '))
    player2 = str(input('Jugador 2: '))
    player3 = str(input('Jugador 3: '))
    player4 = str(input('Jugador 4: '))

    choice = input(str('Desea comprar o vender? C para comprar | V para vender: \n'))

    print(self.nombreEmpresas)
    print(precioAcciones)
    while contadorMovimientos <= 20:
        if choice == 'C' or 'c':
            sellOrBuy = input(str('De que compañia desea comprar las acciones?: '))
            sellOrBuy2 = input(int('Cuantas acciones desea comprar?: '))
            for num in sellOrBuy2:
                self.dineroJugador1 - self.precioAcciones #Realizamos el descuento de dinero tras la compra de la acción
                print('Al jugador ' + self.jugador1 + ' le quedan: $' + self.dineroJugador1)
                contadorMovimientos = contadorMovimientos + 1 #Hacemos que el contador de movimientos incremente
'''
