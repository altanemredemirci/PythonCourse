## İki kardeşin yaşlarını kullanıcıdan alın ve toplemını ekrana yazdırınız.
# yas1=input("1.Yaş:")
# yas2=input("2.Yaş:")
#
# y1=int(yas1)
# y2=int(yas2)
#
# toplamYas=y1+y2
# print(toplamYas)
##--- yukarıdaki kodun optimize hali

# yas1=int(input("1.Yaş:"))
# yas2=int(input("2.Yaş:"))
#
# toplamYas=yas1+yas2
# print(toplamYas)


# yas1=float(input("1.Yaş:")) ##float da tam sayı ile ondalıklı sayıyı . ayırır.
# yas2=int(input("2.Yaş:"))
#
# toplamYas=yas1+yas2
# print(toplamYas)


#region ÖDEV
"""
Soru 1: Değişken Tanımlama
Aşağıdaki değişkenleri tanımlayın ve değerlerini yazdırın:

Ad="Sinem"
Yas=15
Boy=145.40
IsStudent=True

Soru 2: Veri Tipi Belirleme
Aşağıdaki değişkenlerin veri tiplerini type() fonksiyonu ile bulun:

a = 42 int
b = 3.14 float
c = "Python" string
d = True bool
e = [1, 2, 3] list
print(type(e))


Soru 3: Basit Tür Dönüşümü
Aşağıdaki dönüşümleri yapın:

sayi_str = "123"
# String'i integer'a çevirin sayi=int(sayi_str)   123
# Integer'ı float'a çevirin sayiFloat= float(sayi) 123.0
# Float'ı string'e çevirin  sayiString=str(sayiFloat)




Soru 4: Kullanıcı Girişi ve Dönüşüm
Kullanıcıdan yaşını isteyin ve aşağıdaki işlemleri yapın:

Girdiyi integer'a çevirin
10 yıl sonraki yaşını hesaplayın
Sonucu string olarak "10 yıl sonra ... yaşında olacaksınız" formatında yazdırın

ad="Altan Emre"
soyad="Demirci"
yas=36

print("Ad:{}\nSoyad:{}\nYaş:{}".format(ad,soyad,yas))



Soru 5: Hatalı Dönüşüm Kontrolü
Aşağıdaki kodda hangi satırlar hata verir? Neden?
a = int("123")      # Satır 1
# b = int("12.5")   # Satır 2 float hatası
c = float("3.14")   # Satır 3
d = str(True)       # Satır 4 "True"
e = bool("")        # Satır 5 True
f = int(True)       # Satır 6 1

"""
#endregion

# sayiSTR="123.4"
# sayiFloat=float(sayiSTR)
# print(sayiFloat)



# Girdiyi integer'a çevirin
# 10 yıl sonraki yaşını hesaplayın
# Sonucu string olarak "10 yıl sonra ... yaşında olacaksınız" formatında yazdırın

# yas=int(input("Yaş:"))
# yas+=10 # yas=yas+10
# print("10 yıl sonra "+str(yas)+" yaşında olacaksınız")
# print("10 yıl sonra",str(yas),"yaşında olacaksınız")
# print(f"10 yıl sonra {yas} yaşında olacaksınız")
# print("10 yıl sonra {} yaşında olacaksınız".format(yas))





a = int("123")      # Satır 1
# b = int("12.5")     # Satır 2 float hatası
c = float("3.14")   # Satır 3
d = str(True)       # Satır 4 "True"
e = bool("")        # Satır 5 True
f = int(True)       # Satır 6 1

print(a)
# print(b)
print(c)
print(d)
print(e)
print(f)



