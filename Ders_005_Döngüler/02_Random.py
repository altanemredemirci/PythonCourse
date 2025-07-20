import random #random kod kütüphanesini projeye dahil ettik
import time

# sayi=random.randint(1,10)
# print(sayi)

# print(random.randint(1,5)) # Belirtilen aralıkta int bir rastgele sayı verir.
# print(random.random()) # 0-1 aralığında rastgele sayı verir.
# print(random.randrange(1,5)) # Belirtilen aralıkta bitiş değerini dahil etmeden rastgele sayı verir.
# print(random.uniform(1.55,2.44)) # Belirtilen aralıkta float bir rastgele sayı verir

#Kullanıcıya 3 tahmin hakkı verin ve sayıyı tahmin etmesini isteyiniz.
rastgele=random.randint(1,10)
print(rastgele)

# for i in range(1,4):
#     sayi=int(input(f"{i}. Tahmininiz:"))
#
#     if sayi==rastgele:
#         print("Tebrikler")
#         break
#     else:
#         print("Tekrar Deneyiniz!")

hak=1

while hak<4:
    sayi = int(input(f"{hak}. Tahmininiz:"))

    if sayi==rastgele:
        print("Tebrikler")
        break
    else:
         print("Tekrar Deneyiniz!")
    hak+=1