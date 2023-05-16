def numerolojiGoster(sonuc):
    if sonuc == "1":
        print("Numeroloji sisteminde 1 sayısının anlamı; Bağımsızlık, yaratıcılık, kendine düşkünlük, ego olarak ifade edilir. Kişi hem kendine yeterli hem de tam bir liderdir. Yani liderliği temsil eder. İş yaşamında acelecilik, aşırılık ve hükmedici davranışlardan kaçınması kişi adına fayda sağlayabilir.")
    elif sonuc == "2":
        print("Numeroloji sisteminde 2 sayısının anlamı; Kişilik özellikler; bağımlılık, aşırı duyarlılık, kavrama ve tasarım, iş birlik anlayışı ve sezgi yeteneği gelişmiştir. Kişi sevgi dolu, eleştirici ve barış yanlısı, ideal ortaktır. Detaylara takılmaktan ve yalnızlıktan kaçınmalıdır.")
    elif sonuc == "3":
        print("Numeroloji sisteminde 3 sayısının anlamı; Numerolojide 3 rakamı; sosyal, arkadaş canlısı, sanata yatkın, iyimser, ziyankarlık, yüzeysellik anlamlarına gelir. Dışa dönük bir kişidir. Yaşamı ve eğlenceyi sever. Oldukça yaratıcı ve duyarlıdır. Rutini sevmez. Kendine disiplin uygulamayı benimsemesi gerekir.")
    elif sonuc == "4":
        print("Numeroloji sisteminde 4 sayısının anlamı; Numerolojide 4 sayısı sağlam, pratik, uygulayıcı, bükülmez ve sıkı bir çalışan anlamına gelir. Her konuda başarıyı yakalamak ister. Candan ve iyi bir arkadaş olma konusunda yardıma ihtiyacı vardır. Aşırı güvenlik duygusuna kapılmamalıdır.")
    elif sonuc == "5":
        print("Numeroloji sisteminde 5  sayısının anlamı; Özgürlük, gezginlik, uyum kabiliyeti, değişkenlik gibi karakteristik özellikler numerolojide bu rakamın karşılığı olarak bilinmektedir. İkna edici bir kişiliğe sahiptir ve cesur bir kişiliktir. Can sıkıntısı olumsuz etkiler. Amacından kolayca sapması söz konusudur.")
    elif sonuc == "6":
        print("Numeroloji sisteminde 6 sayısının anlamı;Anlayış, aşk, sorumluluk, kıskançlık, her işe müdahale etmek gibi özelliklere sahiptir. Oldukça sıcak, koruyucu ve mutlu bir kişiliğe sahiptir. Sevdikleri için fedakarlık yapmaktan çekinmez. Sağlam ve güvenilir bir yapısı bulunur. Kendini kötümser bir ruh haline sokmaktan ve başkaları tarafından istismar edilen duygularından arınmış olmalıdır.")
    elif sonuc == "7":
        print("Numeroloji sisteminde 7  sayısının anlamı;Bu rakam; sır saklama, zeka, ruhsallık ve baskıcılığı ifade eder. Düşünür bir kişiliğe sahiptir. Değişken ve eksantriktir. Mesafeli ve soğuk olmaktan kaçınmalıdır. Ayrıca iyi şeylere sahip olmama duygusu ve yalnızlıktan kaçınmalıdır.")
    elif sonuc == "8":
        print("Numeroloji sisteminde 8 sayısının anlamı; Organizasyon yeteneğine sahip, güçlü, yönetici ruha sahip ve oldukça adildir. Sonuca giden bir kişiliğe sahiptir. Bu bağlamda her zaman kararlı ve güçlü yapısı ile ön plana çıkmaktadır. Özellikle maddi konularda başarılıdır. Hedefinin karşısında gördüğü kişilere karşı duygusuzca davranmaktan kaçınması gerekir.")
    elif sonuc == "9":
        print("Numeroloji sisteminde 9  sayısının anlamı; Hümanist, romantik, şefkatli, duygusal, sanatkar, sezgili, duyarlı, yaratıcı ve konforuna düşkündür. Kendini anlatmak adına tüm dünya ile savaşabilir. Kötü alışkanlıklarından arınmak ve yaşamın küçük detaylarından olumsuz etkilenmemek adına gayret göstermesi gerekir.")
    elif sonuc == "11":
        print("Numeroloji sisteminde 11  sayısının anlamı;Duyarlı, fanatik ve sezgi gücü yüksektir. Ayrıca keşif yeteneğine sahiptir. Öngörülü ve hayalci bir kişiliğe sahiptir. Bilinç üstü gelişmiştir ve sanatkardır. Aşırı duyarlılık ve gerginlik halinden uzak durmalıdır. ")
    elif sonuc == "22":
        print("Numeroloji sisteminde 22 sayısının anlamı; Numerolojide 22 rakamının anlamı; maddi alanda üstün, zenginliğe kolay ulaşabilen, oldukça pratik bir idealist olarak tanımlanır. Amacına doğru ilerler ve eli çabuktur. Düşünce tarzı globaldir. Geleceğe fazla düşünmekten kaçınmalıdır.")



def integerYap(stringNumber):
    stringNumber = stringNumber.strip()
    return int(stringNumber) if stringNumber else 0

def topla(stringNumber):
    toplam=0
    for chr in stringNumber:
        toplam+=int(chr)
    return toplam

while(True):
    try:
        dogumGunu = str(input("Doğum gününüzü  giriniz (gg.aa.yyyy): \n "))
        if "." not in dogumGunu:
            print("Lütfen Doğum Gününüzü Doğru giriniz.")
            continue
        tarihSplit = dogumGunu.split(".")

        if(integerYap(tarihSplit[0])>31 or integerYap(tarihSplit[0])<1):
            print("Ayın Günleri 31'i Geçmemeli , 0 olamaz. boşluk girmeyiniz. Lütfen tekrar deneyiniz\n")
            continue
        if (integerYap(tarihSplit[1]) > 12 or integerYap(tarihSplit[1])<1):
            print("Yılın Ayları 12'i Geçemez. Lütfen tekrar deneyiniz\n")
            continue
        if (integerYap(tarihSplit[2]) < 1000):
            print("Lütfen Yılı Doğru Giriniz.\n")
            continue

        toplam = topla(tarihSplit[0])
        toplam += topla(tarihSplit[1])
        toplam += topla(tarihSplit[2])
        while(toplam>9 and toplam !=11 and toplam !=22):
            toplam = topla(str(toplam))
        numerolojiGoster(str(toplam))
    except:
        print("Hata Oluştu Lütfen Doğru Bir Şekilde Tekrar Deneyiniz")

