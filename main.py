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


    def juego(Jugadores, CompraVentaAcciones):
        contadorMovimientos = 0
        choice = input(str('Desea comprar o vender? C para comprar y V para vender: \n'))
        while 