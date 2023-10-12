import tkinter as tk
import random
import time

def calcular_valor_mano(mano):
    valor = 0
    ases = 0
    for carta in mano:
        if carta in ['J', 'Q', 'K']:
            valor += 10
        elif carta == 'A':
            ases += 1
            valor += 11
        else:
            valor += carta
    while valor > 21 and ases:
        valor -= 10
        ases -= 1
    return valor

def tomar_carta_automaticamente():
    if not jugador_se_planto: 
        if calcular_valor_mano(mano_jugador) < 21:
            carta = random.choice(baraja)
            mano_jugador.append(carta)
            ventana.update() 
            mano_jugador_label.config(text=f"Mano del Jugador: {mano_jugador} ({calcular_valor_mano(mano_jugador)})")
        if calcular_valor_mano(mano_jugador) < 21 and not jugador_se_planto:
            ventana.after(1000, tomar_carta_automaticamente)
        else:
            turno_de_computadora()

def turno_de_computadora():
    while calcular_valor_mano(mano_computadora) < 17:
        carta = random.choice(baraja)
        mano_computadora.append(carta)
        mano_jugador_label.config(text=f"Mano del Jugador: {mano_jugador} ({calcular_valor_mano(mano_jugador)})")
        ventana.update()  
        time.sleep(1)
    mostrar_resultado()

def mostrar_resultado():
    if calcular_valor_mano(mano_jugador) > 21:
        mensaje = "¡El jugador ha perdido! La mano del jugador supera 21."
    elif calcular_valor_mano(mano_computadora) > 21:
        mensaje = "¡La computadora ha perdido! La mano de la computadora supera 21."
    elif calcular_valor_mano(mano_jugador) == calcular_valor_mano(mano_computadora):
        mensaje = "¡Es un empate!"
    elif calcular_valor_mano(mano_jugador) > calcular_valor_mano(mano_computadora):
        mensaje = "¡El jugador ha ganado!"
    else:
        mensaje = "¡La computadora ha ganado!"
    resultado_label.config(text=mensaje)

def plantarse():
    global jugador_se_planto
    jugador_se_planto = True
    turno_de_computadora()

ventana = tk.Tk()
ventana.title("Juego 21")

baraja = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K', 'A'] * 4

mano_jugador = [random.choice(baraja), random.choice(baraja)]
mano_computadora = [random.choice(baraja), random.choice(baraja)]
jugador_se_planto = False

mano_jugador_label = tk.Label(ventana, text=f"Mano del Jugador: {mano_jugador} ({calcular_valor_mano(mano_jugador)})")
mano_jugador_label.pack()
mano_computadora_label = tk.Label(ventana, text=f"Mano de la Computadora: [{mano_computadora[0]}, ?]")
mano_computadora_label.pack()

resultado_label = tk.Label(ventana, text="")
resultado_label.pack()

tomar_carta_button = tk.Button(ventana, text="Tomar Carta", command=tomar_carta_automaticamente)
tomar_carta_button.pack()

plantarse_button = tk.Button(ventana, text="Plantarse", command=plantarse)
plantarse_button.pack()

ventana.mainloop()
