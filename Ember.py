class Ember:
    def __init__(self,sor):
        adatok = sor.strip().split(";")
        self.kutyanev = adatok[0]
        self.nev = adatok[1]
        self.telefonszam = adatok[2]
        self.emailcim = adatok[3]
        self.lakcim = adatok[4]


