# 1. Hány Alma/alma van a listában?
def szoveg_feladat1(szoveg_lista):
    db = 0
    i = 0
    while i < len(szoveg_lista):
        if szoveg_lista[i] == "Alma" or szoveg_lista[i] == "alma":
            db += 1
        i += 1
    return db

# 2. Hány Sz betűvel kezdődő van a listában? 
def szoveg_feladat2(szoveg_lista):
    db = 0 
    i = 0
    while i < len(szoveg_lista):
        if szoveg_lista[i][0:2] == "Sz":
            db += 1
        i += 1 
    return db

# 3. Melyik a leghoszabb szó?
# Mekkora a hossza?
# Hányadik helyen áll a listában?
def szoveg_feladat3(szoveg_lista):
    leghosszabb = szoveg_lista[0]
    i = 0
    while i < len(szoveg_lista):
        if leghosszabb < szoveg_lista[i]:
            leghosszabb = szoveg_lista[i]
        i +=1