L=[]
for i in range(0,6):
    sayi=int(input('sayı giriniz..'))
    L.append(sayi)
L.sort()
print('listenin medyani:',(L[2]+L[3])/2)
