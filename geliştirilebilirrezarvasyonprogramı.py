masaNo=0
rezervasyon=['Polat','Abdülhey','Memati','Çakır']
rezervasyon2=['Elif','Nesrin']
isim=input('İsminiz nedir?')
if isim=='Polat':
    masaNo=5
if isim=='Abdülhey':
    masaNo=7
if isim=='Memati':
    masaNo=3
if isim=='Çakır':
    masaNo=10
    
if isim in rezervasyon:
    print('Buyrun',isim,'Bey,Hoşgeldiniz.',masaNo,'numaralı masanız hazır.')

elif isim in rezervasyon2:
    print('Üzgünüm',isim,'Hanım.Rezervasyonunuz yarın akşam için görünüyor.')
elif isim not in rezervasyon and isim not in rezervasyon2:
    print('Maalesef rezervasyonunuz bulunamadı.')
