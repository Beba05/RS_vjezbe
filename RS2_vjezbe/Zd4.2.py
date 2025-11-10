import math

class Kalkulator:
    def __init__(self, a, b): # __init__: konstruktor koji postavlja vrijednosti a i b
        self.a = a
        self.b = b

    # Svaka metoda vraća rezultat odgovarajuće matematičke operacije
    def zbroj(self):
        return self.a + self.b

    def oduzimanje(self):
        return self.a - self.b

    def mnozenje(self):
        return self.a * self.b

    # U metodama dijeljenje i korijen dodana je provjera da se izbjegnu matematičke greške
    def dijeljenje(self):
        if self.b != 0:
            return self.a / self.b
        else:
            return "Greška: dijeljenje s nulom nije dopušteno!"

    def potenciranje(self):
        return self.a ** self.b

    def korijen(self):
        if self.a >= 0:
            return math.sqrt(self.a)
        else:
            return "Greška: ne može se izračunati korijen negativnog broja!"


# 🔹 Primjer korištenja:
k = Kalkulator(9, 3)

print("Zbroj:", k.zbroj())               # 12
print("Oduzimanje:", k.oduzimanje())     # 6
print("Množenje:", k.mnozenje())         # 27
print("Dijeljenje:", k.dijeljenje())     # 3.0
print("Potenciranje:", k.potenciranje()) # 729
print("Korijen:", k.korijen())           # 3.0
