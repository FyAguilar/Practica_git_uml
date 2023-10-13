from juego import *

class Interfaz:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego 21")
        self.juego = Juego()

        self.frame_jugador = tk.Frame(self.root)
        self.frame_jugador.pack()
        self.frame_computadora = tk.Frame(self.root)
        self.frame_computadora.pack()

        self.etiqueta_jugador = tk.Label(self.frame_jugador, text=f"Mano del Jugador: ({self.juego.calcular_valor_mano(self.juego.mano_jugador)})")
        self.etiqueta_jugador.pack()
        self.pantalla = tk.Label(self.frame_computadora, text=f"Mano de la Computadora: [{self.juego.mano_computadora[0]}, ?]")
        self.pantalla.pack()

        self.boton_pedir_carta = tk.Button(self.frame_jugador, text="Pedir Carta", command=self.pedir_carta)
        self.boton_pedir_carta.pack()
        self.boton_plantarse = tk.Button(self.frame_jugador, text="Plantarse", command=self.turno_computadora)
        self.boton_plantarse.pack()

    def pedir_carta(self):
        self.juego.jugador_pedir_carta()
        valor_jugador = self.juego.calcular_valor_mano(self.juego.mano_jugador)
        self.etiqueta_jugador.config(text=f"Mano del Jugador: ({valor_jugador})")
        if valor_jugador >= 21:
            self.boton_plantarse.config(state=tk.DISABLED)
            self.turno_computadora()

    def turno_computadora(self):
        self.boton_pedir_carta.config(state=tk.DISABLED)
        self.boton_plantarse.config(state=tk.DISABLED)
        self.juego.turno_computadora()
        self.actualizar_pantalla()
        self.determinar_ganador()

    def actualizar_pantalla(self):
        valor_computadora = self.juego.calcular_valor_mano(self.juego.mano_computadora)
        self.pantalla.config(text=f"Mano de la Computadora: {self.juego.mano_computadora} ({valor_computadora})")

    def determinar_ganador(self):
        valor_jugador = self.juego.calcular_valor_mano(self.juego.mano_jugador)
        valor_computadora = self.juego.calcular_valor_mano(self.juego.mano_computadora)
        
        if valor_jugador > 21 and valor_computadora > 21:
            resultado = "¡Es un empate!"
        elif valor_jugador > 21:
            resultado = "¡La computadora gana! El jugador se pasó de 21."
        elif valor_computadora > 21:
            resultado = "¡El jugador gana! La computadora se pasó de 21."
        elif valor_jugador > valor_computadora:
            resultado = "¡El jugador gana!"
        elif valor_jugador < valor_computadora:
            resultado = "¡La computadora gana!"
        else: 
            resultado = "¡Es un empate!"
        etiqueta_resultado = tk.Label(self.root, text=resultado)
        etiqueta_resultado.pack()