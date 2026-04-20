import json
import random

def ladda_highscore():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return None

def spara_highscore(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def spela():
    hemligt_tal = random.randint(1, 100)
    antal = 0
    while True:
        gissa = int(input("Gissa: "))
        antal += 1
        if gissa < hemligt_tal:
            print("För lågt!")
        elif gissa > hemligt_tal:
            print("För högt!")
        else:
            print(f"Rätt! {antal} gissningar.")
            return antal


def visa_meny():
    print("--- HÖGT/LÅGT ---")
    print("1. Spela ny omgång")
    print("2. Visa highscore")
    print("3. Avsluta")


def visa_highscore():
    highscores = ladda_highscore()
    if not highscores:
        print("Inga resultat ännu")
        return

    # Sortera (minst antal gissningar först)
    sorterad = sorted(highscores, key=lambda x: x[" gissningar "])
    print("--- HIGHSCORE ---")
    for spelare in sorterad:
        print(f"{spelare[' namn ']} ({spelare[' gissningar ']})")


def add_spelare(namn, antal):
    spelare = {}
    spelare[" namn "] = namn
    spelare[" gissningar "] = antal
    highscore = ladda_highscore()
    if highscore is None:
        highscore = []
    highscore.append(spelare)
    spara_highscore(highscore)


while True:
    visa_meny()
    val = input("Val: ")
    print("Du valde:", val)

    if val == "1":
        namn = input("Ange ditt namn: ")
        antal = spela()
        add_spelare(namn, antal)
    elif val == "2":
        visa_highscore()
    elif val == "3":
        print("Hejdå!")
        break
    else:
        print("Ogiltigt val")
