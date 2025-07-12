##### OPERATÖRLER #####

#Matematiksel Operatörler(+,-,*,/,//,%,**)
#Mod alma operatörü
# sayi=45
# print(sayi%2) #45 sayının 2 ye bölümünden kalanı verir.

#Kullanıcıdan alınan bir sayının çift olup olmadığını ekrana yazdırınız
# sayi=int(input("Sayı giriniz"))
# print(sayi%2)

#Üs alma
# sayi=3
# print(sayi**2)
# print(sayi**3)
# print(sayi**4)

#Atama(=) ve İşlemli Atama Operatörleri

# sayi = 45
#
# sayi+=1  # sayi=sayi+1  #46
# sayi-=1  # sayi=sayi-1  #45
# sayi*=1  # sayi=sayi*1  #45

#Ondalıklı bölme operatörü
# sayi/=2  # sayi=sayi/1  #22.5

#Tamsayı bölme operatörü
# sayi//=2   #22.5 yerine 22 verir.
# print(sayi//2)

#Mod alma operatörü
# sayi=45
# print(sayi%2) #45 sayının 2 ye bölümünden kalanı verir.

#Kullanıcıdan alınan bir sayının çift olup olmadığını ekrana yazdırınız
# sayi=int(input("Sayı giriniz"))
# print(sayi%2)


"""
Soru 6: Matematik İşlemleri ve Dönüşümler
İki sayı tanımlayın: 15 ve 4
Aşağıdaki işlemleri yapın ve sonuçların tiplerini kontrol edin:

Toplama
Çıkarma
Çarpma
Bölme (/)
Tam bölme (//)
Mod alma (%)
Üs alma (**)

sayi1=15
sayi2=4
print(sayi1+sayi2)
print(type(sayi1+sayi2))

print(sayi1-sayi2)
print(type(sayi1-sayi2))

print(sayi1*sayi2)
print(type(sayi1*sayi2))

print(sayi1/sayi2)
print(type(sayi1/sayi2))

print(sayi1//sayi2)
print(type(sayi1//sayi2))

print(sayi1%sayi2)
print(type(sayi1%sayi2))

print(sayi1**sayi2)
print(type(sayi1**sayi2))
"""

#### KARŞILAŞTIRMA OPERATÖRLER ####
"""
<  Küçüktür
>  Büyüktür
<= Küçük veya Eşit
>= Büyük veya Eşit
== Eşittir
!= Eşit Değildir
"""

# sayi1=10
# sayi2=10
# print(sayi1<sayi2)
# print(sayi1>sayi2)
# print(sayi1<=sayi2)
# print(sayi1>=sayi2)
# print(sayi1==sayi2)
# print(sayi1!=sayi2)


### MANTIKSAL OPERATÖRLER(AND,OR,NOT) ###
"""
AND: birden fazla karşılaştırma işlemini yapmamızı ve her durumun true dönmesi gereken işlemlerde kullanılır.
and operatörü çarpma işlemi mantığında çalışır. operatörün kontrol ettiği koşullardan biri bile false (0) olursa sonuç False olur.
"""
# username = "altanemre"
# password = "123"
# Kullanıcıdan giriş bilgilerini(kullanıcıadı ve şifre) isteyelim.
# Girilen bilgiler ile sistemde tanımlı olanlar eşleşiyor ise ekrana "GİRİŞ BAŞARILI"
# Eşleşmiyor ise "Giriş Bilgileriniz Hatalı" yazsın.

# kullaniciadi = input("Username:")
# sifre = input("Password:")
#
# cevap = username==kullaniciadi and password==sifre
#
# if(cevap==True):
#     print("GİRİŞ BAŞARILI")
# else:
#     print("Giriş Bilgileriniz Hatalı")

"""
OR:birden fazla karşılaştırma işlemini yapmamızı ve sonucun true dönmesi için herhangi bir koşulun true olması yeterli ise OR operatörü kullanılır.
OR operatörü toplama işlemi mantığında çalışır. operatörün kontrol ettiği koşullardan biri bile True (1) olursa sonuç True olur.
"""
# username = "altanemre"
# email = "altanemre@gmail.com"
# password = "123"
#
#
#
# kullanici = input("Username/Email:")
# sifre = input("Password:")
#
# cevap = (username==kullanici or email==kullanici) and password==sifre
#
# if(cevap==True):
#     print("GİRİŞ BAŞARILI")
# else:
#     print("Giriş Bilgileriniz Hatalı")


"""
NOT: True olan bir değeri False'a, False olan bir değeri ise True'a çevirir.
"""



## in içinde kontrolü
# sehir="Ardahan"
# # print("da" in sehir)
# print("arda" not in sehir)

# username="altan"
# kullanici="Altan"
# cevap=username==kullanici
# if(not cevap): #if içindeki koşulun-karşılaştırmanın sonucu True ise çalışır.
#     print("BAŞARILI")


# SORU: Kullanıcıdan alınan vize ve final notları üzerinden ortalamayı hesaplayarak ekrana yazdırınız.
#   Ortalama= vize%40 +  final%60

vize = float(input("Vize:"))
vizeDogru= vize>=0 and vize<=100







# SORU: Kullanıcıdan yaş, mezuniyet ve Cinsiyet bilgilerini alınız.
#   Ehliyet alma koşulu: Yaş 18 den büyük ve mezuniyet Lise olmalı. veya cinsiyet erkek olmalı.

# yas=int(input("Yaş:"))
# mezuniyet = input("Mezuniyet:")
# cinsiyet=input("Cinsiyet:")
#
# ehliyet= (yas>18 and mezuniyet=="lise") or cinsiyet=="erkek"












