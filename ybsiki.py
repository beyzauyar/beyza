class ybsiki():
    def eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi):
        global eo
        eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    begenisayisi=450000
    yorumsayisi=25000
    paylasimsayisi=380
    iceriksayisi=100
    takipcisayisi=1450000
    eo(begenisayisi,yorumsayisi,paylasimsayisi,iceriksayisi,takipcisayisi)
    eo=(((begenisayisi+yorumsayisi+paylasimsayisi)/iceriksayisi)/takipcisayisi)*100
    print(eo)
    if (eo>0.20):
        print("başarılı")
    else:
        print("başarısız")
