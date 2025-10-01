#program kt zisti ci je cislo prvocislo ak ano true  inak false
number=int(input("Zadaj cislo: "))
countNumber=0
for delitel in range (2,number) :
    if number % delitel == 0 :
        countNumber += 1 #zvacsi premenu o 1
if countNumber == 0 :
    print("Nie je to prvocislo")
else :
    print("Nie je to prvocislo")
    