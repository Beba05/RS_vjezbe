# kraća verzija pomoću dictionary comprehensiona

def grupiraj_po_paritetu(lista):
    return {
        'parni': [x for x in lista if x % 2 == 0],
        'neparni': [x for x in lista if x % 2 != 0]
    }

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(grupiraj_po_paritetu(lista))