class ciro():
    def adambasiciro(toplamciro,toplamcalisansayisi):
        adambasiciro=toplamciro/toplamcalisansayisi
        return adambasiciro
    toplamciro=int(input("toplam cironuzu giriniz:"))
    toplamcalisansayisi=int(input("toplam çalışan sayısını giriniz:"))
    adambasiciro(toplamciro,toplamcalisansayisi)
    adambasiciro=toplamciro/toplamcalisansayisi
    print("adam başına düşen ciro miktarınız:")
    print(adambasiciro)
