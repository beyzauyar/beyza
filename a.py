def donenvarliklar(q,w,e,r,t):
    global donenvarliklar
    donenvarliklar=q+w+e+r+t
    return donenvarliklar
print("I.DÖNEN VARLIKLAR")
q=int(input("100 kasa hesabı..................."))
w=int(input("101 alınan çekler hesabı.........."))
e=int(input("102 bankalar hesabı..............."))
r=int(input("121 alacak senetleri hesabı......."))
t=int(input("153 ticari mallar hesabı.........."))
donenvarliklar(q,w,e,r,t)
donenvarliklar=q+w+e+r+t
print(donenvarliklar)
def duranvarliklar(y,u,o):
    global duranvarliklar
    duranvarliklar=y+u+o
    return duranvarliklar
print("II.DURAN VARLIKLAR")
y=int(input("252 binalar hesabı................"))
u=int(input("254 taşıtlar hesabı..............."))
o=int(input("255 demirbaşlar hesabı............"))
duranvarliklar(y,u,o)
duranvarliklar=y+u+o
print(duranvarliklar)
def aktifler(donenvarliklar,duranvarliklar):
    global aktifler
    aktifler=donenvarliklar+duranvarliklar
    return aktifler
print("aktifler toplamı:")
aktifler(donenvarliklar,duranvarliklar)
aktifler=donenvarliklar+duranvarliklar
print(aktifler)
