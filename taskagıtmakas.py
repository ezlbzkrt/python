import random
print("OYUNA HOŞGELDİN,SEÇİMİNİ YAP :) ")
Liste = ["Taş","Kağıt","Makas",] 
pc=random.choice(Liste) #Bilgisayarın seçimi
player = input('[Taş-Kağıt-Makas]').capitalize()
print("Bilgisayar" , pc , "Seçti")
print("Sen" ,player, "Seçtin")
if pc==player:
    print("BERABERE")
if pc=="Kağıt" and player=="Taş":
    print("KAYBETTİN :D")
if pc=="Kağıt" and player=="Makas":
    print("KAZANDIN :D")
if pc=="Taş" and player=="Kağıt":
    print("KAZANDIN :D")
if pc=="Makas" and player=="Taş":
    print("KAZANDIN :D")
if pc=="Makas" and player=="Kağıt":
    print("KAYBETTİN :P")
if pc=="Taş" and player=="Makas":
    print("KAYBETTİN :P")
else:
    print("Liste dışı giriş yaptınız,bb")
    

