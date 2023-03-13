class Kutya:
    def __init__(self, sor):
        adatok = sor.strip().split(";")
        self.nev = adatok[0]
        self.szuletes = int(adatok[1])
        self.fajta = adatok[2]
        self.termet = adatok[3]
        self.nem = adatok[4]
        self.ivar = adatok[5]
        self.statusz = adatok[6]
        if len(adatok) >= 8:
            self.korosztaly = adatok[7]
            self.eletkor = adatok[8]
            self.azonosito = adatok[9]