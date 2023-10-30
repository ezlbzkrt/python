gun=input("Türkçe gün ya da ay adı yazınız..:")
TrEn={'Pazartesi':'Monday','Salı':'Tuesday','Çarşamba':'Wednesday','Perşembe':'Thursday','Cuma':'Friday','Cumartesi':'Saturday','Pazar':'Sunday','Ocak':'January','Şubat':'February','Mart':
'March','Nisan':'April','Mayıs':'May','Haziran':'June','Temmuz':'July','Ağustos':'August','Eylül':'September','Ekim':'October','Kasım':'November','Aralık':'December'}
print("ingilizcesi..:",end=" ")
print(TrEn.get(gun,'Bu kelimenin karşılığı sözlükte yok!'))
