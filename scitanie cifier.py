#scitavanie cifier yadaneho cisla
x=int(input("Masukkan angka: "))
sucet_cifier = 0
while x != 0:
    cifra = x % 10
    sucet_cifier += cifra
    x //= 10 #x = x // 10
print("Suma cifier je: ",sucet_cifier)
