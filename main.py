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
        Orokbefogadas(kutyak, emberek)
    elif valasztas == 2:
        Listamenu(kutyak)
    elif valasztas == 3:
        KutyaFelvetel(kutyak)
    elif valasztas == 4:   
        osszeg = FajlOlvasAdomany()
        KutyaLefoglalas(kutyak, emberek, osszeg)
    elif valasztas == 5:
        Kutyaadatmod(kutyak, emberek, osszeg)
    elif valasztas == 6:
        osszeg = FajlOlvasAdomany()
        Adomanykezeles(kutyak, emberek, osszeg)
    vlasztas = menu(menupontok)
