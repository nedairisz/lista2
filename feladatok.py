import math

# 1. Írd ki a képernyőre a lista elemeit
# Írj metódust amely a paraméterében kapott lista elemeit kiírja a képernyőre
def feladat1(szam_lista):
    for i in range (0,len(szam_lista),1):
        print(f"A lista {i}. eleme: {szam_lista[i]}")

# 2. Mennyi a pozitív számok összege? - összegzés
def feladat2(szam_lista):
    gyujto = 0 
    i = 0
    while i < len(szam_lista):
        if (szam_lista[i]) > 0:
            gyujto += i
        i += 1
    return gyujto
        

# 3. Hány negatív szám van? - megszámlálás
def feladat3(szam_lista):
    gyujto = 0
    i = 0
    while i < len(szam_lista):
        if (szam_lista[i]) < 0:
            gyujto += 1
        i += 1
    return gyujto


# 4. Hány nem egész szám van a számok között? - összegzés - megszámlálás
def feladat4(szam_lista):
    gyujto = 0
    i: int = 0
    while i < len(szam_lista):
        if szam_lista[i] != math.floor(szam_lista[i]):
            gyujto += 1
        i += 1
    return gyujto


# 5. Mennyi a hárommal osztható számok átlaga?
def feladat5(szam_lista):
    gyujto = 0
    atlag = 0
    db = 0
    i: int = 0
    while i < len(szam_lista):
        if szam_lista[i] % 3 == 0:
            gyujto += szam_lista[i]
            db += 1
        i += 1
    atlag = gyujto/db
    return atlag

# 6. Mekkora a legnagyobb szám? - max
def feladat6(szam_lista):
    max = szam_lista[0]
    for i in range(0,len(szam_lista),1):
        if max < szam_lista[i]:
            max = szam_lista[i]
    return max

# 7. Mekkora a legkisebb szám? - min
def feladat7(szam_lista):
    min = szam_lista[0]
    for i in range(0,len(szam_lista),1):
        if min > szam_lista[i]:
            min = szam_lista[i]
    return min


# 8. Mekkora a legkisebb és a legnagyobb szám különbsége?
def feladat8(szam_lista):
    kulonbseg= feladat6(szam_lista)-feladat7(szam_lista)
    return kulonbseg