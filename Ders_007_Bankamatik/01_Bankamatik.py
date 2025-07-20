# string değerler karakterlerden oluşan bir koleksiyondur. 'altan' gibi string bir değerin karakterlerin Index adı verilen numaralar ile ulaşabiliriz.
# Index numaraları default olarak 0'dan başlar ve 1'er 1'er artar.

# ad="altan"
# print(ad[0])
# print(ad[:2])
# print(ad[2:4])
# print(ad[2:])



import time
from stringprep import in_table_a1

bakiye=2500
sifre ="ab18"
tc=12345678909
cepTel=5366295131
while True:
    print("1-Kartlı İşlem\n2-Kartsız İşlem\n3-Çıkış")
    kartSecim=input("Seçiminiz:")
    if kartSecim=="1":
        hak=3
        while(hak>0):
            password=input("Şifreniz:")
            hak-=1
            if sifre==password:
              while True:
                print("""
1-Para Çekme
2-Para Yatırma
3-Transfer
4-Eğitim Ödemeleri
5-Fatura Ödemeleri
6-Şifre Güncelleme""")
                anaMenuSecim=input("Seçiminiz:")

                if anaMenuSecim=="1":
                    miktar=int(input("Çekilecek Miktar:"))
                    if bakiye>=miktar:
                        bakiye-=miktar
                        print(f"Paranızı alınız:{miktar}\nYeni Bakiye:{bakiye}")
                    else:
                        print("Yetersiz Bakiye")


                elif anaMenuSecim=="2":
                    secimYatirma=input("1-Kredi Kartı\n2-Hesap\nSeçiminiz:")
                    if secimYatirma=="1":
                        kartNo=input("16 haneli Kart Numarası:")
                        if len(kartNo)==16 and kartNo.isdigit():
                            miktar = int(input("Yatırılacak Miktar:"))
                            if bakiye >= miktar:
                                bakiye -= miktar
                                print(f"Paranızı yatırıldı:{miktar}\nYeni Bakiye:{bakiye}")
                            else:
                                print("Yetersiz Bakiye")
                    elif secimYatirma=="2":
                        miktar = int(input("Yatırılacak Miktar:"))
                        bakiye+=miktar
                        print(f"Yeni Bakiye:{bakiye}")
                    else:
                        print("Hatalı Para Yatırma Seçimi!!")


                elif anaMenuSecim=="3":
                    secimTransfer = input("1-EFT\n2-Havale\nSeçiminiz:")
                    if secimTransfer=="1":
                        iban = input("EFT yapılacak Iban numarası:").upper()
                        #
                        # print(iban.startswith("TR"))
                        # print(iban[2:])
                        # print(iban[:2])

                        if iban.startswith("TR") and iban[2:].isdigit() and len(iban)==14:
                            miktar = int(input("EFT Edilecek Miktar:"))
                            if bakiye >= miktar:
                                bakiye -= miktar
                                print(f"Eft yapıldı:{miktar}\nYeni Bakiye:{bakiye}")
                            else:
                                print("Yetersiz Bakiye")
                        else:
                            print("Hatalı IBAN Bilgisi!!")


                    elif secimTransfer=="2":
                        hesapNo = input("11 haneli Hesap Numarası:")
                        if len(hesapNo) == 11 and hesapNo.isdigit():
                            miktar = int(input("Transfer Edilecek Miktar:"))
                            if bakiye >= miktar:
                                bakiye -= miktar
                                print(f"Transfer Başarılı:{miktar}\nYeni Bakiye:{bakiye}")
                            else:
                                print("Yetersiz Bakiye")

                        else:
                            print("Hatalı Hesap Numarası!!")
                    else:
                        print("Hatalı Transfer Seçimi!!")


                elif anaMenuSecim=="4":
                    print("Eğitim Ödemeleri Bölümü Arızalı!!")


                elif anaMenuSecim=="5":
                    print("""
                    1-Elektrik Faturası
                    2-Doğalgaz  Faturası
                    3-Su Faturası
                    4-İnternet Faturası
                    5-HGS Ödemeleri
                    6-İstanbul Kart Yükleme""")
                    faturaSecim=input("Seçiminiz:")

                    if(faturaSecim=="1"):
                        print("Faturanız Ödendi")


                elif anaMenuSecim=="6":
                    eskiSifre = input("Eski Şifreniz")
                    if sifre==eskiSifre:
                        yeniSifre=input("Yeni Şifreniz:")
                        yeniSifre2=input("Tekrar Yeni Şifreniz:")

                        if yeniSifre==yeniSifre2:
                            print("Şifreniz güncellendi.")
                            sifre=yeniSifre
                        else:
                            print("Şifreleriniz Uyuşmuyor!!")
                    else:
                        print("Hatalı Şifre Girişi!!")


                else:
                    print("Hatalı Ana Menü Seçimi!!")

                donus=input("9-Ana Menü\n0-Çıkış\nSeçiminiz:")
                if donus=="9":
                    continue
                else:
                    hak=0
                    break

            elif hak==0:
                print("Hesabınız 5 saniye kitlenmiştir.")
                time.sleep(5)

            else:
                print("Şifreniz Hatalı!! Kalan hakkınız:",hak)

    elif kartSecim=="2":
        while True:
            print("""    
    **** Ana Menü ****
    CepBank Para Çekmek 1
    Para yatırmak için  2
    Kredi Kartı Ödeme   3
    Eğitim Ödemeleri    4
    Ödemeler            5
    Çıkış               6
            """)
            anaMenuSecim=input("Seçiminiz:")
            if anaMenuSecim=="1":
                hak=3
                while hak>0:
                    _tc=input("TC:")
                    _cepTel=input("Cep Telefon Numarası:")

                    if tc==_tc and cepTel==_cepTel:
                        bakiye-=1000
                        print("Paranızı alınız.")
                    else:
                        hak-=1
                        print("TC veya Cep Numarası yanlış Girildi!!")
                    if hak==0:
                        time.sleep(3600)

            elif anaMenuSecim=="2":
                paraYatirma=input("1-Nakit Ödeme\n2-Hesaptan Ödeme\nSeçiminiz: ")
                if paraYatirma=="1":
                    krediKartNo=input("Kredi kart numarası:")

                    if krediKartNo.isdigit() and len(krediKartNo)==12:
                        print("Ödeme işlemi başarılı")
                    else:
                        print("Yetersiz Bakiye!!")

                elif paraYatirma=="2":
                    krediKartNo = input("Kredi kart numarası:")

                    if krediKartNo.isdigit() and len(krediKartNo) == 12:
                        krediKartBorcu=float(input("Borç:"))

                        if bakiye>=krediKartBorcu:
                            bakiye-=krediKartBorcu
                            print("Kredi kartınız ödendi.","Yeni bakiyeniz:",bakiye)

                        else:
                            print("Yetersiz Bakiye!!")

                        print("Ödeme işlemi başarılı")
                    else:
                        print("Yetersiz Bakiye!!")
                else:
                    print("Hatalı Yatırma İşlem seçimi!!")

            elif anaMenuSecim == "3":
                pass
            elif anaMenuSecim == "4":
                pass
            elif anaMenuSecim == "5":
                pass
            elif anaMenuSecim == "6":
                print("Çıkış yapılıyor..")
                time.sleep(3)
                break
            else:
                print("Hatalı Menü Seçimi!!")

            donus = input("9-Ana Menü\n0-Çıkış\nSeçiminiz:")
            if donus == "9":
                continue
            else:
                break



    elif kartSecim == "3":
        print("Yine Bekleriz..")
        time.sleep(3)
        break
    else:
        print("İşlem Seçimi Hatalı!!")