import os

def menu(menulista):
    os.system('cls')
    for i in range(len(menulista)):
        print(f"{i+1}. {menulista[i]}")
    print("")
    print("0. Kilép")
    
    valasztas = input(f"Választás: (0...{len(menulista)}): ")
    while len(valasztas) !=1 or "0" > valasztas or "6" < valasztas:
        valasztas = input(f"Választás: (0...{len(menulista)}): ")
    os.system('cls')
    return int(valasztas)