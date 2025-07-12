######## DEĞİŞKENLER #########
"""
RAM: Bilgisayarın donanımınada gecici bellek olraka tanımlanır ve PC kapattığımızda resetlenir.
Bilgisayarda gerçekleştirilen her işlem özellikle KAYDET denmediği sürece RAM bellekte gerçekleşir.

Programlama amacıyla kodlanan her proje ram üzerinde anlık çalışır. Bu çalışma esnasında projede kullanılacak değerlerin tanımlanması, işleme tabi tutmak için taşınması ve sonucun tutulması için değişkenler kullanılır.

Değişkenler tek bir data(veri) tutabilirler. İsimleri unique(benzersiz) olmalıdır.

**** Değişken İsimlendirme Kuralları ****
*yanlışlar: 1sayi, ?sayi, sayi!, ad soyad, ad-soyad
*doğrular: sayi1, _sayi, sayi_, adsoyad, ad_soyad
***Bütün yazılım dillerinde kabul edilen tek özel karakter _ alt tire dir.

Case-Sensitive
lowercase = adsoyad
UPPERCASE = ADSOYAD
camelCase = adSoyad      universiteFakulteAdlari
kebab-case = ad-soyad
snake_case = ad_soyad
"""


####### VERİ TİPLERİ #########
"""
Sayısal Veri Tipleri: 
    *int: +/- tam sayıları tanımlar.
    *float: +/- ondalıklı sayıları tanımlar.
    
Sözel Veri Tipi(string):
    *str: Metinsel veri tanımlar. "değer" çift tırnak veya 'değer' tek tırnak ile tanımlanır.
    
Mantıksal Veri Tipi(boolean):
    *bool: Sadece true veya false değeri alır.
"""
# a=56
# b=45
# print(a+b) #int tipindeki değerer + operatörü ile toplanır.
# print(type(a))
# print(type(b))


# s1=15.5
# s2=16.654
# print(s1+s2) #float tipindeki değerer + operatörü ile toplanır.
# print(type(s1))
# print(type(s2))

# x="56"
# y="45"
# print(x+y) #metinsel değerler + operatörü ile birleştirilir(concat).


# s1=15.5
# s2="15.5"
# print(s1+s2) #sayısal + sözel hata verir.
# print(s1,s2) #virgül ile iki eleman olduğunu bilir.


# s1=15
# s2=4
# print(s1>s2)
# sonuc=s1<s2
# print(sonuc)
# print(type(sonuc))

### KULLANICI ETKİLEŞİM KOMUTLARI ###

##Ekrana metin yazdırmak için print() komutu kullanılır.

# print()

##Kullanıcıdan data almak için input() komutu kullanılır.

# isim=input("Adınız:")
# soyisim=input("Soyadınız:")
#
# print(isim+" "+soyisim)
#
# adSoyad = isim+" "+soyisim
# print(adSoyad)
#
# print(isim,soyisim)

##Sep() Komut Kullanımı
#Sep print içerisinde virgül ile ayrılan elemanların arasına ne tanımlanacağını belirler. Default " " boşluk olarak tanımlanır.
# print("Elma","Armut","Kiraz")
# print("Elma","Armut","Kiraz",sep=" ")
# print("Elma","Armut","Kiraz",sep="-") #
# print("Elma","Armut","Kiraz",sep="?") #


#End print komutundan sonra ne yapılacağını tanımlanacağını belirler. Default "\n" yani alt satıra geçer.
# print("Elma","Armut","Kiraz")
# print("Elma","Armut","Kiraz",end="\n")
# print("Elma","Armut","Kiraz",end=" ")
# print("Elma","Armut","Kiraz")
# print("Elma","Armut","Kiraz")


#\n Komutu alt satıra geçmeyi sağlar.
# print("Altan\nEmre\n\nDemirci")





