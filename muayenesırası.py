Hasta_Giris=[]
while True:
    TC=int(input('Hastanın tc kimlik numarasını giriniz:'))
    if TC in Hasta_Giris:
        i=Hasta_Giris.index(TC)
        print("Muayene Sırası:",i+1)
    elif TC==0:
        print(Hasta_Giris[0],'TC numaralı hasta,muayene sıranız geldi.') #ilk hastayı içeriye aldık ve listeden çıkardık.
    
        Hasta_Giris.pop(0)
    else:
        Hasta_Giris.append(TC)
        print(TC,'Kaydedildi,sıraya alındı.')
