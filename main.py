from Swiat import Swiat


# hello world

print("       OOP 2023")
print("s193320 Jan Krupiniewicz")
print("   S Y M U L A T O R ")
print("      S W I A T A\n")

sizeX = int(input("WYBIERZ WYMIARY PLANSZY\nWprowadz rozmiar X: "))
sizeY = int(input("Wprowadz rozmiar Y: "))
mojaGra = Swiat(sizeX, sizeY)
M = 'a'
while M != 'q':
    mojaGra.rysujSwiat()
    mojaGra.wykonajTure()
    M = input("\nQ - Zakoncz: ")