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
def Kutyaadatmod(kutyak):
    menupontok = ["Név", "Termet", "Ivartalanítás", "Státusz"]
    nev = input("Adja meg a kutya nevét: ")
    for kutya in kutyak:
        if kutya.nev == nev:
            print("Válasszon módosítandó adatot:")
            valasztas = menu(menupontok)
            while valasztas != 0:
                if valasztas == 1:
                    kutya.nev = input("Adja meg az új nevet: ")
                elif valasztas == 2:
                    kutya.termet = TermetBeker()
                elif valasztas == 3:
                    kutya.ivar = IvarBeker()
                elif valasztas == 4:
                    kutya.statusz = StatuszBeker()
                valasztas = menu(menupontok)
            break
        else:
            print("Nem található a megadott névnek megfelelő vizsgázó!")

# 2. választás
def TermetBeker():
    lehetsegesTermet = ['kicsi', 'közepes', 'nagy']
    for i in range(len(lehetsegesTermet)):
        print(f"{i+1}. {lehetsegesTermet[i]}")
    valasztas = "ab"
    while '0' > valasztas or '3' < valasztas:
        valasztas = input("Adja meg a típus számát [1-3]: ")
    return lehetsegesTermet[int(valasztas)-1]    

# 3. választás
def IvarBeker():
    amiszeretne = input("Ivartalaanítva lett a kutya[Igen/Nem]:")
    ivar = "ab"
    if amiszeretne == "Igen":
        ivar = "Igen"
    return ivar

# 4. választás
# def StatuszBeker():


    
# 4. Menupont
