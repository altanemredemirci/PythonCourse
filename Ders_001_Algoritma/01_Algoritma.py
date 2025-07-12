# Tek Satır Açıklama

"""
Çoklu
    Açıklama
        Satırı
"""

'''
Çoklu Açıklama
    Satırı
'''

'''
Programlama Dili: PYTHON-Yapay zeka geliştirme alanlarında kullanılır.
Compiler - Derleyiciler( PyCharm, VSCode, Anaconda ) : Geliştirilen projede,
        *Kodlama hatalarını
        *İmla kontrollerini
        *Referans(kaynak) alınan dosyaların erişilebilirliğini
        *Çalıştırılan projenin çalıştığı donanımın yeterliliğini
        *Yazılan kodun makine koduna dönüştürülmesini sağlar.
        *Sonucu kullanıcıya gösterme-
        
** Yazılımın akışı client-server (istemci-sunucu) arasında geçer. Çalışma stratejiside her kullanıcı isteğini(request) alıp cevap(result) vermek üzerine geliştirilir. 

** Yazılım dillerinde küçük harf BÜYÜK HARF duayarlılığı vardır.
** Yazılım dillerinde yapı isimlendirilirken benzersiz olmalıdır.

not1=65
not2=78
'''
######          Algoritma           ######
'''
Algoritma: Bir sorunu çözmek veya belirlenmiş bir amaca ulaşmak için tasarlanan yola,
takip edilen işlem basamaklarına denir. Algoritmalar açıkça belirtilmiş bir başlangıcı
ve sonu olan işlemler kümesidir.

Amaca ulaşmak için işlenecek çözüm yolları ve sıralamaları belirlenir ve algoritma bu sırayı takip ederek en mantıklı
çözüme ulaşır.


    Giriş/Çıkış Bilgisi: Algoritmalarda giriş ve çıkış bilgileri olmalıdır. Dışarıdan gelen verilere giriş bilgisi denir.
        Bu veriler algoritmada işlenir ve çıkış bilgisini oluşturur. Çıkış bilgisi her algoritmada mutlaka vardır.
        Algoritmaların temel amacı giriş bilgisini işleyerek çıkış bilgisi oluşturmaktır.

    Sonluluk: Her türlü olasılık için algoritma sonlu adımda bitmelidir. Algoritma sonsuz döngüye girmemelidir.
        Başı ve sonu belli olmalıdır.
    Kesinlik: Her komut kişinin kalem ve kağıt ile yürütebileceği kadar basit olmalıdır. Algoritmanın her adımı anlaşılır,
        basit ve kesin bir biçimde ifade edilmiş olmalıdır. Kesinlikle yorum gerektirmemeli ve belirsiz ifadelere sahip
        olmamalıdır.
    Etkinlik: Yazılan algoritmalar etkin ve dolayısıyla gereksiz tekrarlardan uzak oluşturulmalıdır.
        Bu algoritmanın temel özelliklerinden birisidir. Ayrıca algoritmalar genel amaçlı yazılıp yapısal bir ana
        algoritma ve alt algoritmalardan oluşturulmalıdır.
        Böylece daha önce yazılmış bir algoritma daha sonra başka işlemler için de kullanılabilir.
        Buna örnek vermek gerekirse eğer elimizde, verilen n adet sayının ortalamasını bulmakta kullandığımız algoritma
        varsa bu algoritma, bir sınıfta öğrencilerin yaş ortalamasını bulan bir algoritma için de kullanılabilmelidir.
    Başarım ve Performans: Amaç donanım gereksinimi (bellek kullanımı gibi), çalışma süresi gibi performans kriterlerini
        dikkate alarak yüksek başarımlı programlar yazmak olmalıdır. Gereksiz tekrarlar ortadan kaldırılmalıdır.
        Bir algoritmanın performans değerlendirmesinde aşağıdaki temel kriterler göz önünde bulundurulur.
            Birim İşlem Zamanı
            Veri Arama ve Getirme Zamanı
            Kıyaslama Zamanı
            Aktarma Zamanı
'''


### ÇAY DEMLEME ALGORİTMASI
"""
1-Başla
2-Mutfağa Git
3-Çaydanlığa Su Koy
4-Ocağı Yak
5-Su Kaynadı Mı? T->7 F->6
6-Bekle(3dk) ->5
7-Demliğe Çay Koy
8-Çaydanlığa Su Koy
9-Çaydanlığı Ocağa Koy
10-Çay Demlendi Mi? T->12 F->11
11-Bekle(3dk) ->10
12-Ocağı Kapat
13-Servis Et
14-Bitti

## Sonluluk Maddesine Aykırı Olasıklar
**Çay Yok
**Su Yok
**Bakkal Kapalı


1-Başla
2-Mutfağa Git
3-Su ve Çay Var Mı? T->9 F->4
4-Bakkala Git
5-Bakkal Açık Mı? T->7 F->6
6-Başka Bakkala Git -> 5
7-Eksikleri Al
8-Eve Dön -> 2
9-Çaydanlığa Su Koy
10-Ocağı Yak
11-Su Kaynadı Mı? T->13 F->12
12-Bekle ->11
13-Demliğe Çay Koy
14-Çaydanlığa Su Koy
15-Çaydanlığı Ocağa Koy
16-Çay Demlendi Mi? T->18 F->17
17-Bekle(3dk) ->16
18-Ocağı Kapat
19-Servis Et
20-Bitti
"""

"""
İki kardeşin yaşları toplamını ekrana yazdırınız.
1-Başla
2-1.kardeşin yaşı:
3-2.kardeşin yaşı:
4-1.yaş + 2.yaş
5-Toplamını ekrana yaz
6-Bitti 


"""
# sayi1 = input("1.yaş girin :")
# sayi2 = input("2.yaş girin :")
#
# topla = int(sayi1)+int(sayi2)
# print("Toplam :",topla)

"""
Console.WriteLine("1.yaş:");
string y1 = Console.ReadLine();

Console.WriteLine("2.yaş:")
string y1 = Console.ReadLine();

int toplam = Convert.ToInt32(y1);+Convert.ToInt32(y2);
Console.WriteLine("Toplam:"+toplam)
"""

"""
EVDEN ÜÇÜNCÜBİNYIL AKADEMİYE GELME ALGORİTMASI
1-Başla
2-Daireden Çık
3-Asansör Mü? Merdiven Mi? A->4 M->11
4-Asansör Katta Mı? F->5 T->6
5-Asansörü Çağır ->4
6-Asansöre Bin
7-İstenilen Kat Tuşuna Bas
8-Asansör İstenilen Katta Mı? T->10 F->9
9-Bekle -> 8
10-Asansörden İn->13
11-Aşağı Mı Yukarı Mı?
12-Bir Kat Hareket Et
13-İstenilen Katta Mıyız? F->12 T->14
14-Binadan Çık


14-Akbil Dolu Mu? F->15 T->16
15-Akbil Doldur
16-Toplu Taşıma Durağına Git
17-İstenilen Taşıt Geldi Mi? F->18 T->19 
18-Bekle -> 17
19-Taşıta Bin
20-Akbil Bas
21-Boş Yer Var Mı? F->22 T->23
22-Ayakta Git ->24
23-Otur
24-İstenilen Durağına Geldi Mi? F->25 T->26
25-Bekle ->24
26-Taşıttan İn
27-Akademiye Yürü
28-Bitti
"""








