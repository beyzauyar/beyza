class ybsuc():
    def eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi):
        global eo
        eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    begenisayisi=582000
    yorumsayisi=52000
    paylasimsayisi=1200
    iceriksayisi=650
    takipcisayisi=2000000
    eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi)
    eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    print(eo)
    if (eo<0.20):
        print("başarılı")
    else:
        print("başarısız")
