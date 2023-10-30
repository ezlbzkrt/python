def dolar(TL):
    return(TL/28,26)


#aşağı satırdaki fonksiyon da yukarıdakiyle aynı işi yapacaktır.
#dolar=lambda TL: TL/27



TL=int(input("Türk lirası giriniz:"))
print(TL,"Türk lirası=",dolar(TL),"dolardır.")
