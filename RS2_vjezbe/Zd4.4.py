import math

class Krug:
    def __init__(self, r): # __init__ postavlja atribut r (radijus kruga)
        self.r = r

    def opseg(self): # opseg() računa opseg po formuli 2𝜋𝑟
        return 2 * math.pi * self.r  # math.pi daje vrijednost konstante π

    def povrsina(self): # povrsina() računa površinu po formuli 𝜋𝑟2
        return math.pi * self.r ** 2


# Primjer korištenja:
k = Krug(5)  # proizvoljan radijus, npr. 5

print(f"Opseg kruga: {k.opseg():.2f}")
print(f"Površina kruga: {k.povrsina():.2f}")
