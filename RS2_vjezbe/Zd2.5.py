rijeci = [
    "jabuka", "pas", "knjiga", "zvijezda", "prijatelj", 
    "zvuk", "čokolada", "ples", "pjesma", "otorinolaringolog"
]

min_duljina = int(input("Unesite minimalnu duljinu riječi: "))
# primjer: min_duljina = 7

duge_rijeci = list(filter(lambda r: len(r) > min_duljina, rijeci))
# filter() prolazi kroz sve riječi u listi rijeci.
# lambda r: len(r) > min_duljina vraća True samo za one riječi koje su dulje od zadane duljine.
# list(...) pretvara filter objekt u listu

print(duge_rijeci)
# ['zvijezda', 'prijatelj', 'čokolada', 'otorinolaringolog']
