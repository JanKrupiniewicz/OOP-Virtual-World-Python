from Organizm import Organizm
from Owca import Owca


class Swiat:
    def __init__(self, sizeX, sizeY):
        self.sizeX = sizeX
        self.sizeY = sizeY
        self.tura = 1
        self.statusGry = True
        self.organizmy = []
        self.tablicaOrganizmow = [[None for _ in range(sizeX)] for _ in range(sizeY)]

        o = Owca(self, 4, 4, 10, True) # problematic line

    def rysujSwiat(self):
        print(f"\nTura: {self.tura}")
        print("." + "-" * self.sizeX + ".")
        for y in range(self.sizeY):
            row = "|"
            for x in range(self.sizeX):
                if self.tablicaOrganizmow[y][x] is None:
                    row += " "
                else:
                    row += self.tablicaOrganizmow[y][x].rysujOrganizm()
            row += "|"
            print(row)
        print("." + "-" * self.sizeX + ".")

    def ustawOrganizm(self, org):
        x, y = org.getWsp()
        if self.tablicaOrganizmow[y][x] is None:
            self.tablicaOrganizmow[y][x] = org
        self.organizmy.append(org)
        #self.organizmy.sort(key=Organizm.porownajOrganizmy)

    def wykonajTure(self):
        for organizm in self.organizmy:
            organizm.akcja()
        self.tura += 1

    def getStatusGry(self):
        return self.statusGry

    def setStatusGry(self, nowyStatus):
        self.statusGry = nowyStatus

    def getSizeX(self):
        return self.sizeX

    def getSizeY(self):
        return self.sizeY

    def ustawNaPlanszy(self, org, x, y):
        self.tablicaOrganizmow[y][x] = org

    def getOrganizm(self, x, y):
        return self.tablicaOrganizmow[y][x]

    def usunOrganizm(self, org):
        self.organizmy.remove(org)