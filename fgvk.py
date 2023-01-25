from menu import menu
import os

# MENUPONTOK
def Listamenu():
    menupontok2 = ["Fajta szerint", "Születési év szerint", "Termet szerint", "Nem szerint", "Ivartalanitás szerint", "Státusz szerint"]
    valasztas = menu(menupontok2)
    while valasztas != 0:
        if valasztas == 1:
            print("Kutyuska1")
        elif valasztas == 2:
            print("Kutyuska2")
        elif valasztas == 3:
            print("Kutyuska3")
        elif valasztas == 4:
            print("Kutyuska4")
        elif valasztas == 5:
            print("Kutyuska5")
        valasztas = menu(menupontok2)


# 6. MENUPONT
def Adomanykezeles():
    adomany = 30000
    print(f"Jelenlegi egyenleg: {adomany}")
    kerdes = input("Szeretne új adományt rögzíteni? (Igen/Nem): ")
    if kerdes == "igen":
        ujadomany = int(input("Adja meg az összeget: "))
        adomany += ujadomany
        print(f"Új egyenleg: {adomany}")
    else:
        print(f"Az egyenleg:{adomany}")

# 5.MENUPONT
def Kutyaadatmod():
    print("Lehetőségek:\n1. Ivartalanítása:1\n 2.Státusza:2")
    # kivansag = input("Melyik adatot szeretné módosítani:")
    # if kivansag == "1":
    #     # ide kell egy fajlba iras!!!!
    # else:
    #     # ide kell meg egy fajlba iras

# 4. Menupont
