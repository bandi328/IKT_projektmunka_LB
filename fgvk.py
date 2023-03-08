from menu import menu
from Kutya import *
from Ember import *
import time
import datetime
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
    ok = False
    while ok == False:
        if re.fullmatch(regexEmail, email):
            return str(email)
        email = input("\tEmail cím: ")

def checkTel():
    tel = input("\tTelefonszám: ")
    ok = False
    while ok == False:
        if len(tel) == 11 and tel.isnumeric():
            return str(tel)
        tel = input("\tTelefonszám: ")

def checkKutyaNev(kutyak):
    good = False
    while not good:
        allatNev = input("Adja meg az örökbefogadni kívánt kutya nevét [kilépés: mégse]: ")
        for kutya in kutyak:
            if allatNev.capitalize() == kutya.nev:
                good = True
            elif allatNev.capitalize() == "Mégse":
                return "mégse"
        os.system('cls')
        print("Nincs ilyen kutya.")
    for i in range(len(kutyak)):
        if kutyak[i].nev == allatNev.capitalize():
            if kutyak[i].statusz == "foglalt" or kutyak[i].statusz == "örökbeadott":
                os.system('cls')
                print("A kutya nem fogadható örökbe, válasszon másik kutyát!")
                checkKutyaNev(kutyak)
            else:
                kutyak[i].statusz = "örökbeadott"
                return allatNev.capitalize()

def Orokbefogadas(kutyak, emberek, osszeg):
    szabad = []
    for kutya in kutyak:
        if kutya.statusz == "lakos":
            szabad.append(kutya.nev)
    print("Örökbefogadhatő kutyák:")
    print(*szabad, sep=", ")
    allatNev = checkKutyaNev(kutyak)
    if allatNev == "mégse":
        return
    os.system('cls')
    print(f"A kiválasztott kutya: {str(allatNev)}")
    print("Adja meg adatait!")
    emberNev = input("\tTeljes név: ")
    tel = checkTel()
    email = str(checkEmail())
    print(email)
    lakcim = str(input("\tLakcím: "))
    emberek.append(Ember(f"{allatNev};{emberNev};{tel};{email};{lakcim}"))
    FajlIras(kutyak, emberek, osszeg)
    os.system('cls')
    print("A örökbefogadás sikeres volt!")
    time.sleep(2)

# 2. MENUPONT
def Listamenu(kutyak):
    menupontok2 = ["Fajta szerint", "Születési év szerint", "Termet szerint", "Nem szerint", "Ivartalanitás szerint", "Státusz szerint", ]
    valasztas = menu(menupontok2)
    kutyafajtak = []
    kutyaszuletesek = []
    kutyastatuszok = []
    for kutya in kutyak:
        kutyafajtak.append(kutya.fajta)
        kutyaszuletesek.append(kutya.szuletes)
        kutyastatuszok.append(kutya.statusz)

    while valasztas != 0:
        if valasztas == 1:
            fajta = input("Adja meg a kutyák fajtáját: ")
            while fajta not in kutyafajtak:
                print("Nincs ilyen fajta kutya az adatbázisban!")
                inpfaj =input("Szeretne másik fajtára keresni?")
                if inpfaj.lower() == "igen":
                    fajta = input("Adja meg a kutyák fajtáját: ")
                elif inpfaj.lower() != "nem" and inpfaj.lower() != "igen":
                    print("Kérem adja meg helyesen")
                    inpfaj =input("Szeretne másik fajtára keresni?")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.fajta == fajta:
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 2:
            szulinap = input("Adja meg a kutya születési évét: ")
            while szulinap.isnumeric() == False:
                print("Kérem egy számot adjon meg!")
                szulinap = input("Adja meg a kutya születési évét: ")
            while int(szulinap) not in kutyaszuletesek:
                while szulinap.isnumeric() == False:
                    print("Kérem egy számot adjon meg!")
                    szulinap = input("Adja meg a kutya születési évét: ")
                print("Nincs ebben az évben született kutya az adatbázisban!")
                szuliakar = input("Szeretne másik évre rákeresni?[igen/nem] ").lower()
                while szuliakar != "nem" and szuliakar != "igen":
                    print("Kérem adja meg helyesen")
                    szuliakar = input("Szeretne másik évre rákeresni?[igen/nem] ").lower()
                if szuliakar == "igen":
                    szulinap = input("Adja meg a kutya születési évét: ")
                else:
                    return
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.szuletes == int(szulinap):
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 3:
            termetek = ["nagy","közepes","kicsi"]
            termet = input("Adja meg a kutya termetét[nagy/közepes/kicsi]: ")
            while termet.lower() not in termetek:
                print("Nem helyesen adta meg!")
                termet = input("Adja meg a kutya termetét[nagy/közepes/kicsi]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.termet == termet.lower():
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 4:
            nem = input("Adja meg a kutya nemét[lány/fiú]: ")
            while nem.lower() != "lány" and nem.lower() != "fiú":
                print("Kérem válasszon a lehetőségek közül/Adja meg helyesen!")
                nem = input("Adja meg a kutya nemét[lány/fiú]: ")
            while nem.lower() != "lány":
                nem = input("Adja meg a kutya nemét[lány/fiú]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.nem == nem.lower():
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 5:
            ivar = input("Adja meg a kutya ivartalanítva van-e[Igen/Nem]: ")
            while ivar.lower() != "igen" and ivar.lower() != "nem":
                print("Kérem válasszon a lehetőségek közül/Adja meg helyesen!")
                ivar = input("Adja meg a kutya ivartalanítva van-e[Igen/Nem]: ")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.ivar == ivar.lower():
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")   
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)
        elif valasztas == 6:
            statusz = input("Adja meg a kutya státuszát[lakos/foglalt/örökbeadott]:")
            while statusz.lower() not in kutyastatuszok:
                print("Kérem válasszon a lehetőségek közül/Adja meg helyesen!")
                statusz = input("Adja meg a kutya státuszát[lakos/foglalt/örökbeadott]:")
            print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
            for kutya in kutyak:
                if kutya.statusz == statusz.lower():
                    print(f"{kutya.nev}\t{kutya.szuletes}\t{kutya.fajta}\t{kutya.termet}\t{kutya.nem}\t{kutya.ivar}\t{kutya.statusz}")   
            time.sleep(5)
            input(f"\nTovábblépéshez nyomja meg az ENTER-t.")
            valasztas = menu(menupontok2)



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
        os.system("cls")
        neve = input("Adja meg a kutya nevét: ").capitalize()
        os.system("cls")
        print(f"A kutya neve: {neve}")
        szuletesBeker = (input("Adja meg a kutya születési évét: "))
        while ok == False:
            if szuletesBeker.isnumeric():
                if ev-int(szuletesBeker) <= 15 and ev-int(szuletesBeker) >= 0:
                    szuletes = szuletesBeker
                    ok = True
                else:
                    os.system("cls")
                    szuletesBeker = input("Az évszám helytelen. Adja meg a kutya születési évét: ")
            else:
                os.system("cls")
                szuletesBeker = input("Az évszám helytelen. Adja meg a kutya születési évét: ")
        os.system("cls")
        print(f"A kutya neve: {neve}")
        print(f"A kutya születési éve: {szuletesBeker}")
        fajta = input("Adja meg a kutya fajtáját: ").lower()
        os.system("cls")
        print(f"A kutya neve: {neve}")
        print(f"A kutya születési éve: {szuletesBeker}")
        print(f"A kutya fajtája: {fajta}")
        ok = False
        termet = input(f"Adja meg a kuya termetét [kicsi/közepes/nagy]: ").lower()
        while ok == False:
            if termet.lower() in valosTermet:
                ok = True
            else:
                os.system("cls")
                termet = input(f"Az termet helytelen. Adja meg a kuya termetét [kicsi/közepes/nagy]: ").lower()
        ok = False
        os.system("cls")
        print(f"A kutya neve: {neve}")
        print(f"A kutya születési éve: {szuletesBeker}")
        print(f"A kutya fajtája: {fajta}")
        print(f"A kutya termete: {termet}")
        neme = input(f"Adja meg a kutya nemét [lány/fiú]: ").lower()
        while ok == False:
            if neme in valosNem:
                ok = True
            else:
                os.system("cls")
                neme = input("A nem helytelen. Adja meg a kutya nemét [lány/fiú]: ").lower()
        ok = False
        os.system("cls")
        print(f"A kutya neve: {neve}")
        print(f"A kutya születési éve: {szuletesBeker}")
        print(f"A kutya fajtája: {fajta}")
        print(f"A kutya termete: {termet}")
        print(f"A kutya neme: {neme}")
        ivar = input("Ivartalanított a kutya? [igen/nem]: ").lower()
        while ok == False:
            if ivar == "igen":
                ok = True
            elif ivar == "nem":
                ok = True
            else:
                ivar = input("Rossz adatot adott meg. Ivartalanított a kutya? [igen/nem]: ").lower()
        ok = False
        os.system("cls")
        print(f"A kutya neve: {neve}")
        print(f"A kutya születési éve: {szuletesBeker}")
        print(f"A kutya fajtája: {fajta}")
        print(f"A kutya termete: {termet}")
        print(f"A kutya neme: {neme}")
        print(f"A kutya ivartalanított: {ivar}")
        statusz = "lakos"
        print(f"A kutya státusza: {statusz}")
    else:
        return
    kutyak.append(Kutya(f"{neve};{szuletes};{fajta};{termet};{neme};{ivar};{statusz}"))
    FajlIras(kutyak, emberek, osszeg)
    print("\nA kutya felvétele sikeres volt!")
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
        while kutyanev.capitalize() not in kutyanevek:
            kutyanev = input("Nincs ilyen kutya. Adjon meg másik nevet: ")
        for kutya in kutyak:
            if kutya.nev == kutyanev.capitalize():
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
            kutya.nev = KutyanevBeker(kutya)
        elif valasztas == 2:
            kutya.termet = TermetBeker(kutya)
        elif valasztas == 3:
            kutya.ivar = IvarBeker(kutya)
        elif valasztas == 4:
            kutya.statusz = StatuszBeker()
        valasztas = menu(menupontok)
        FajlIras(kutyak, emberek, osszeg)


    # 1. választás
def KutyanevBeker(kutya):
    ujNev = input("Adja meg az új nevét: ").capitalize()
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
    kutya.termet = lehetsegesTermet[int(valasztas)-1].lower()
    return lehetsegesTermet[int(valasztas)-1]

    # 3. választás
def IvarBeker(kutya):
    amiszeretne = input("Ivartalanítva lett a kutya? [Igen/Nem] ").lower()
    while amiszeretne != "igen" and amiszeretne != "nem":
        print("Kérem adja meg helyesen")
        amiszeretne = input("Ivartalanítva lett a kutya? [Igen/Nem] ").lower()
    ivar = "a"
    if amiszeretne == "igen":
        ivar = "igen"
        print("A kutya adata módosítva lett.")
    else:
        ivar = "nem"
        print("A kutya adata módosítva lett.")
    time.sleep(2)
    kutya.ivar = ivar
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
    return lehetsegesStatusz[int(valasztas)-1].lower()


# 6. MENUPONT
def Adomanykezeles(kutyak, emberek, osszeg):
    szam = int(osszeg)
    print(f"Jelenlegi egyenleg: {szam} Ft")
    kerdes = input("Szeretné kezelni az adományokat? (Igen/Nem): ")
    while kerdes.lower() != "igen" and kerdes.lower() != "nem":
        print("Kérem válasszon a lehetőségek közül!")
        kerdes = input("Szeretné kezelni az adományokat? (Igen/Nem): ")
    if kerdes.lower() == "igen":
        inp = input("Mit szeretne tenni? [+(adomány hozzáadása)/-(költés feljegyzése)]: ")
        while inp != "+" and inp != "-":
            os.system("cls")
            print(f"Jelenlegi egyenleg: {szam} Ft")
            print("Kérem válasszon a lehetőségek közül!")
            inp = input("Mit szeretne tenni? [+(adomány hozzá adása)/-(költés feljegyzése)]: ")
        if inp == "+":
            koltseg = input("Adja meg az adomány összegét: ")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg az adomány összegét: ")
            szam += int(koltseg)
            print(f"Az új egyenleg: {szam} Ft")
            time.sleep(2)
        else:
            koltseg = input("Adja meg a költség összegét: ")
            while koltseg.isnumeric() == False:
                print("Kérem számot adjon meg!")
                koltseg = input("Adja meg a költség összegét: ")
            szam -= int(koltseg)
            print(f"Az új egyenleg: {szam} Ft")
            time.sleep(2)
    else:
        print("Az egyenleg nem változott!")
    osszeg = szam
    FajlIras(kutyak, emberek, osszeg)

# 7.MENUPONT
def IdKeres(kutyak, emberek, osszeg):
    kutyaazonositok = []
    for kutya in kutyak:
        kutyaazonositok.append(kutya.azonosito)
    azonositoKer = input("Adja meg a kuyta azonosítóját: ")
    while azonositoKer not in kutyaazonositok:
        print("Nincs ilyen azonosítójú!")
        akarID = input("Szeretne másik azonosítóra rákeresni?[Igen/Nem] ")
        while akarID.lower() != "igen" or akarID.lower() != "nem":
            print("Kérem válasszon a lehetőségek közül/Adja meg helyesen!")
            akarID = input("Szeretne másik azonosítóra rákeresni?[Igen/Nem] ")
            if akarID.lower() == "igen":
                azonositoKer = input("Adja meg a kuyta azonosítóját: ")
            else:
                return
    print("Név\tSzületés\tFajta\tTermet\tNeme\tIvartalanítva\tStátusz")
    for kutya in kutyak:
        if kutya.azonosito == int(azonositoKer):
            print(f"{kutya.nev};{kutya.szuletes};{kutya.fajta};{kutya.termet};{kutya.nem};{kutya.ivar};{kutya.statusz};{'kölyök' if kutya.szuletes >= 2020 else 'felnőtt'};{int(datetime.datetime.today().strftime('%Y'))-kutya.szuletes};{lista[-1]}\n")
        time.sleep(2)


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
    KutyaAzonositoGeneral(kutyak)


def KutyaEvIras(kutyak):
    f = open("kutyak.txt", "w", encoding="utf-8")
    for kutya in kutyak:
        f.write(f"{kutya.nev};{kutya.szuletes};{kutya.fajta};{kutya.termet};{kutya.nem};{kutya.ivar};{kutya.statusz};{'kölyök' if kutya.szuletes >= 2020 else 'felnőtt'};{int(datetime.datetime.today().strftime('%Y'))-kutya.szuletes}\n")
    f.close()


#KutyaAzonosito
def KutyaAzonositoGeneral(kutyak):
    f = open("kutyak.txt", "w", encoding="utf-8")
    for i in range(len(kutyak)):
        f.write(f"{kutyak[i].nev};{kutyak[i].szuletes};{kutyak[i].fajta};{kutyak[i].termet};{kutyak[i].nem};{kutyak[i].ivar};{kutyak[i].statusz};{'kölyök' if kutyak[i].szuletes >= 2020 else 'felnőtt'};{int(datetime.datetime.today().strftime('%Y'))-kutyak[i].szuletes};{i+1}\n")
    f.close()