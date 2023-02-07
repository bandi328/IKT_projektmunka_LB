from fgvk import *
from menu import menu
kutyak = []
emberek = []
FajlOlvasKutya(kutyak)
FajlOlvasEmber(emberek)

menupontok = ["Örökbefogadás", "Menhelyi kutyák kilistázása", "Új kutya felvétele", "Kutya lefoglalása", "Kutya adatai módosítása", "Adományok kezelése"]

valasztas = menu(menupontok)
while valasztas != 0:
    if valasztas == 1:
        print("A az örökbefogadást választotta")
    elif valasztas == 2:
        print("A Menhelyi kutyák kilistázását választotta")
    elif valasztas == 3:
        print("Új kutya felvételét választotta")
    elif valasztas == 4:
        osszeg = FajlOlvasAdomany()
        KutyaLefoglalas(kutyak, emberek, osszeg)
    elif valasztas == 5:
        Kutyaadatmod(kutyak, emberek, osszeg)
    elif valasztas == 6:
        osszeg = FajlOlvasAdomany()
        Adomanykezeles(kutyak, emberek, osszeg)
    vlasztas = menu(menupontok)
