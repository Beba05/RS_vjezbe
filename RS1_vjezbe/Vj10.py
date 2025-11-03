def brojanje_riječi(tekst):
    rijeci = tekst.split()  # tekst.split() razdvaja rečenicu po razmacima u listu riječi
    frekvencija = {}  # svaka riječ se koristi kao ključ u rječniku 'frekvencija'

    for rijec in rijeci:
        if rijec in frekvencija:
            frekvencija[rijec] += 1  # ako se riječ već pojavila → povećavamo vrijednost za 1
        else:
            frekvencija[rijec] = 1  # ako nije → postavljamo početnu vrijednost na 1

    return frekvencija


# Primjer upotrebe:
tekst = "Python je programski jezik koji je jednostavan za učenje i korištenje. Python je vrlo popularan."
print(brojanje_riječi(tekst))