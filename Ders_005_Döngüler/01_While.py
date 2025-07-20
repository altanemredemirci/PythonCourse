"""
******* DÖNGÜLER - LOOPS *******
Döngüler belirli bir kod bloğunun koşula bağlı şekilde tekrarlı çalışmasını sağlar.

Döngüler : While, For olmak üzere 2 çeşittir.
"""
### WHILE ###

#1-10 arasındaki sayıları alt alta yazdırınız

# i=1
#
# while i<11:
#     print(i)
#     i=i+1

##50-0 a kadar olan sayıların çift olanlarını yazdırınız.

# i=50
# while i>=0:
#     if i%2==0:
#         print(i)
#     i=i-1


# i=50
# while i>=0:
#     print(i)
#     i=i-2


### 7-77 arasındaki sayıların toplamını ekrana yazdırınız
# toplam=0
# i=7
# while i<77:
#     toplam=toplam+i   #print(i)
#     i+=1
#
# print("Toplam:",toplam)

##SORU: 1'den başlayarak kullanıcıdan alınan sayıya kadar olan sayıların karelerini toplayan program

# i=1
# sayi = int(input("Bir sayı giriniz"))
# toplam=0
#
# while i<=sayi:
#     toplam+=i**2
#     i+=1
#
# print("Toplam:",toplam)


## BREAK: Dönügüyü istenilen adımda kırmayı sağlar.

## 1-10 arasındaki sayıları yazdırırken 7 sayısında döngü kırılsın
# i=1
#
# while i<11:
#     if i==7:
#         break
#     print(i)
#     i+=1


## CONTINUE: İşlemi bulunduğu satırdan döngü koşuluna geri gönderir.

## 1-10 arasındaki sayıların toplayan ve ekrana yazan program.
# 7 sayısı toplama işlemine dahil edilmesin

# i=1
# toplam=0
# while i<11:
#     if i==7:
#         i+=1
#         continue
#     toplam+=i
#     i+=1
#
# print(toplam)


# i=1
# toplam=0
# while i<11:
#     if i==7:
#         i+=1
#     toplam+=i
#     i+=1
#
# print(toplam)


# i=1
# toplam=0
# while i<11:
#     if i==7:
#         pass
#     else:
#         toplam+=i
#     i+=1
#
# print(toplam)

### SORU: Kullanıcının girdiği değer 'cik' olmadığı sürece toplanacak. Kullanıcı 'cik' girdiğinde toplama sona erecek ve sonnuç ekrana yazdırılacak.
# toplam=0
#
# while True: ##Sonsuz Döngü
#     sayi=input("Bir sayı giriniz:")
#     if(sayi!="cik"):
#         toplam+=int(sayi)
#     else:
#         print("Toplam:",toplam)
#         break

#region Seyfi
# toplam = 0
#
# while True:
#     girdi = input("Bir sayı girin (çıkmak için 'çık' yazın): ")
#
#     if girdi.lower() == "çık":
#         break
#     toplam+=int(girdi)
#endregion


#region Feyzanur
# toplam = 0
# deger = input("Bir sayı girin (çıkmak için 'cik' yazın): ")
#
# while deger != "cik":
#     toplam += float(deger)
#     deger = input("Bir sayı girin (çıkmak için 'cik' yazın): ")
#
# print("Toplam:", toplam)
#endregion


#region Buket
# toplam=0
#
# deger=input("Değer girin:")
#
# while deger!="cik":
#     sayi=int(deger)
#     toplam=toplam+sayi
#     deger=input("bir değer girin:")
# print("toplam:",toplam)
#endregion

### SORU: Kullanıcıdan iki sayı alınız. Toplamlarını ekrana yazdırınız
# Girilen sayıların try except ile kontrolünü sağlayınız.
# Girilen sayılardan hangisi hatalıysa tekrar isteyiniz

# while True:
#     try:
#         sayi1=int(input("1.Sayı:"))
#         break
#     except:
#         print("Sayı girişi hatalı!!")
#
# while True:
#     try:
#         sayi2=int(input("2.Sayı:"))
#         break
#     except:
#         print("Sayı girişi hatalı!!")
#
# print(sayi2+sayi1)

#region # 1-100 arasındaki sayıların toplayan program. Ancak aşağıdaki durumlarda sayıyı toplama eklemeyecek.
# * Sayı 7'nin katı ise toplama eklenmesin.
# * Sayı'nın 3 katının 7 fazlası 37'nın katı ise döngüden çıksın.

i=1
toplam=0
# while i<101:
#
#     if ((3*i)+7)%37==0:
#         break
#
#     if i%7==0:
#         i+=1
#         continue
#     toplam=toplam+i
#     i+=1


while i < 101:
    if ((3 * i) + 7) % 37 == 0:
        break

    if i % 7 != 0:
        toplam = toplam + i
    i += 1
print("Toplam:",toplam)

#endreion


















