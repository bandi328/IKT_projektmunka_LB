from menu import menu
from Kutya import *
from Ember import *
import os
import re

# FÁJLOLVASÁSOK
def FajlOlvasKutya(kutyak):
    f = open("kutyak.txt", "r", encoding="utf-8")
    for sor in f:
        egyKutya = Kutya(sor)
        kutyak.append(egyKutya)
    f.close()

def FajlOlvasEmber(emberek):
    f = open("ember.txt", "r", encoding="utf-8")
    for sor in f:
        egyEmber = Ember(sor)
        emberek.append(egyEmber)
    f.close()

def FajlOlvasAdomany():
    adomany = 0
    f = open("adomany.txt", "r", encoding="utf-8")
    for sor in f:
        adomany = sor
    f.close()
    return adomany

# 1. MENUPONT
regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
def checkEmail():
    email = input("\tEmail cím: ")
    if(re.fullmatch(regexEmail, email)):
        return email
    else:
        checkEmail()
def checkTel():
    tel = input("\tTelefonszám: ")
    if len(tel) == 11 and tel.isnumeric():
        return tel
    else:
        checkTel()

def Orokbefogadas(kutyak, emberek, osszeg):
    os.system('cls')
    good = False
    allatNev = input("Adja meg az örökbefogadni kívánt kutya nevét: ")

    while not good:
        allatNev = input("Adja meg az örökbefogadni kívánt kutya nevét: ")
        for kutya in kutyak:
            if allatNev == kutya.nev:
                good = True
    
    print("Adja meg adatait!")
    emberNev = input("\tTeljes név: ")
    tel = checkTel()
    email = checkEmail()
    lakcim = input("\tLakcím: ")

    f = open("ember.txt", "a", encoding="utf-8")
    f.write(f"{allatNev};{emberNev};{tel};{email};{lakcim}\n")
    f.close()
    print("A kutya felvétele sikeres volt!")


# 2. MENUPONT
def Listamenu(kutyak):
    menupontok2 = ["Fajta szerint", "Születési év szerint", "Termet szerint", "Nem szerint", "Ivartalanitás szerint", "Státusz szerint"]
    valasztas = menu(menupontok2)
    while valasztas != 0:
        if valasztas == 1:
            fajta = input("Adja meg a kutyák fajtáját:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.fajta == fajta:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
        elif valasztas == 2:
            szulinap = int(input("Adja meg a kutya születési évét:"))
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.szuletes == szulinap:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
        elif valasztas == 3:
            termet = input("Adja meg a kutya termetét[nagy/közepes/kicsi]:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.termet == termet:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
        elif valasztas == 4:
            nem = input("Adja meg a kutya nemét[lány/fiú]:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.nem == nem:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
        elif valasztas == 5:
            ivar = input("Adja meg a kutya ivartalanítva van-e[Igen/Nem]:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.ivar == ivar:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")   
        valasztas = menu(menupontok2)


# 3. MENUPONT
def KutyaFelvetel(kutyak):
    inp = input("Szeretne új kutyát felvenni[Igen/Nem]:")
    if inp == "Igen":
        neve = input("Adja meg a kutya nevét:")
        szuletes = input("Adja meg a kutya születési évét:")
        fajta = input("Adja meg a kutya fajtáját:")
        termet = input("Adja meg a kuya termetét:")
        neme = input("Adja meg a kutya nemét:")
        ivar = input("Ivartalanított a kutya?[igen/nem]:")
        statusz = input("Mi a státusza?[lakos/fogalalt/örökbeadott]")
    f = open("kutyak.txt", "a", encoding="utf-8")
    f.write(f"{neve};{szuletes};{fajta};{termet};{neme};{ivar};{statusz}\n")
    print("A kutya felvétele sikeres volt!")
    f.close()


# 4. MENUPONT
def KutyaLefoglalas(kutyak, emberek, osszeg):
    inp = input("Szeretne lefoglalni egy kutyát? [Igen/Nem]: ")
    if inp == "Igen":
        kutyanev = input("Adja meg a kutya nevét:")
        for kutya in kutyak:
            if kutya.nev == kutyanev:
                kutya.statusz = "foglalt"
                print(f"A kutya státusza vátoztatva lett {kutya.statusz}ra.")
    else:
        print("Nem változtatta meg a kutya státuszát.")
    FajlIras(kutyak, emberek, osszeg)


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
def StatuszBeker():
    lehetsegesStatusz = ['lakos','foglalt', "örökbeadott"]
    for i in range(len(lehetsegesStatusz)):
        print(f"{i+1}. {lehetsegesStatusz[i]}")
    valasztas = "ab"
    while '0' > valasztas or '3' < valasztas:
        valasztas = input("Adja meg a típus számát [1-3]: ")
    return lehetsegesStatusz[int(valasztas)-1]  

# 6. MENUPONT
def Adomanykezeles(kutyak, emberek, osszeg):
    szam = int(osszeg)
    print(f"Jelenlegi egyenleg: {szam}")
    kerdes = input("Szeretné kezelni az adományokat? (Igen/Nem): ")
    while kerdes.lower() != "igen" and kerdes.lower() != "nem":
        print("Kérem válasszon a lehetőségek közül!")
        kerdes = input("Szeretné kezelni az adományokat? (Igen/Nem): ")
    if kerdes.lower() == "igen":
        inp = input("Mit szeretne tenni? [+(adomány hozzá adása)/-(költés feljegyzése)]: ")
        while inp != "+" and inp != "-":
            print("Kérem válasszon a lehetőségek közül!")
            inp = input("Mit szeretne tenni? [+(adomány hozzá adása)/-(költés feljegyzése)]: ")
        if inp == "+":
            koltseg = input("Adja meg a költség összegét:")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg a költség összegét:")
            szam += int(koltseg)
            print(f"Az új egyenleg: {szam}")
        else:
            koltseg = input("Adja meg a költség összegét:")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg a költség összegét:")
            szam -= int(koltseg)
            print(f"Az új egyenleg: {szam}")
    else:
        print("Az egyenleg nem változott!")



# fájlÍrás
def FajlIras(kutyak, emberek, osszeg):
    f = open("kutyak.txt", "w", encoding="utf-8")
    for kutya in kutyak:
        f.write(f"{kutya.nev};{kutya.szuletes};{kutya.fajta};{kutya.termet};{kutya.nem};{kutya.ivar};{kutya.statusz}\n")
    f.close()

    f = open("ember.txt", "w", encoding="utf-8")
    for ember in emberek:
        f.write(f"{ember.kutyanev};{ember.nev};{ember.telefonszam};{ember.emailcim};{ember.lakcim}\n")
    f.close()
    
    f = open("adomany.txt", "w", encoding="utf-8")
    f.write(str(osszeg))
    f.close()