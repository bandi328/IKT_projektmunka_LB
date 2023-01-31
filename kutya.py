class Kutya:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.szuletes = int(adatok[1])
        self.fajta = adatok[2]
        self.termet = adatok[3]
        self.nem = adatok[4]
        self.ivar = adatok[5]
        self.statusz = adatok [6]

    def eletkor(self, kutyak):
        eletkor = ""
        for kutya in kutyak:
            if kutya.szuletes >= 2020:
                eletkor = "kölyök"
            else:
                eletkor = "felnőtt"
        return eletkor