import random

class Jugadores:
    def __init__(self, jugador1, jugador2, jugador3, jugador4, dineroJugador1, dineroJugador2, dineroJugador3, dineroJugador4):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
        self.jugador3 = jugador3
        self.jugador4 = jugador4
        self.dineroJugador1 = dineroJugador1
        self.dineroJugador2 = dineroJugador2
        self.dineroJugador3 = dineroJugador3
        self.dineroJugador4 = dineroJugador4


class CompraVentaAcciones:
    def __init__(self, comprarAccion, venderAccion):
        self.comprarAccion = comprarAccion
        self.venderAccion = venderAccion

class Empresas:
    def __init__(self, nombreEmpresas, precioAcciones):
        self.nombreEmpresas = nombreEmpresas
        self.precioAcciones = precioAcciones

    def Acciones_y_Empresas():
        self.nombreEmpresas = ('Apple', 'Samsung')
        self.precioAcciones = range(0, 300)
        precioAcciones = random.sample(self.precioAcciones, k = 5)       
    
    def juego(Jugadores, CompraVentaAcciones, Acciones_y_Empresas):
        contadorMovimientos = 0
        choice = input(str('Desea comprar o vender? C para comprar | V para vender: \n'))
        print(self.nombreEmpresas)
        print(precioAcciones)
        while contadorMovimientos <= 20:
            if choice == 'C' or 'c':
                sellOrBuy = input(str('De que compañia desea comprar las acciones?: '))
                sellOrBuy2 = input(int('Cuantas acciones desea comprar?: '))
                for num in sellOrBuy2:
                    self.dineroJugador1 - self.precioAcciones
                    print('Al jugador ' + self.jugador1 + 'le quedan: $' + self.dineroJugador1)
                    contadorMovimientos = contadorMovimientos + 1

               