def presjek(skup_1, skup_2):
    rezultat = set()  #  stvara novi prazan skup
    for element in skup_1:  # petljom prolazimo kroz svaki element prvog skupa
        if element in skup_2:  # ako se taj element nalazi i u drugom skupu (if element in skup_2:), 
            rezultat.add(element)  # dodajemo ga u rezultat
    return rezultat  # na kraju vraćamo novi skup koji sadrži samo zajedničke elemente

# Primjer upotrebe:
skup_1 = {1, 2, 3, 4, 5}
skup_2 = {4, 5, 6, 7, 8}
print(presjek(skup_1, skup_2))  # {4, 5}



# Kraća verzija (uz dopuštene skupovske operacije)
#def presjek(skup_1, skup_2):
    #return skup_1 & skup_2 //  # ili skup_1.intersection(skup_2)