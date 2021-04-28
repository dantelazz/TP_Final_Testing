import random

class Jugadores:
    def __init__(self, jugador1, jugador2, dineroJugador1, dineroJugador2, dineroJugador3, dineroJugador4):
        self.jugador1 = jugador1
        self.jugador2 = jugador2
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

    def Accionesy_y_Empresas():
        self.precioAcciones = range(0, 300)
        random.sample(actionsValue, k = 5)       
    
    
    def juego(Jugadores, CompraVentaAcciones, Accionesy_y_Empresas):
        contadorMovimientos = 0
        choice = input(str('Desea comprar o vender? C para comprar y V para vender: \n'))
        while contadorMovimientos <= 20:
            if choice == 'C' or 'c':
                sellOrBuy = input(str('De que compañia desea comprar las acciones?: '))
                sellOrBuy2 = input(int('Cuantas acciones desea comprar?: '))



Empresas("Apple", "300")