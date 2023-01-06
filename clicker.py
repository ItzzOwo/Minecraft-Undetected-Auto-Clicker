from pynput.mouse import Button, Controller
import random
import keyboard
import threading

print("░█████╗░░██╗░░░░░░░██╗░█████╗░  ░█████╗░██╗░░░░░██╗░█████╗░██╗░░██╗███████╗██████╗░")
print("██╔══██╗░██║░░██╗░░██║██╔══██╗  ██╔══██╗██║░░░░░██║██╔══██╗██║░██╔╝██╔════╝██╔══██╗")
print("██║░░██║░╚██╗████╗██╔╝██║░░██║  ██║░░╚═╝██║░░░░░██║██║░░╚═╝█████═╝░█████╗░░██████╔╝")
print("██║░░██║░░████╔═████║░██║░░██║  ██║░░██╗██║░░░░░██║██║░░██╗██╔═██╗░██╔══╝░░██╔══██╗")
print("╚█████╔╝░░╚██╔╝░╚██╔╝░╚█████╔╝  ╚█████╔╝███████╗██║╚█████╔╝██║░╚██╗███████╗██║░░██║")
print("░╚════╝░░░░╚═╝░░░╚═╝░░░╚════╝░  ░╚════╝░╚══════╝╚═╝░╚════╝░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝")
print("")
print("Burst click - 20 CPS Drag Click for not getting kicked/banned while taking similar knockback to drag clicking")
print("Drag click - Faster version at burst clicking for reducing servers")
print("Butterfly - Butterfly clicker with randomized double clicks (Ability to change chance) and realistic clicking patterns")
print("Jitter - Jitter clicker with realistic start patterns and consistent clicks to maximize taking less knockback")
print("")
z = input("Enter a keybind: ")
y = input("Enter keybind to restart program: ")


def main():
                event = threading.Event()
                def burst():
                            burst_randint = 2
                            burst_randint_v2 = 5
                            burst_slow_down = random.randint(200,300)
                            burst_clicks = 0
                            if burst_clicks == burst_slow_down:
                                burst_randint +=1
                                burst_randint_v2 +=1
                                burst_clicks = 0
                            delay_ver_1 = delay - 0.015
                            delay_ver_2 = delay + 0.015
                            mouse = Controller()
                            random_start = random.randint(burst_randint,burst_randint_v2)
                            click_amount = 0
                            click_stop = random.randint(12,16)
                            clicks = 0
                            while True:
                                for clicks in range(random_start):
                                    while keyboard.is_pressed(z):
                                            mouse.click(Button.left, 1)
                                            event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                            clicks +=1
                                            if clicks == random_start:
                                                while keyboard.is_pressed(z):
                                                    delay_ver_1 = delay - 0.003
                                                    delay_ver_2 = delay + 0.003
                                                    event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                                    mouse.click(Button.left, 1)
                                                    click_amount +=1
                                                    burst_clicks +=1
                                                    if click_amount == click_stop:
                                                        wait = random.uniform(0.3,0.6)
                                                        event.wait(wait)
                                                        burst()
                                                    else:
                                                        pass
                                                if keyboard.is_pressed(y):
                                                        main()
                                            else:
                                                pass
                def drag():
                            drag_randint = 10
                            drag_randint_v2 = 15
                            drag_slow_down = random.randint(600,900)
                            drag_clicks = 0
                            if drag_clicks == drag_slow_down:
                                drag_randint +=1
                                drag_randint_v2 +=1
                                drag_clicks = 0
                            delay_ver_1 = delay - 0.005
                            delay_ver_2 = delay + 0.005
                            mouse = Controller()
                            random_start = random.randint(drag_randint,drag_randint_v2)
                            click_amount = 0
                            click_stop = random.randint(30,45)
                            clicks = 0
                            while True:
                                for clicks in range(random_start):
                                    while keyboard.is_pressed(z):
                                            mouse.click(Button.left, 1)
                                            event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                            clicks +=1
                                            if clicks == random_start:
                                                while keyboard.is_pressed(z):
                                                    delay_ver_1 = delay - 0.003
                                                    delay_ver_2 = delay + 0.003
                                                    event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                                    mouse.click(Button.left, 1)
                                                    click_amount +=1
                                                    drag_clicks +=1
                                                    if click_amount == click_stop:
                                                        wait = random.uniform(0.3,0.6)
                                                        event.wait(wait)
                                                        drag()
                                                    else:
                                                        pass
                                                if keyboard.is_pressed(y):
                                                        main()
                                            else:
                                                pass
                def butterfly():
                            delay_ver_1 = delay - 0.015
                            delay_ver_2 = delay + 0.055
                            butterfly_stop = random.randint(6,10)
                            clicks = 0
                            mouse = Controller()
                            random_start = random.randint(2,4)
                            while True:
                                for clicks in range(random_start):
                                    while keyboard.is_pressed(z):
                                        x = 2 if random.random() > chance else 1
                                        event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                        if x == 2:
                                            mouse.click(Button.left, 1)
                                            event.wait(random.uniform(0.003,0.009))
                                            mouse.click(Button.left, 1)
                                            clicks +=2
                                        else:
                                            mouse.click(Button.left, 1)
                                            clicks +=1
                                    if clicks == butterfly_stop:
                                        while keyboard.is_pressed(z):
                                            delay_ver_1 = delay - 0.010
                                            delay_ver_2 = delay + 0.010
                                            x = 2 if random.random() > chance else 1
                                            event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                            if x == 2:
                                                mouse.click(Button.left, 1)
                                                event.wait(random.uniform(0.003,0.009))
                                                mouse.click(Button.left, 1)
                                                clicks = 0
                                            else:
                                                mouse.click(Button.left, 1)
                                                clicks = 0
                                        if keyboard.is_pressed(y):
                                            main()
                                    else:
                                        pass
                                    if keyboard.is_pressed(y):
                                        main()
                def jitter():
                        delay_ver_1 = delay - 0.012
                        delay_ver_2 = delay + 0.012
                        jitter_stop = random.randint(6,10)
                        clicks = 0
                        mouse = Controller()
                        random_start = random.randint(3,6)
                        while True:
                            for clicks in range(random_start):
                                while keyboard.is_pressed(z):
                                    mouse.click(Button.left, 1)
                                    event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                    clicks +=1
                                if clicks == jitter_stop:
                                    while keyboard.is_pressed(z):
                                            delay_ver_1 = delay - 0.005
                                            delay_ver_2 = delay + 0.005
                                            event.wait(random.uniform(delay_ver_1,delay_ver_2))
                                            mouse.click(Button.left, 1)
                                            clicks = 0
                                    if keyboard.is_pressed(y):
                                            main()
                                else:
                                    pass
                                if keyboard.is_pressed(y):
                                    main()
                method = input("Enter clicking method (jitter/butterfly/drag click/burst click): ")
                if method == "jitter":
                        delay = float(input("Enter click delay (Recommended 75ms): "))
                        delay = delay/1000
                        mouse = Controller()
                        jitter()
                elif method == "butterfly":
                        delay = float(input("Enter click delay (Recommended 55ms): "))
                        delay = delay/1000
                        chance = int(input("Enter double click chance (Recommended 64): "))
                        chance = chance/100
                        butterfly()
                elif method == "drag click":
                        delay = float(input("Enter click delay (Recommended 5ms): "))
                        delay = delay/1000
                        drag()
                elif method == "burst click":
                        delay = float(input("Enter click delay (Recommended 7ms): "))
                        delay = delay/1000
                        burst()
                else:
                        print("Invalid clicking method!")
                        main()

main()
