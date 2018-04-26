def kvyk(a,s):
    global kvyk
    kvyk=a+s
    return kvyk
print("III.KISA VADELİ YABANCI KAYNAK")
a=int(input("300 bankalar hesabı................"))
s=int(input("320 satıcılar hesabı..............."))
kvyk(a,s)
kvyk=a+s
print(kvyk)
def uvyk(d,f):
    global uvyk
    uvyk=d+f
    return uvyk
print("IV.UZUN VADELİ YABANCI KAYNAK")
d=int(input("400 banka kredileri hesabı.........."))
f=int(input("421 borç senetleri hesabı..........."))
print("V.ÖZ KAYNAKLAR")
g=int(input("500 sermaye hesabı.................."))
uvyk(d,f)
uvyk=d+f
print(uvyk)
def pasif(kvyk,uvyk,g):
    global pasif
    pasif=kvyk+uvyk+g
    return pasif
print("pasifler toplamı:")
pasif(kvyk,uvyk,g)
pasif=kvyk+uvyk+g
print(pasif)
