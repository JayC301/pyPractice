import ctypes
import sys
import os
import keyboard
import time


class Soldier:
    def __init__(self, name, health, mana, speed, basicDamage):
        self.name = name
        self.health = health
        self.mana = mana
        self.speed = speed
        self.basicDamage = basicDamage
    
    def displayInfo(self):
        centralizedText(f"I am {self.name}, {self.health} HP, {self.mana} MP, {self.speed} speed, {self.basicDamage} damage")

def centralizedText(text):
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    if isinstance(text, list):
        center = (terminal_height - len(text)*2)//2
        print('\n'*center)
        for i in text:
            # Calculate the number of spaces needed to center the text
            padding = (terminal_width - len(i)) // 2
            # Print the text with padding
            print(" " * padding + i + '\n')

    elif isinstance(text, str):
        center = terminal_height//2
        print('\n'*center)
        padding = (terminal_width - len(text))//2
        print(" "*padding + text)

def centralizedInput(val, Hcenter=True):
    terminal_width = os.get_terminal_size().columns
    terminal_height = os.get_terminal_size().lines
    if Hcenter:
        center = terminal_height//2
        print('\n'*center)
    padding = (terminal_width - len(val))//2
    print(" " * padding + val)
    ans = input(" "*(padding))
    os.system('cls')
    return ans

def displayMainMenu():
    display =["Welcome To The Town", "A: Start Game", "L: Load Game", "S: Quit"]
    centralizedText(display)

def weaponList(displayWeapon=False, idx =-1):
    weapon = ["sword", "knife", "spear", "knuckles", "long axe"]
    if idx>=0:
        return weapon[idx]
    if displayWeapon:
        centralizedText(weapon)

def maximizedWindow():
    # To maximize the window
    user32 = ctypes.WinDLL('user32')
    SW_MAXIMISE = 3
    hWnd = user32.GetForegroundWindow()
    user32.ShowWindow(hWnd, SW_MAXIMISE)


# maximizedWindow()
# time.sleep(0.5)

# os.system('cls')
# displayMainMenu()

# while True:
#     if keyboard.read_key()=='a':
#         os.system('cls')
#         soldierInfo = [] 
#         weaponList(True)
#         soldierInfo.append(centralizedInput("Choose your weapon: ", False))
#         soldierInfo.append(centralizedInput("Name your soldier: "))
#         armyA = Soldier(soldierInfo[1], 100, 120, 3, 15)
#         armyA.displayInfo()

#     elif keyboard.read_key()=='l':
#         pass
    
#     elif keyboard.read_key()=='q':
#         sys.exit()




    
