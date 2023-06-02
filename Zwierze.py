from abc import ABC, abstractmethod

from Organizm import Organizm


class Zwierze(Organizm):
    def __init__(self, mojaGra, sila, inicjatywa, x, y, wiek, nowoNarodzony):
        super().__init__(mojaGra, sila, inicjatywa, x, y, wiek, nowoNarodzony)

    def akcja(self):
        self.wiek += 1
        if not self.nowoNarodzony:
            wsp_n = self.ruchOrganizmu()
            if self.mojaGra.getOrganizm(wsp_n.y, wsp_n.x) is None:
                self.mojaGra.ustawNaPlanszy(None, self.wsp_o.y, self.wsp_o.x)
                self.mojaGra.ustawNaPlanszy(self, wsp_n.y, wsp_n.x)
                self.wsp_o = wsp_n
            else:
                innyOrganizm = self.mojaGra.getOrganizm(wsp_n.y, wsp_n.x)
                self.kolizja(innyOrganizm)
        else:
            self.nowoNarodzony = False

    @abstractmethod
    def kolizja(self, innyOrganizm):
        pass

    @abstractmethod
    def walka(self, innyOrganizm):
        pass

    @abstractmethod
    def rysujOrganizm(self):
        pass

    @abstractmethod
    def getImie(self):
        pass

    def rozmnazanie(self):
        wsp_n = self.wspDoRozmnazania()
        if wsp_n.x != -1 and wsp_n.y != -1:
            print(f"Rozmnazanie: {self.getImie()}({self.wsp_o.x}, {self.wsp_o.y}) udane.")
            #self.duplikujOrg(wsp_n)

    def zgodneGatunki(self, innyOrganizm):
        return innyOrganizm.getImie() == self.getImie()
