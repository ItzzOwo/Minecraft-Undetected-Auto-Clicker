from pynput.mouse import Button, Controller
import random
import keyboard
import threading
z = input("Enter a keybind: ")
mouse = Controller()
while True:
    while keyboard.is_pressed(z):
        event = threading.Event()
        event.wait(random.uniform(0.095614621967175,0.085614621967175))
        x = 2 if random.random() < 0.64 else 1
        mouse.click(Button.left, x)
