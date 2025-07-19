#!/usr/bin/env python3
# Auto Bunny Hop para Left 4 Dead 2
# Autor: Henry Callupe
# Licencia: MIT

import os
import keyboard
import time
import psutil
import pyautogui
import winsound

# Configuración del script
config = {
    'x': 1883,  # Coordenada X del píxel objetivo # 1920 x 1080
    'y': 965,  # Coordenada Y del píxel objetivo # 1920 x 1080
    'tecla': 'n', # Tecla para activar el salto automático
    'color_objetivo': (255, 255, 255) # Color del píxel objetivo (blanco)
}

psutil.Process(os.getpid()).nice(psutil.HIGH_PRIORITY_CLASS)

def press_space():
    keyboard.press('space')
    time.sleep(0.1)
    keyboard.release('space')
    
    winsound.Beep(440, 100) # Comentar esta línea si se desea desactivar el sonido

def is_pixel_color(x, y, target_color):
    return pyautogui.pixelMatchesColor(x, y, target_color)

print(' - - - - Iniciado - - - -')
while True:
    if is_pixel_color(config['x'], config['y'], config['color_objetivo']):
        if keyboard.is_pressed(config['tecla']):
            press_space()
