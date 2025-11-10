from functools import reduce

brojevi = [10, 5, 12, 15, 20]

# reduce() postupno “skuplja” elemente iz liste u jedan rezultat (ovdje rječnik).
# acc (akumulator) je dosadašnji rječnik, x je trenutni broj.
# {**acc, x: x**2} stvara novi rječnik koji sadrži sve prethodne parove i dodaje novi.
# Početna vrijednost (initializer) je prazan rječnik {}
transform = reduce(lambda acc, x: {**acc, x: x**2}, brojevi, {})

print(transform)  # {10: 100, 5: 25, 12: 144, 15: 225, 20: 400}
