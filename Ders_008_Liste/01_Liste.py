############ KOLEKSİYONLAR #############
"""
Birden fazla veriyi br başlık altında tutmak için kullanılır.

Liste [] veya list() ifadeleri tanımlanırlar.

### Boş Liste Tanımı
bosListe=[]
print(type(bosListe))
print(bosListe)

bosListe2=list()
print(type(bosListe2))


### Dolu Liste Tanımı
sayilar = [11,22,33,44,55,66]

print(sayilar)


*** Listeler birden fazla data tuttukları için bu dataları INDEX adı verilen default 0 dan başlayan ve 1'er 1'er artan numaralandırma sistemi ile tutarlar.


sayilar =[11,22,33,44,55,66,77]
# print(sayilar[0])
# print(sayilar[2])
# print(sayilar[5])
# print(sayilar[7]) #IndexError: list index out of range


sayilar =[11,22,33,44,55,66,77]

### Listeye Eleman Ekleme
sayilar.append(88)
sayilar.append("Altan")

sayilar+=[99]
print(sayilar)
print(sayilar[8])


### Çoklu Eleman Ekleme
# sehirler=["Hakkari","Giresun","Adana","Zonguldak"]
#
# # sehirler.append("İstanbul","İzmir","Çanakkale")
# sehirler+=["İstanbul","İzmir","Çanakkale"]
# # sehirler.append(["İstanbul","İzmir","Çanakkale"])
#
# print(sehirler)
# print(sehirler[4][0])



### Elemanları Sıralama
#sort metodu A->Z 0->9 a sıralama yapar. İ,Ç,Ş gibi karakteri kendi arasında sıralar.
# sehirler=["Hakkari","Giresun","Adana","Zonguldak","İstanbul","İzmir","Çanakkale"]
# sehirler.sort()
# print(sehirler)

# sehirler.sort(reverse=True) ##sort metodunun tersini yapar.
# print(sehirler)




### İstenlen Index Değerine Eleman Ekleme
sayilar =[11,22,33,44]
# sayilar.append(55)

# sayilar.insert(2,17)
# sayilar.insert(2,17)
# print(sayilar)


### Listeden Eleman Silme
# sayilar.remove(22) # Silinecek değer

# del sayilar[1] # Silinecek index numarası

# del sayilar # Liste tanımını ram bellketen KOMPLE SİLER.
# print(sayilar)




### Listedeki Eleman Sayısı
# sayilar=[11,22,33,44,11,55,66,11]
#
# print(len(sayilar)) #Listedeki eleman sayısı
# print(sayilar.count(11)) #Liste içerisinde belirtilen değerin kaç defa geçtiği bilgisini verir.


### Listedeki Elemanın Index Değerini Öğrenme
sayilar=[11,22,33,44,11,55,66,11]

# firstindx = sayilar.index(11)
# secondIndx = sayilar.index(11,1)
# thirdIndex = sayilar.index(11,5)
# print(thirdIndex)

# indx = sayilar.index(11,1,5)
# print(indx)



# sayilar=[11,22,33,44,11,55,66,11,77,11,88,99]
#SORU:Sayılar listesindeki 11 değerlerinin index numaralarını bir döngü yardımıyla ekran yazdırınız

# for i in range(12): #0-11
#     if sayilar[i]==11:
#         print(i)



# index=-1
# i=1
# while i<=sayilar.count(11):
#     index=sayilar.index(11,index+1)
#     print(index)
#
#     i+=1


# sayilar=[11,22,33,44,11,55,66,11,77,11,88,99]

#Yukarıdaki listenin en son elemanını ekran yazdıralım
# print(sayilar[len(sayilar)-1])
# print(sayilar[-1])
# print(sayilar[-2])

### Listedeki Elemanı Dışarı Çıkarma
# sayilar=[11,22,33,44,11,55,66,11,77,11,88,99]

# sayi = sayilar.pop()
# sayi = sayilar.pop(2)
# print(sayilar)
# print(sayi)



### Listedeki Elemanları Yazdırma
# sayilar=[11,22,33,44,11,55,66,11,77,11,88,99]
#
# for deger in sayilar:
#     print(deger)
#
#
#
# for index in range(len(sayilar)):
#     print(sayilar[index])

### Listedeki Eleman Kontrolü
# sayilar=[11,22,33,44,11,55,66,11,77,11,88,99]
#
# print(22 in sayilar)
#
# if 22 in sayilar:
#     print("Var")
"""

## 20 adet 1-50 arasında rastgele sayılardan oluşan bir liste tanımlayınız.

import random
random.randint(1,50)



















