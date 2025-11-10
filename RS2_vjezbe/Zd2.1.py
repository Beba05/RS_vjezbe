nizovi = ["jabuka", "kruška", "banana", "naranča"]

# map() prima funkciju i kolekciju (u ovom slučaju listu nizovi)
# lambda s: len(s) ** 2 je anonimna funkcija koja za svaki string s vraća kvadrat njegove duljine
# list(...) pretvara rezultat map objekta u listu
kvadrirane_duljine = list(map(lambda s: len(s) ** 2, nizovi))  

print(kvadrirane_duljine)  # [36, 36, 36, 49]
