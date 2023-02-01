from fgvk import *
from menu import menu
kutyak = []
emberek = []
adomany = FajlOlvasAdomany()
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
        print("Kutya lefoglalását választotta")
    elif valasztas == 5:
        Kutyaadatmod(kutyak)
    elif valasztas == 6:
        Adomanykezeles()
    vlasztas = menu(menupontok)