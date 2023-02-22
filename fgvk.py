from menu import menu
from Kutya import *
from Ember import *
import time
import datetime
import os
import re
import datetime

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
        return str(email)
    else:
        checkEmail()
def checkTel():
    tel = input("\tTelefonszám: ")
    if len(tel) == 11 and tel.isnumeric():
        return tel
    else:
        checkTel()
def checkKutyaNev(kutyak):
    good = False
    while not good:
        allatNev = input("Adja meg az örökbefogadni kívánt kutya nevét: ")
        for kutya in kutyak:
            if allatNev == kutya.nev:
                good = True
    for i in range(len(kutyak)):
        if kutyak[i].nev == allatNev:
            if kutyak[i].statusz == "foglalt" or kutyak[i].statusz == "örökbeadott":
                print("A kutya nem fogadható örökbe, válasszon másik kutyát!")
                checkKutyaNev(kutyak)
            else:
                kutyak[i].statusz = "örökbeadott"
                return allatNev

def Orokbefogadas(kutyak, emberek, osszeg):
    os.system('cls')
    allatNev = checkKutyaNev(kutyak)
    print("Adja meg adatait!")
    emberNev = input("\tTeljes név: ")
    tel = checkTel()
    email = checkEmail()
    lakcim = input("\tLakcím: ")
    emberek.append(Ember(f"{allatNev};{emberNev};{tel};{email};{lakcim}"))
    FajlIras(kutyak, emberek, osszeg)
    print("A örökbefogadás sikeres volt!")


# 2. MENUPONT
def Listamenu(kutyak):
    menupontok2 = ["Fajta szerint", "Születési év szerint", "Termet szerint", "Nem szerint", "Ivartalanitás szerint", "Státusz szerint", ]
    valasztas = menu(menupontok2)
    while valasztas != 0:
        if valasztas == 1:
            fajta = input("Adja meg a kutyák fajtáját: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.fajta == fajta:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 2:
            szulinap = int(input("Adja meg a kutya születési évét: "))
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            # if szulinap.isnumeric()
            for kutya in kutyak:
                if kutya.szuletes == szulinap:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 3:
            termet = input("Adja meg a kutya termetét[nagy/közepes/kicsi]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.termet == termet:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 4:
            nem = input("Adja meg a kutya nemét[lány/fiú]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.nem == nem:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 5:
            ivar = input("Adja meg a kutya ivartalanítva van-e[Igen/Nem]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.ivar == ivar:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")   
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 6:
            statusz = input("Adja meg a kutya státuszát[lakos/foglalt/örökbeadott]:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.statusz == statusz:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")   
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)

        # INPUT CHEK 6. FAJTA LISTAZASHOZ!!!!!!!!!!


# 3. MENUPONT
def KutyaFelvetel(kutyak, emberek, osszeg):
    ma = datetime.date.today()
    ev = ma.year
    ok = False
    inp = input("Szeretne új kutyát felvenni? [Igen/Nem]: ")
    valosTermet = ["kicsi", "közepes", "nagy"]
    valosNem = ["lány", "fiú"]
    valosStatusz = ["lakos", "foglalt", "örökbeadott"]
    if inp.lower() == "igen":
        neve = input(f"\tAdja meg a kutya nevét: ")
        szuletesBeker = (input(f"\tAdja meg a kutya születési évét: "))
        while ok == False:
            if szuletesBeker.isnumeric():
                if ev-int(szuletesBeker) <= 15 and ev-int(szuletesBeker) >= 0:
                    szuletes = szuletesBeker
                    ok = True
                else:
                    szuletesBeker = input(f"\tAz évszám helytelen. Adja meg a kutya születési évét: ")
            else:
                szuletesBeker = input(f"\tAz évszám helytelen. Adja meg a kutya születési évét: ")
        fajta = input(f"\tAdja meg a kutya fajtáját: ")
        ok = False
        termet = input(f"\tAdja meg a kuya termetét: ")
        while ok == False:
            if termet in valosTermet:
                ok = True
            else:
                termet = input(f"\tAz termet helytelen. Adja meg a kuya termetét: ")
        ok = False
        neme = input(f"\tAdja meg a kutya nemét: ")
        while ok == False:
            if neme in valosNem:
                ok = True
            else:
                neme = input(f"\tA nem helytelen. Adja meg a kutya nemét: ")
        ok = False
        ivar = input(f"\tIvartalanított a kutya? [igen/nem]: ")
        while ok == False:
            if ivar.lower() == "igen":
                ok = True
            elif ivar.lower() == "nem":
                ok = True
            else:
                ivar = input(f"\tRossz adatot adott meg. Ivartalanított a kutya? [igen/nem]: ")
        ok = False
        statusz = input(f"\tMi a státusza? [lakos/foglalt/örökbeadott]: ")
        while ok == False:
            if statusz in valosStatusz:
                ok = True
            else:
                statusz = input(f"\tRossz státuszt adott meg. Mi a státusza? [lakos/foglalt/örökbeadott]: ")
    else:
        return
    kutyak.append(Kutya(f"{neve};{szuletes};{fajta};{termet};{neme};{ivar};{statusz}"))
    FajlIras(kutyak, emberek, osszeg)
    print("A kutya felvétele sikeres volt!")
    time.sleep(2)


# 4. MENUPONT
def KutyaLefoglalas(kutyak, emberek, osszeg):
    kutyanevek = []
    for nev in kutyak:
        kutyanevek.append(nev.nev)
    inp = input("Szeretne lefoglalni egy kutyát? [Igen/Nem]: ")
    while inp.lower() != "igen" and inp.lower() != "nem":
        print("Kérem adja meg helyesen!")
        inp = input("Szeretne lefoglalni egy kutyát? [Igen/Nem]: ")
    if inp.lower() == "igen":
        kutyanev = input("Adja meg a kutya nevét: ")
        while kutyanev not in kutyanevek:
            kutyanev = input("Nincs ilyen kutya. Adjon meg másik nevet: ")
        for kutya in kutyak:
            if kutya.nev == kutyanev:
                if kutya.statusz != "foglalt":
                    kutya.statusz = "foglalt"
                    print(f"A kutya státusza vátoztatva lett {kutya.statusz}-ra.")
                    time.sleep(2)
                else:
                    print("A kutya már foglalt.")
                    time.sleep(2)
    else:
        print("Nem változtatott meg egy státuszt sem.")
        time.sleep(2)
    FajlIras(kutyak, emberek, osszeg)
    

# 5.MENUPONT
def Kutyaadatmod(kutyak, emberek, osszeg):
    menupontok = ["Név", "Termet", "Ivartalanítás", "Státusz"]
    nev = input("Adja meg a kutya nevét: ")
    nevek = []
    for kutya in kutyak:
        nevek.append(kutya.nev)
    while nev not in nevek:
        print("Nem található a megadott névnek megfelelő kutya!")
        nev = input("Adja meg a kutya nevét: ")
    print("Válasszon módosítandó adatot: ")
    valasztas = menu(menupontok)
    while valasztas != 0:
        if valasztas == 1:
            kutya.nev = KutyanevBeker()
        elif valasztas == 2:
            kutya.termet = TermetBeker()
        elif valasztas == 3:
            kutya.ivar = IvarBeker()
        elif valasztas == 4:
            kutya.statusz = StatuszBeker()
        valasztas = menu(menupontok)
        break
    FajlIras(kutyak, emberek, osszeg)
    valasztas = menu(menupontok)


     # 1. választás
def KutyanevBeker(kutya):
    ujNev = input("Adja meg az új nevet: ")
    kutya.nev = ujNev
    return ujNev

      # 2. választás
def TermetBeker(kutya):
    lehetsegesTermet = ['kicsi', 'közepes', 'nagy']
    for i in range(len(lehetsegesTermet)):
        print(f"{i+1}. {lehetsegesTermet[i]}")
    valasztas = "ab"
    while '0' > valasztas or '3' < valasztas:
        valasztas = input("Adja meg a típus számát [1-3]: ")
        if lehetsegesTermet[int(valasztas)-1] == "kicsi" or lehetsegesTermet[int(valasztas)-1] == "közepes":
            print(f"A kutya termete változtatva lett {lehetsegesTermet[int(valasztas)-1]}-re")
        elif lehetsegesTermet[int(valasztas)-1] == "nagy":
            print(f"A kutya termete változtatva lett {lehetsegesTermet[int(valasztas)-1]}-ra")
    time.sleep(2)
    kutya.termet = lehetsegesTermet[int(valasztas)-1]
    return lehetsegesTermet[int(valasztas)-1]

      # 3. választás
def IvarBeker(kutya):
    amiszeretne = input("Ivartalanítva lett a kutya? [Igen/Nem] ")
    while amiszeretne.lower() != "igen" and amiszeretne.lower() != "nem":
        print("Kérem adja meg helyesen")
        amiszeretne = input("Ivartalanítva lett a kutya? [Igen/Nem] ")
    ivar = "ab"
    if amiszeretne.lower() == "igen":
        ivar = "igen"
        print("A kutya adata módosítva lett.")
    else:
        ivar = "nem"
        print("A kutya adata módosítva lett.")
    time.sleep(2)
    kutya.ivar = amiszeretne.lower
    return ivar

      # 4. választás
def StatuszBeker():
    lehetsegesStatusz = ['lakos','foglalt', "örökbeadott"]
    for i in range(len(lehetsegesStatusz)):
        print(f"{i+1}. {lehetsegesStatusz[i]}")
    valasztas = "ab"
    while '0' >= valasztas or '3' < valasztas:
        valasztas = input("Adja meg a típus számát [1-3]: ")
    print(f"A kutya státusza változtatva lett {lehetsegesStatusz[int(valasztas)-1]}-ra")
    time.sleep(2)
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
            koltseg = input("Adja meg a költség összegét: ")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg a költség összegét: ")
            szam += int(koltseg)
            print(f"Az új egyenleg: {szam}")
        else:
            koltseg = input("Adja meg a költség összegét: ")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg a költség összegét: ")
            szam -= int(koltseg)
            print(f"Az új egyenleg: {szam}")
    else:
        print("Az egyenleg nem változott!")
    osszeg = szam
    FajlIras(kutyak, emberek, osszeg)



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
    KutyaEvIras(kutyak)

def KutyaEvIras(kutyak):
    f = open("kutyak.txt", "w", encoding="utf-8")
    for kutya in kutyak:
        f.write(f"{kutya.nev};{kutya.szuletes};{kutya.fajta};{kutya.termet};{kutya.nem};{kutya.ivar};{kutya.statusz};{'kölyök' if kutya.szuletes >= 2020 else 'felnőtt'};{int(datetime.datetime.today().strftime('%Y'))-kutya.szuletes}\n")
    f.close()