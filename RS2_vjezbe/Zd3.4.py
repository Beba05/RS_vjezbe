import math

korijeni = {x: round(math.sqrt(x), 2) for x in range(50, 501, 50)}
# range(50, 501, 50) daje brojeve 50, 100, 150, …, 500.
# math.sqrt(x) računa kvadratni korijen broja x.
# round(..., 2) zaokružuje rezultat na dvije decimale.
# {x: ... for x in ...} je dictionary comprehension koji stvara parove ključ–vrijednost

print(korijeni)
# {50: 7.07, 100: 10.0, 150: 12.25, 200: 14.14, 250: 15.81, 300: 17.32, 350: 18.71, 400: 20.0, 450: 21.21, 500: 22.36}
