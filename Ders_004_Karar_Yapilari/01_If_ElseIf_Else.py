### KARAR YAPILARI - AKIŞ KONTROL - IF ELSE ###
"""
 CONDITION - KOŞUL


            ******* IF ELSEIF ELSE *******
            Bir program akışı koşullara göre hareket edecek ise If Else yapısı kullanılır.
            if veya elseif bloklarından biri çalışırsa geriye kalan durumlar kontrol edilmez.

            if(condition==true)
            {
                if koşulu true ise çalışacak kod bloğu
            }
            elif(condition2==true)
            {
                elif koşulu true ise çalışacak kod bloğu
            }
            elif(condition2==true)
            {
                elif koşulu true ise çalışacak kod bloğu
            }
            elif(condition2==true)
            {
               elif koşulu true ise çalışacak kod bloğu
            }
            else
            {
                if ve elif koşulları true olmazsa else çalışır.
            }
"""

## Kullanıcıdan alınan sayının negatif mi? pozitif mi? olduğunu ekrana yazdırınız.
"""
1-Başla
2-Kullanıcıdan sayı al
3-Eğer sayı>0'dan ekrana "Pozitif" yaz
4-Değilse Eğer sayı==0 ise ekrana "Sıfır" yaz
5-Değilse ekrana "Negatif" yaz
"""

# sayi=int(input("Sayı giriniz:"))
# if sayi>0:
#     print("Pozitif")
# elif sayi==0:
#     print("Sıfır")
# else:
#     print("Negatif")


# print("if veya elif bloklarından biri True olduğu için çalışırsa, ** geri kalan her kontrol bloğu atlanır.")


#Örnek: Kullanıcının girdiği sayı 10'dan büyük ise ekrana BÜYÜK değilse KÜÇÜK yazsın

# sayi=int(input("Sayı giriniz:")) ##istenilen sayı int'e çevrildi(kullanıcıdan bir sayı istendi)
# if sayi>10:
#     print("Büyük")
# elif sayi==10:
#     print("Eşittir")
# else: ##else geriye kalan bütün durumlar için kullanılır. Bu sebeple koşul TANIMLANMAZ.
#     print("Küçük")


#SORU: Kullanıcıdan haftanın kaçıncı gününde olduğumuzu rakam olarak alalım ve alınan değere göre gün adını ekrana yazdıralım
# gun = int(input("Haftanın Kaçıncı Günündeyiz?"))
#region 1.Yol
# if gun==1:
#     print("Pazartesi")
# elif gun==2:
#     print("Salı")
# elif gun==3:
#     print("Çarşamba")
# elif gun==4:
#     print("Perşembe")
# elif gun==5:
#     print("Cuma")
# elif gun==6:
#     print("Cumartesi")
# elif gun==7:
#     print("Pazar")
# else:
#     print("Hafta 7 günden oluşur")
#2.Yol


#SORU: Kullanıcıdan alınan iki sayıdan büyük olanını ekrana yazdırınız



#SORU: Kullanıcının girdiği iki ürün fiyatından ucuz olanı bulun. Ucuz olan ürüne %25 indirim uygulayarak ödeme toplamını ekrana yazdırınız.


#SORU: Kullanıcıdan alınan vize ve final notlarının ortalamasını vize%40 final%60 üzerinden hesaplayınız.
#Ortalamaya göre harf notunu kullanıcıya bildiriniz.
#0-24 FF
#25-44 DD
#45-54 CC
#55-69 CB
#70-84 BB
#85 AA
# *** vize ve final notlarının 0-100 aralık kontrolünü yapınız. Hatalı not aralığında uyarı veriniz.

#region 2.Yol

# if gun<1 or gun>7:
#     print("Hafta 7 günden oluşur")
# elif gun==1:
#     print("Pazartesi")
# elif gun==2:
#     print("Salı")
# elif gun==3:
#     print("Çarşamba")
# elif gun==4:
#     print("Perşembe")
# elif gun==5:
#     print("Cuma")
# elif gun==6:
#     print("Cumartesi")
# elif gun==7:
#     print("Pazar")

#endregion

#region 3.Yol

# if gun<1 or gun>7:
#     print("Hafta 7 günden oluşur")
# else:
#     if gun==1:
#         print("Pazartesi")
#     elif gun==2:
#         print("Salı")
#     elif gun==3:
#         print("Çarşamba")
#     elif gun==4:
#         print("Perşembe")
#     elif gun==5:
#         print("Cuma")
#     elif gun==6:
#         print("Cumartesi")
#     else:
#         print("Pazar")

#endregion

#region 4.Yol
## Loops-Döngüler: while - for
# while True:
#     gun = int(input("Haftanın Kaçıncı Günündeyiz?"))
#     if gun<1 or gun>7:
#         print("Hafta 7 günden oluşur")
#     else:
#         if gun==1:
#             print("Pazartesi")
#         elif gun==2:
#             print("Salı")
#         elif gun==3:
#             print("Çarşamba")
#         elif gun==4:
#             print("Perşembe")
#         elif gun==5:
#             print("Cuma")
#         elif gun==6:
#             print("Cumartesi")
#         else:
#             print("Pazar")
#         break



#SORU: Kullanıcıdan alınan iki sayıdan büyük olanını ekrana yazdırınız
# sayi1=int(input("İlk sayıyı giriniz:"))
# sayi2=int(input("ikinci sayıyı giriniz:"))
#
# if sayi1>sayi2:
#     print(sayi1)
# else:
#     print(sayi2)


#SORU: Kullanıcının girdiği iki ürün fiyatından ucuz olanı bulun. Ucuz olan ürüne %25 indirim uygulayarak ödeme toplamını ekrana yazdırınız.

# fiyat1=float(input("1.Ürün fiyatı giriniz:"))
# fiyat2=float(input("2.Ürün fiyatı giriniz:"))
#
# if fiyat1>fiyat2:
#     fiyat2 = fiyat2 * 0.75
#     # fiyat2 = fiyat2 * .75
#     # fiyat2 *= 0.75
# else:
#     fiyat1=fiyat1*0.75
#
# odeme=fiyat1+fiyat2
# print("Ödemeniz:",odeme)
# print(f"Ödemeniz:{odeme:.2f}")
# print("Ödemeniz:{:.2f} TL".format(odeme))


#SORU: Kullanıcıdan alınan vize ve final notlarının ortalamasını vize%40 final%60 üzerinden hesaplayınız.
#Ortalamaya göre harf notunu kullanıcıya bildiriniz.
#0-24 FF
#25-44 DD
#45-54 CC
#55-69 CB
#70-84 BB
#85 AA
# *** vize ve final notlarının 0-100 aralık kontrolünü yapınız. Hatalı not aralığında uyarı veriniz.
# while True:
#     vize = float(input("Vize:"))
#     if vize<0 or vize>100:
#         print("Vize not aralığı hatalı!!")
#     else:
#         final = float(input("Final:"))
#
#         if final<0 or final>100:
#             print("Final not aralığı hatalı!!")
#         else:
#             ortalama = vize*.4 + final*.6
#             if ortalama<45:
#                 print("FF")
#             elif ortalama<55:
#                 print("DD")
#             elif ortalama<70:
#                 print("CC")
#             elif ortalama<85:
#                 print("BB")
#             else:
#                 print("AA")
#             break
## *** Vize notu doğru ama final notunun yanlış olması durumunda: Vizeyi tekrar istiyor..

# vize=0
#
# while True:
#     vize = float(input("Vize:"))
#     if vize<0 or vize>100:
#         print("Vize Not Aralığı 0-100 olmalıdır.")
#     else:
#         break
#
# final=0
# while True:
#     final = float(input("Final:"))
#     if final<0 or final>100:
#         print("Final Not Aralığı 0-100 olmalıdır.")
#     else:
#         break
#
# print(vize,final)

"""
Soru:
Bir yılın artık yıl olup olmadığını kontrol eden bir program yazın. 
Artık yıl kuralları:Yıl 4'e tam bölünebiliyorsa ve 100'e tam bölünemiyorsa artık yıldır.Yıl 400'e tam bölünebiliyorsa artık yıldır.Diğer durumlarda artık yıl değildir.
"""

# yil = int(input("Yıl giriniz"))
# if yil<=0:
#     print("Hatalı Yıl Bilgisi")
# else:
#     if (yil % 4==0 and yil % 100!=0) or (yil % 400==0):
#         print("Artık Yıl:",yil)
#     else:
#         print("Artık Yıl Değildir",yil)
"""
Soru:
Kullanıcıdan bir üçgenin üç kenar uzunluğunu isteyin. Girilen uzunluklara göre:Eğer üç kenar uzunluğu eşitse "Eşkenar üçgen",İki kenar uzunluğu eşitse "İkizkenar üçgen",Tüm kenar uzunlukları farklıysa "Çeşitkenar üçgen" yazdıran bir program yazın.
"""
# kenar1=int(input("1.Kenar:"))
# kenar2=int(input("2.Kenar:"))
# kenar3=int(input("3.Kenar:"))
#
# if (kenar3+kenar2)>kenar1 and (kenar1+kenar2)>kenar3  and (kenar1+kenar3)>kenar2:
#     if kenar3==kenar1==kenar2:
#         print("Eşkenar Üçgen")
#     elif kenar1==kenar2 or kenar3==kenar2 or kenar3==kenar1:
#         print("İkiz Kenar")
#     else:
#         print("Çeşitkenar")
# else:
#     print("Üçgen Değildir..")
"""
Soru:
Kullanıcıdan bir sayı girmesini isteyin. Eğer sayı pozitifse, sayının karesini hesaplayın ve yazdırın. Eğer sayı negatifse, sayının mutlak değerini hesaplayın ve yazdırın. Eğer sayı sıfırsa "Sayı sıfırdır" yazdırın.
"""
# sayi = int(input("Sayı giriniz:"))
#
# if sayi>0:
#     print(sayi**2)
# elif sayi<0:
#     print(abs(sayi))
# else:
#     print("Sayı Sıfırdır")

"""
Soru:
Kullanıcıdan bir ay numarası (1-12 arası) girmesini isteyin. Girilen numaraya göre ayın kaç gün olduğunu yazdıran bir program yazın. Şubat ayı için 28 gün, diğer aylar için standart gün sayısını kullanın (Ocak: 31, Şubat: 28, Mart: 31, vb.).
"""
# ay = int(input("Bir ay numarası girin (1-12):"))
#
# if 1 <= ay <= 12:
#     print("Geçerli rakam")
#     if ay in (1,3,5,7,8,10,12):
#         print("Ay 31 gündür")
#     elif (ay == 4 or ay == 6 or ay == 9 or ay == 11):
#         print("Ay 30 gündür")
#     elif ay == 2:
#         print("Ay 28 gündür")
#
# else:
#     print("Lütfen 1 ile 12 arasında bir tam sayı girin!")



"""
Soru:
Kullanıcıdan bir tarih (gün, ay, yıl) girmesini isteyin ve bu tarihin hangi gün olduğunu hesaplayan bir program yazın. Tarihin geçerliliğini kontrol edin (örneğin, 30 Şubat geçerli değildir). Geçerli bir tarih girilmezse "Geçersiz tarih" yazdırın.
"""
#
# tarih = input("Tarih giriniz:(Gun/Ay/Yıl)")
# import datetime
#
# yeniTarih = datetime.date(int(tarih.split("/")[2]),int(tarih.split("/")[1]),int(tarih.split("/")[0]))
# print(yeniTarih)
# print(yeniTarih.strftime("%A"))
# import datetime
#
# try:
#     gun=int(input("Günü giriniz (1-31):"))
#     ay= int(input("Ayı giriniz (1-12):"))
#     yil= int(input("Yılı giriniz:"))
#
#     tarih= datetime.date(yil, ay, gun)
#
#     gunler=["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]
#     print(f"Girilen tarih: {tarih.strftime('%d.%m.%y')}")
#     print("Haftanın günü:", gunler[tarih.weekday()])
#
# except ValueError:
#     print("Geçersiz Tarih!")

############## DATETIME KÜTÜPHANESİ ###################

# import datetime

# print(datetime.datetime.now())  # . erişim operatörüdür.
# tarih = datetime.datetime.now()
# print(tarih.year)
# print(tarih.month)
# print(tarih.day)

# print(datetime.date(2004, 2, 29))

# dogumTarihi=input("Doğum tarihi:gün/ay/yıl")
# tarihDizisi = dogumTarihi.split('/')
# print(tarihDizisi)
# yeniTarih=datetime.date(int(tarihDizisi[2]),int(tarihDizisi[1]),int(tarihDizisi[0]))
# print(yeniTarih)



# today=datetime.datetime.now()
# print(today)
# print(today.strftime("%d-%m-%Y %A"))
# print(today.strftime("%D"))
# print(today.strftime("%B"))


## Soru Kullanıcıdan isim, yaş, maaş ve çocuk sayısı alınsın.
"""
    Eğer kulanıcının yaşı 45'in altındaysa;
    Çocuk sayısına bakılacak. Ve çocuk sayısı 3'ten az ise çocuk başına 250₺, çok ise çocuk başına 200₺ 
    maaşa ekleme yapılacak.(Temel Maaş= 3000₺)
    45'in üzerinde ise çocuk başına para verilmeyecek ancak 500₺ ekleme yapılacak.
    Son olarak ekrana : "Nesrin Yılmaz, Maaşınız: 4000₺" yazılacak.  
"""

# isim=input("İsim:")
# yas= int(input("Yaş:"))
# maas= int(input("Maaş:"))
# cocukSayisi= int(input("Çocuk Sayısı:"))
#
# if yas<45:
#     if cocukSayisi<3:
#         maas = maas + (cocukSayisi*250)
#     else:
#         maas = maas + (cocukSayisi*200)
# else:
#     maas = maas + 500
# print(f"{isim}, Maaşınız:{maas}, Çocuk sayısı:{cocukSayisi}")
# print(isim," Maaşınız:",maas," Çocuk sayısı:",cocukSayisi)



"""
Kullanıcıdan cinsiyet bilgisi alınız.
    * Erkek 
            Yaş alınız. 60 ve üstünde ise 
                Maaş alınız ve maaşının 10 katı ile emekli edildiniz mesajı veriniz
            Yaşı 60'ın altında ise 
                Prim gün sayısını alınız ve prim 6000 ve üzerinde ise maaşın 11 katı ile emekli edildiniz
                Değilse Çalışmaya devam mesajını veriniz
    * Kadın
      Yaş alınız. 58 ve üstünde ise 
                Maaş alınız ve maaşının 10 katı ile emekli edildiniz mesajı veriniz
            Yaşı 58'ın altında ise 
                Prim gün sayısını alınız ve prim 3600 ve üzerinde ise maaşın 11 katı ile emekli edildiniz
                Değilse Çalışmaya devam mesajını veriniz
"""
#lower(): string datanın her karakterini küçük harfe çevirir.
#upper(): string datanın her karakterini BÜYÜK harfe çevirir.

# cinsiyet=input("Cinsiyet:").lower()
# if cinsiyet=="erkek":
#     yas=int(input("Yaşınız:"))
#     if yas>=60:
#         maas=float(input("Maaşınız:"))
#         print("Emeklilik İkramiyeniz:",(maas*10))
#     else:
#         prim=int(input("Prim Gününüz:"))
#         if prim>=6000:
#             maas = float(input("Maaşınız:"))
#             print("Emeklilik İkramiyeniz:", (maas * 11))
#         else:
#             print("Emeklilik Hayal!!!")
#
# elif cinsiyet=="kadın":
#     yas = int(input("Yaşınız:"))
#     if yas >= 58:
#         maas = float(input("Maaşınız:"))
#         print("Emeklilik İkramiyeniz:", (maas * 10))
#     else:
#         prim = int(input("Prim Gününüz:"))
#         if prim >= 3600:
#             maas = float(input("Maaşınız:"))
#             print("Emeklilik İkramiyeniz:", (maas * 11))
#         else:
#             print("Emeklilik Hayal!!!")
#
# else:
#     print("Hatalı Cinsiyet Bilgisi!!")


"""
// Aylık geliri 40000 üstünde ise %12 vergi kesilecek,
// 40000 ve altında ise %9 vergi kesimi yapılarak 
// kullanıcıya yeni gelirini bu hesaplamalar sonucunda gösteriniz
"""

# maas = float(input("Maaş:"))
#
# if maas>40000:
#     maas=maas*0.88
# else:
#     maas=maas*0.91
#
# print("Maaş:",maas)













