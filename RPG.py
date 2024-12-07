import random
import tkinter as tk
from PIL import Image, ImageTk
import time
root = 0
def siac(image_path, display_time_ms=5000): #Siac function
    root = tk.Tk() #New Tkinter window
    image = Image.open(image_path)
    photo = ImageTk.PhotoImage(image) #Convert Into Photo
    label = tk.Label(root, image=photo)
    label.pack()
    root.after(display_time_ms, root.destroy)
    root.mainloop()
def close_window():
    root.destroy()
siac("H:/Python/Empty/PythonDownload/Title.png", 3400) #End Of Intro
Gate = 1
while Gate == 1: #GamePrep
    input("Press any key to start")
    Gate = 0
Name = input("Name your character:  ")
Attack = ["Gnostic Pray","Blasphemy","Sacrifice"]
Things = ["Pierog𐤀","Apple Of Eden𐤀","Apple𐤀","Bottle Of Mud𐤀","Wooden Spatula"]
Hat = ["Straw Hat(A)","Cap Of Hope(A)","Hellas Necklace(A)"]
PossibleAttacks = ["Finger Snap","Morallity Check","Preach Of Babel"]
FreezerThings = ["Ice Cold Energy Drink𐤀","Ice Cube𐤀"]
InShop = ["Straw Hat(A)(40)","Apple𐤀(O","Nagorna Relic(49)","Platinum Template(26)"]
Str = 1
Gate = 1
Region = 1
eHp = 0
eStr = 0
ψ = 0
Ազ = 0
Current = 0
Roulette = 0
Action = 0
lulu = 0
TemporaryStr = 0
AttackExe = 0
HpChange = 0
RandomAttEffect = 0
EnemyConditions = []
Items = []
PlayerLVL = random.choice([1,2,3])
if PlayerLVL == 1:
    Attack.pop(1)
    Attack.pop(1)
elif PlayerLVL == 2:
    Attack.pop(2)
Attack.append("Low Kick")
PlHP = 11 + PlayerLVL
print(Name,"starts with level",PlayerLVL) #EndGamePrep
EnemyList = [1,2,3,4,5] #,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
def fof(Gate, Things, Items, EnemyList, eHp, eStr): #Fof- Fight Or Flight (Attack or Open Inventory function)
    while Gate == 1:
        Action = input("Available Actions: Open Inventory (1), Move (2)  ")
        if (Action == "1") or (Action == "Open Inventory"):
            if len(Items) == 0:
                print("Your inventory is empty")
        elif (Action == "2") or (Action == "Move"):
            print("...")
            time.sleep(2)
            Gate = 0
            Roulette = 0
            Roulette = random.choice([0,1,2,3,4])
            if Roulette == 0:
                Current = random.sample(Things)
                Items.append(Current)
                print("You found",Current,)
            elif Roulette == 1:
                print("You find a traveller!")
                if Ազ > 0:
                    print(random.sample(Things, 3))
                else:
                    print("But you have no money anyway (Ազ)..")
            else:
                encountere(Roulette, Current, Items, EnemyConditions, eHp, eStr, Gate)

def encountere(Roulette, Current, Items, EnemyConditions, eHp, eStr, Gate): #Encountere- Enemy encounter machine
    Roulette = random.choice(EnemyList)
    if Roulette == 0:
        print("You encounter a Kappa!")
        siac("H:/Python/Empty/PythonDownload/Kappa.png", 3400)
        eHp = 32
        eStr = 4
    elif Roulette == 1:
        print("You encounter a Crow!")
        siac("H:/Python/Empty/PythonDownload/Crow.png", 3400)
        eHp = 15
        eStr = 2
        EnemyConditions.append("Loot")
    elif Roulette == 2:
        print("You encounter a Soldier Of Baku!")
        siac("H:/Python/Empty/PythonDownload/SoldierBaku.png", 3400)
        eHp = 42
        eStr = random.choice([4,5,6])
    elif Roulette == 3:
        print("You encounter a Dart Frog!")
        siac("H:/Python/Empty/PythonDownload/DartFrog.png", 3400)
        eHp = 22
        eStr = random.choice([4,5,6])
        if random.choice([1,2]) == 1:
            EnemyConditions.append("Poisonous")
        if random.choice([1,2]) == 1:
            EnemyConditions.append("ConfusionAble")
    Gate = 4
while not Gate == 4:
    fof(Gate, Things, Items, EnemyList, eHp, eStr)
    Gate = 4
Gate = 4
while Gate != 2:
    Combat(Action, Items, lulu, Attack, AttackExe, RandomAttEffect, PlHP, HpChange, Current, TemporaryStr)

def Combat(Action, Items, lulu, Attack, AttackExe, RandomAttEffect, PlHP, HpChange, Current, TemporaryStr): #Combat Function
    Gate = 4
    Action = input("Available Actions: Open Inventory (1), Attack (2), Escape (3)")
    if (Action == "3") or (Action == "Escape"):
        if random.choice([1,2,3,4]) == 3:
            print("You succesfully escaped the enemy!")
    elif (Action == "1") or (Action == "Open Inventory"):
        if len(Items) == 0:
            print("Your inventory is empty")
        else:
            print("Inventory: ",Items)
            for lulu in Items:
                if "𐤀" in lulu:
                    print("You have some usable items (" ,lulu, ") in your inventory")
                else:
                    print("You have no usable items (𐤀)")
    elif (Action == "2") or (Action == "Attack"):
        print("Available attacks:")
        Counter = 0
        while Counter < len(Attack):  
            print(Attack[Counter], Counter)
            Counter += 1
        while AttackExe != lulu:
            lulu = input("Use attack? (Number or name)")
            AttackExe = (lulu[:-1])
            if AttackExe == ("Gnostic Pray"):
                print("You pray..")
                time.sleep(2)
                RandomAttEffect = random.choice([0,1,2])
                if RandomAttEffect == 0:
                    eHp = eHp - random.choice([1,2])
                    print("The enemy's wounds are expanding..")
                elif RandomAttEffect == 1:
                    HpChange = random.choice([1,2,3,4])
                    PlHP = PlHP + HpChange
                    print("You are were healed by ",HpChange, "!")
                elif RandomAttEffect == 2:
                    print("An item descends from the above!")
                    Current = random.sample(Things)
                    Items.append(Current)
                    print("You obtain ",Current)
            elif AttackExe == ("Low Kick"):
                print("You kick the enemy!")
                eHp = eHp - (Str + 2 + TemporaryStr)
            elif AttackExe == ("Sacrifice"):
                if Items < 1:
                    print("You have nothing to sacrifice except yourself..")
                    PlHP = PlHP - random.choice([2,3])
                    TemporaryStr = TemporaryStr + 1
                else:
                    while Gate = 4:
                        print("Sacrifial items:",Items)
