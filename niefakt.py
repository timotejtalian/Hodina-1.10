zaciatok=int(input("Masukkan angka: "))
koniec=int(input("Masukkan angka: "))
vystup=0
for i in range(zaciatok,koniec+1):
    vystup=vystup*i #vystup*=i
print(vystup)
