from Zwierze import Zwierze

class Owca(Zwierze):
    def __init__(self, mojaGra, x, y, wiek, nowo_narodzony):
        super().__init__(mojaGra, 4, 4, x, y, wiek, nowo_narodzony)

    def rysujOrganizm(self):
        return "O"

    def getImie(self):
        return "Owca"

    def duplikujOrg(self, wsp_n):
        return Owca(self.mojaGra, wsp_n['x'], wsp_n['y'], 1, True)
