
def sinyalGucu(num):
    sonuc = ""
    if num <= 255:
        if num >= 201:
            sonuc = "Çok Güçlü Sinyal"
        elif num >= 151:
            sonuc = "Güçlü Sinyal"
        elif num >= 101:
            sonuc = "Orta Sinyal"
        elif num >= 51:
            sonuc = "Zayıf Sinyal"
        elif num >= 0:
            sonuc = "Çok Zayıf Sinyal"
        if sonuc != "":
            sonuc = str(num) + " - " + sonuc
    return sonuc

def cihazlar(c):
    sonuc = ""
    if c == 1:
        sonuc = "Televizyon"
    elif c == 2:
        sonuc = "Camasir Makinesi"
    elif c == 3:
        sonuc = "Buzdolabı"
    elif c == 4:
        sonuc = "Firin"
    if sonuc != "":
        sonuc = str(c) + " - " + sonuc
    return sonuc
    
def durum(d):
    sonuc = ""
    if d == 0:
        sonuc = "Off"
    elif d == 1:
        sonuc = "On"
    if sonuc != "":
        sonuc = str(d) + " - " + sonuc
    return sonuc

def cevap(c):
    sonuc = ""
    if c == 0:
        sonuc = "Cevap istenmiyor"
    elif c == 1:
        sonuc = "Cevap isteniyor"
    if sonuc != "":
        sonuc = str(c) + " - " + sonuc
    return sonuc


def komutParcalayici(komut):
    komutParcasi = komut.split("-")

    hata = ""
    kodTipi = ""
    sinyalGucuVal =""
    cihazlarVal = ""
    durumVal = ""
    cevapVal = ""

    if komutParcasi[0] == "send":
        if len(komutParcasi) != 5:
            hata = "send 5 parametreden oluşmalıdır"
        else:
            kodTipi = "send - Giden"
        
    elif komutParcasi[0] == "receive":
        if len(komutParcasi) != 4:
            hata = "receive 4 parametreden oluşmalıdır"
        else:
            kodTipi = "receive - Gelen"
    else:
        hata = "ERROR : send ya da receive icermiyor"


    if hata == "":
        if len(komutParcasi) == 5:
            if komutParcasi[4].isdigit() :
                cevapVal = cevap(int(komutParcasi[4]))
            if cevapVal == "":
                hata = "Error : besinci bolum hatali"

        if komutParcasi[3].isdigit():
            durumVal = durum(int(komutParcasi[3]))
        if durumVal == "" :
            hata = "Error : dorduncu bolum hatali"

        if komutParcasi[2].isdigit():
            cihazlarVal = cihazlar(int(komutParcasi[2]))
        if cihazlarVal == "":
            hata = "Error : ucuncu bolum hatali"

        if komutParcasi[1].isdigit():
            sinyalGucuVal = sinyalGucu(int(komutParcasi[1]))
        if sinyalGucuVal == "":
            hata = "Error : ikinci bolum hatali"        
    
    return hata, kodTipi, sinyalGucuVal, cihazlarVal, durumVal, cevapVal


##PROGRAM START
girilenDeger=input("İfade : ")
gelenIfadeler = girilenDeger.split("\\n")
if gelenIfadeler[len(gelenIfadeler) -1] == "":
    gelenIfadeler.remove(gelenIfadeler[len(gelenIfadeler) -1])

for index, i in enumerate(gelenIfadeler):
    hata, kodTipi, sinyalGucuVal, cihazlarVal, durumVal, cevapVal = komutParcalayici(i)
    if hata != "":
        print(hata)
    else:
        print("Kod Tipi : {}".format(kodTipi))
        print("Sinyal Gucu : {}".format(sinyalGucuVal))
        print("Cihaz : {}".format(cihazlarVal))
        print("Durumu : {}".format(durumVal))
        if kodTipi == "send - Giden":
            print("Cevap : {}".format(cevapVal))
    
    if  index != len(gelenIfadeler)-1:
        print("------")

input()


##
#cihazs = {
#    "1" = "Televizyon",
#    "2" = "Çamaşır Makinesi",
#    "3" = "Buzdolabı",
#    "4" = "Fırın"
#}