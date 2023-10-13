import tkinter as tk
import random

class Mazo:
    def __init__(self):
        self.cartas = ['2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', '10D', 'JD', 'QD', 'KD', 'AD',
                      '2T', '3T', '4T', '5T', '6T', '7T', '8T', '9T', '10T', 'JT', 'QT', 'KT', 'AT',
                      '2P', '3P', '4P', '5P', '6P', '7P', '8P', '9P', '10P', 'JP', 'QP', 'KP', 'AP',
                      '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', '10C', 'JC', 'QC', 'KC', 'AC'] *2

    def mezclar(self):
        random.shuffle(self.cartas)

    def repartir_carta(self):
        return self.cartas.pop()