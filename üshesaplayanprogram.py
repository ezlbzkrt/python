def ustel(a,b):
    if b==0:
        return 1
    else:
        return a*ustel(a,b-1) #2*2*2*2*1


a=int(input("tabanı giriniz:"))
b=int(input("üssü giriniz:"))


print(ustel(a,b))    
