def alan(u,g):
    A=u*g
    return A
def cevre(u,g):
    C=2*(u+g)
    return C

u=int(input("dikdörtgenin uzun kenarını giriniz:"))
g=int(input("dikdörtgenin kısa kenarını giriniz:"))
print("dikdörtgenin alanı=",alan(u,g),"m^2","dikdörtgenin çevresi=",cevre(u,g),"m.")

