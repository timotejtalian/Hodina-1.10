#spocitaj parne cisla y intervalu <zaciatok, koniec>
zaciatok=int(input("Masukkan angka: "))
koniec=int(input("Masukkan angka: "))
suma=0
pocet=0
for cislo in range(zaciatok, koniec+1):
    if cislo % 2 == 0:
        suma += cislo
        pocet += 1
print("Suma parnych cisel v intervale je:", suma)