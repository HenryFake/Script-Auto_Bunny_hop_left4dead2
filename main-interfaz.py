#!/usr/bin/env python3
# Auto Bunny Hop para Left 4 Dead 2
# Autor: Henry Callupe
# Licencia: MIT

import time
import pyautogui
import winsound
import tkinter as tk
from threading import Thread
import keyboard

# Configuración editable
config = {
    'x': 2512, # Coordenada X del píxel objetivo
    'y': 1281, # Coordenada Y del píxel objetivo
    'tecla_activacion': 'space', # Tecla para activar o desactivar el script
    'color_objetivo': (255, 255, 255),
    'sonido_salto': (440, 10),
    'sonido_toggle': (440, 500),
}

script_habilitado = True

def press_space():
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')
    winsound.Beep(*config['sonido_salto']) # Comentar esta línea si se desea desactivar el sonido

def is_pixel_color(x, y, target_color):
    return pyautogui.pixelMatchesColor(x, y, target_color)

def toggle_script():
    global script_habilitado
    script_habilitado = not script_habilitado
    btn_toggle.config(text="Deshabilitar" if script_habilitado else "Habilitar")
    winsound.Beep(*config['sonido_toggle'])
    print("Script habilitado." if script_habilitado else "Script deshabilitado.")

def check_pixel():
    while True:
        if script_habilitado and is_pixel_color(config['x'], config['y'], config['color_objetivo']):
            press_space()

ventana = tk.Tk()
ventana.title("Control del Script")
ventana.geometry("300x150")

def cambiar_estado():
    toggle_script()

btn_toggle = tk.Button(ventana, text="Deshabilitar", command=cambiar_estado)
btn_toggle.pack(pady=50)

ventana.bind(f"<{config['tecla_activacion']}>", lambda event: cambiar_estado())

Thread(target=check_pixel, daemon=True).start()

ventana.mainloop()
