import random

from Wsp import Wsp


class Organizm:
    def __init__(self, mojaGra, sila, inicjatywa, x, y, wiek, nowo_narodzony):
        self.wsp_o = Wsp(x, y)
        self.mojaGra = mojaGra
        self.sila = sila
        self.inicjatywa = inicjatywa
        self.wiek = wiek
        self.nowoNarodzony = nowo_narodzony

        if x != -1 and y != -1:
            mojaGra.ustawOrganizm(self)

    def ruchOrganizmu(self):
        niepoprawny_ruch = False
        n_wsp = None

        while not n_wsp or niepoprawny_ruch:
            n_wsp = Wsp(self.wsp_o.y, self.wsp_o.x)
            rand_kierunek = random.randint(0, 3)
            if rand_kierunek == 0:
                n_wsp.y -= 1
            elif rand_kierunek == 1:
                n_wsp.y += 1
            elif rand_kierunek == 2:
                n_wsp.x -= 1
            elif rand_kierunek == 3:
                n_wsp.x += 1

            niepoprawny_ruch = n_wsp.x < 0 or self.mojaGra.getSizeX() <= n_wsp.x or n_wsp.y < 0 or self.mojaGra.getSizeY() <= n_wsp.y

        return n_wsp

    def naPlanszy(self, x, y):
        return 0 <= x < self.mojaGra.getSizeX() and 0 <= y < self.mojaGra.getSizeY()

    def wspDoRozmnazania(self):
        wsp_n = self.wsp_o

        if wsp_n.x != 0 and self.mojaGra.getOrganizm(wsp_n.y, wsp_n.x - 1) is None:
            wsp_n = (wsp_n.x - 1, wsp_n.y)
            return wsp_n
        elif wsp_n.x != self.mojaGra.getSizeX() - 1 and self.mojaGra.getOrganizm(wsp_n.y, wsp_n.x + 1) is None:
            wsp_n = (wsp_n.x + 1, wsp_n.y)
            return wsp_n
        elif wsp_n.y != 0 and self.mojaGra.getOrganizm(wsp_n.y - 1, wsp_n.x) is None:
            wsp_n = (wsp_n.x, wsp_n.y - 1)
            return wsp_n
        elif wsp_n.y != self.mojaGra.getSizeY() - 1 and self.mojaGra.getOrganizm(wsp_n.y + 1, wsp_n.x) is None:
            wsp_n = (wsp_n.x, wsp_n.y + 1)
            return wsp_n
        else:
            wsp_n = (-1, -1)
            return wsp_n

    def setWsp(self, x, y):
        self.wsp_o = Wsp(x, y)

    def getWsp(self):
        return self.wsp_o

    @staticmethod
    def porownajOrganizmy(o1, o2):
        if o1.inicjatywa == o2.inicjatywa:
            return o1.wiek < o2.wiek
        return o1.inicjatywa < o2.inicjatywa

    def czyOdbilAtak(self, o1):
        return False

    def getNowoNarodzony(self):
        return self.nowoNarodzony

    def getSila(self):
        return self.sila

    def setSila(self, n_sila):
        self.sila = n_sila

    def getWiek(self):
        return self.wiek

    def getInicjatywa(self):
        return self.inicjatywa
