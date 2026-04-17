import json

def ladda_highscore():
    try:
        with open("data.json", "r") as f:
            return json.load(f)
    

def spara_highscore(data):
    with open("data.json", "w") as f:
        json.dump(data, f, indent=4)

def visa_meny():
    print("--- HÖGT/LÅGT ---")
    print("1. Spela ny omgång")
    print("2. Visa highscore")
    print("3. Avsluta")


visa_meny()
val = input("Val: ")
print("Du valde:", val)

def visa_highscore():
    highscores = [
        {"namn": "Erik", "gissningar": 2},
        {"namn": "Anna", "gissningar": 3},
        {"namn": "Sara", "gissningar": 5}
    ]

    if not highscores:
        print("Inga resultat ännu")
        return

    # Sortera (minst antal gissningar först)
    highscores.sort(key=lambda x: x["gissningar"])

    print("--- HIGHSCORE ---")
    for i, spelare in enumerate(highscores, start=1):
        print(f"{i}. {spelare['namn']} - {spelare['gissningar']} gissningar")

data = ladda_highscore()
print(data)