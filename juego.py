from mazo import *


class Juego:
    def __init__(self):
        self.mazo = Mazo()
        self.mazo.mezclar()
        self.mano_jugador = []
        self.mano_computadora = [self.mazo.repartir_carta()]

    def jugador_pedir_carta(self):
        if self.calcular_valor_mano(self.mano_jugador) < 21:
            self.mano_jugador.append(self.mazo.repartir_carta())

    def calcular_valor_mano(self, mano):
        valor = 0
        ases = mano.count('AD') + mano.count('AP') + mano.count('AT') + mano.count('AC')
        for carta in mano:
            valor_carta = carta[:-1]
            if valor_carta in ['J', 'Q', 'K']:
                valor += 10
            elif valor_carta == 'A':
                valor += 11
            else:
                valor += int(valor_carta)
        while valor > 21 and ases:
            valor -= 10
            ases -= 1
        return valor

    def turno_computadora(self):
        while self.calcular_valor_mano(self.mano_computadora) < 17:
            self.mano_computadora.append(self.mazo.repartir_carta())