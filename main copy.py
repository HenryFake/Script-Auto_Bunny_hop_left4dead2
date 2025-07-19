#!/usr/bin/env python3
import os, psutil, keyboard, time, winsound
from mss import mss

cfg = {'x': 1883, 'y': 965, 'color': (255, 255, 255), 'tecla': 'n'}

# Prioridad alta
psutil.Process(os.getpid()).nice(psutil.HIGH_PRIORITY_CLASS)

sct = mss()
mon = {'top': cfg['y'], 'left': cfg['x'], 'width': 1, 'height': 1}

def press_space():
    keyboard.press('space')
    time.sleep(0.05)         # más corto
    keyboard.release('space')

print("‑‑ Iniciado (prioridad alta, mss) ‑‑")
while True:
    if keyboard.is_pressed(cfg['tecla']):
        px = sct.grab(mon).pixel(0, 0)  # (R, G, B, A)
        if px[:3] == cfg['color']:
            press_space()
