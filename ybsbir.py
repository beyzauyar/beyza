class ybsbir():
    def eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi):
        global eo
        eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    begenisayisi=365000
    yorumsayisi=65000
    paylasimsayisi=870
    iceriksayisi=500
    takipcisayisi=1125000
    eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi)
    eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    print(eo)
    if (eo<0.20):
        print("başarılı")
    else:
        print("başarısız")
