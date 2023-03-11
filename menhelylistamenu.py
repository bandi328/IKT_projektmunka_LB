import os

def menu(menulista):
    os.system('cls')
    for i in range(len(menulista)):
        print(f"{i+1}. {menulista[i]}")
    print("")
    print("0. Kilépés")

    valasztas = input(f"\nVálasztás: (0...{len(menulista)}): ")
    while len(valasztas) != 1 or "0" > valasztas or "5" < valasztas:
        valasztas = input(f"\nVálasztás: (0...{len(menulista)}): ")
    os.system('cls')
    return int(valasztas)