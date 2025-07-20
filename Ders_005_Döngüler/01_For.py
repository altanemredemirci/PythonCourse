#### RANGE - ARALIK ####

range(5)     #0,1,2,3,4 sayıları tanımlar.
range(2,9)   #2,3,4,5,6,7,8 sayıları tanımlar.
range(2,10,2) #2,4,6,8 sayıları tanımlar

# for i in range(5):
#     print(i)


# for i in range(2,9):
#     print(i)

# for i in range(2,10,2):
#     print(i)


#SORU: 2-100 arasındaki tek sayıları ekrana yazdırınız
# for i in range(2,100):
#     if i%2==1:
#         print(i)
#
# for i in range(3,100,2):
#     print(i)


# for i in range(2,100,2):
#     i+=1
#     print(i)


#SORU:500-50 arasında hem 3 hemde 4 e bölünebilen sayıları ekrana yazdırınız
# for i in range(500,50,-1):
#     if i%12==0: # i%3==0 and i%4==0:
#         print(i)


#SORU:Yukarıdaki işlem sonucu çıkan sayılardan çift olanların toplamını ekrana yazdırınız
# toplam=0
# for i in range(500,50,-1):
#     if i%12==0: # i%3==0 and i%4==0:
#         toplam+=i
#
# print("Toplam:",toplam)


#SORU: Kullanıcıdan alınan 2 sayı arasındaki tekleri ayrı çiftleri ayrı toplayarak ekrana  yazdırınız.
# ciftToplam=0
# tekToplam=0
#
# basla=int(input("Başlangıç:"))
# bitis=int(input("Bitiş:"))
#
# if basla>bitis:
#     basla,bitis = bitis,basla
#
# for i in range(basla,bitis+1):
#     if i%2==0:
#         ciftToplam+=i
#     else:
#         tekToplam+=i
#
# print("Çift Sayılar Toplamı:",ciftToplam)
# print("Tek Sayılar Toplamı:",tekToplam)


#region SEFA
# say1=int(input("ilk sayı"))
# say2=int(input("ikinci sayı"))
# toplam2=0
# toplam1=0
# if say1<say2:
#     for i in range(say1,say2+1):
#         if i%2==0:
#             toplam2+=i
#         else:
#             toplam1+=i
# else:
#     for i in range(say2, say1-1,-1):
#         if i % 2 == 0:
#             toplam2 += i
#         else:
#             toplam1 += i
# print("tek sayılar toplamı", toplam1)
# print("Çift sayılar toplamı", toplam2)
#endregion

#SORU:Kullanıcıdan alınan sayının asal olup olmadığını döndüren program.
## Asal sayı: en küçük asal sayı 2'dir. 1 ve kendisi hariç herhangi bir sayıya bölünmüyorsa asaldır.

# sayi=int(input("Sayı giriniz:")) #9
# if sayi<=1:
#     print("Asal Değildir.")
# elif sayi==2:
#     print("Asaldır")
# else:
#     asalMi=True
#     for i in range(2,sayi): #Bölen
#         if sayi%i==0:
#             asalMi=False
#             break
#
# if asalMi==True:
#     print("Asaldır.")
# else:
#     print("Asal Değildir")


## İç İçe For Loops
# for i in range(10): #0,1,2,3,4,5,6,7,8,9
#     for j in range(5): #0,1,2,3,4
#         print(i,j)


##SORU:# Kullanıcı: personel sayısını girsin. Her personel için çocuk sayısı sorulsun.
# Program her çocuk için : "Çocuğunuz adına 1 ağaç dikilmiştir."
# Toplam dikilen ağaç sayısını yazsın.


# toplamAgac=0
# personelSayisi=int(input("Kaç personeliniz var?"))
# for per in range(personelSayisi):
#     cocukSayisi = int(input("Kaç çocuğunuz var?"))
#     toplamAgac+=cocukSayisi
#     for i in range(cocukSayisi):
#         print("Çocuğunuz adına bir ağaç dikildi.")
#
# print("Ağaç sayısı:",toplamAgac)




#ÖDEV: 1 ile 10000000 arasındaki asal sayıları bulunuz.
# Aşağıdaki çıktıyı veren kodu for döngüsü ile yazınız.

# for sayi in range(1,10000000):
#     if sayi==2:
#         print(sayi)
#     else:
#         asalMi=True
#         for i in range(2,(sayi//2)): #Bölen
#             if sayi%i==0:
#                 asalMi=False
#                 break
#
#         if asalMi==True:
#             print(sayi)








#ÖDEV: Aşağıdaki geometrik şekilleri for döngüsü ile ekrana yazdırınız
"""
*
**
***
****
*****
"""
# for i in range(1,9):
#     print("*"*i) #print("",end="\n")

"""
***********
*         *  # 1 yıldız + 8 boşluk + 1 yıldız
*         *
*         *
***********
"""
# for i in range(1,10):
#     if i==1 or i==9:
#         print("*"*10)
#     else:
#         print("*"+(" "*8)+"*")


"""
                *
               ***
              *****
             *******
            *********   
"""

# bosluk=10
# for i in range(1,10,2):
#     print(bosluk*" ",end="")
#     print("*"*i)
#     bosluk-=1


#ÖDEV: For döngüsü ile ekran çarpım tablosunu aşağıdaki şekilde yazdırınız.
"""
1x1=1   2x1=2  3x1=3    ....
1x2=2   2x2=4  3x2=6    ....
1x3=3   2x3=6  3x3=9    ....
.....   .....  .....
"""

for i in range(1,11):
    for j in range(1,11):
        print(j,"x",i,"=",(i*j),end="\t",sep="") #\t 4 boşluk bırak
    print()