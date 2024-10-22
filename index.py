import tkinter as tk
from tkinter import messagebox

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Tic-Tac-Toe con IA")

# Variables del juego
jugador = "O"  # El jugador humano es 'O'
tablero = [['' for _ in range(3)] for _ in range(3)]  # Tablero vacío

# Función para comprobar si hay un ganador
def comprobar_ganador():
    # Comprobar filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2] != '':
            return fila[0]
    # Comprobar columnas
    for col in range(3):
        if tablero[0][col] == tablero[1][col] == tablero[2][col] != '':
            return tablero[0][col]
    # Comprobar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] != '':
        return tablero[0][0]
    if tablero[0][2] == tablero[1][1] == tablero[2][0] != '':
        return tablero[0][2]
    # Comprobar si hay empate
    if all(tablero[fila][col] != '' for fila in range(3) for col in range(3)):
        return "Empate"
    return None

# Función Minimax para la IA
def minimax(tablero, es_IA):
    resultado = comprobar_ganador()
    if resultado == 'X':  # IA gana
        return 1
    elif resultado == 'O':  # Jugador gana
        return -1
    elif resultado == "Empate":  # Empate
        return 0

    if es_IA:
        mejor_puntaje = -float('inf')
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == '':
                    tablero[fila][col] = 'X'
                    puntaje = minimax(tablero, False)
                    tablero[fila][col] = ''
                    mejor_puntaje = max(mejor_puntaje, puntaje)
        return mejor_puntaje
    else:
        mejor_puntaje = float('inf')
        for fila in range(3):
            for col in range(3):
                if tablero[fila][col] == '':
                    tablero[fila][col] = 'O'
                    puntaje = minimax(tablero, True)
                    tablero[fila][col] = ''
                    mejor_puntaje = min(mejor_puntaje, puntaje)
        return mejor_puntaje

# Función para encontrar la mejor jugada de la IA
def mejor_jugada():
    mejor_puntaje = -float('inf')
    mejor_movimiento = None
    for fila in range(3):
        for col in range(3):
            if tablero[fila][col] == '':
                tablero[fila][col] = 'X'
                puntaje = minimax(tablero, False)
                tablero[fila][col] = ''
                if puntaje > mejor_puntaje:
                    mejor_puntaje = puntaje
                    mejor_movimiento = (fila, col)
    return mejor_movimiento

# Función para manejar los clics del jugador
def manejar_click(fila, col):
    global jugador
    if tablero[fila][col] == '' and comprobar_ganador() is None:
        # Marcar el movimiento del jugador
        tablero[fila][col] = jugador
        botones[fila][col].config(text=jugador)

        # Comprobar si el jugador ganó
        ganador = comprobar_ganador()
        if ganador:
            finalizar_juego(ganador)
            return

        # Turno de la IA
        movimiento_ia = mejor_jugada()
        if movimiento_ia:
            fila_ia, col_ia = movimiento_ia
            tablero[fila_ia][col_ia] = 'X'
            botones[fila_ia][col_ia].config(text='X')

        # Comprobar si la IA ganó
        ganador = comprobar_ganador()
        if ganador:
            finalizar_juego(ganador)

# Función para finalizar el juego
def finalizar_juego(ganador):
    if ganador == "Empate":
        messagebox.showinfo("Fin del juego", "¡Es un empate!")
    else:
        messagebox.showinfo("Fin del juego", f"¡El ganador es {ganador}!")
    reiniciar_juego()

# Función para reiniciar el juego
def reiniciar_juego():
    global tablero
    tablero = [['' for _ in range(3)] for _ in range(3)]
    for fila in range(3):
        for col in range(3):
            botones[fila][col].config(text='', state=tk.NORMAL)

# Crear botones para el tablero
botones = [[None for _ in range(3)] for _ in range(3)]
for fila in range(3):
    for col in range(3):
        botones[fila][col] = tk.Button(ventana, text="", width=10, height=3,
                                        font=("Arial", 24),
                                        command=lambda f=fila, c=col: manejar_click(f, c))
        botones[fila][col].grid(row=fila, column=col)

# Ejecutar la ventana
ventana.mainloop()
