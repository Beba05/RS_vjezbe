import heapq

def dijkstra(graph, start):
    # 1️. Inicijalizacija udaljenosti — svi beskonačni osim početnog
    udaljenosti = {cvor: float('inf') for cvor in graph}
    udaljenosti[start] = 0

    # 2️. Prioritetni red (min-heap) — sadrži (udaljenost, čvor)
    red = [(0, start)]

    while red:
        trenutna_udaljenost, trenutni_cvor = heapq.heappop(red)

        # Ako imamo staru (lošiju) udaljenost, preskačemo
        if trenutna_udaljenost > udaljenosti[trenutni_cvor]:
            continue

        # 3️. Prolazimo sve susjede trenutnog čvora
        for susjed, tezina in graph[trenutni_cvor]:
            nova_udaljenost = trenutna_udaljenost + tezina

            # Ako smo pronašli kraći put — ažuriraj i dodaj u red
            if nova_udaljenost < udaljenosti[susjed]:
                udaljenosti[susjed] = nova_udaljenost
                heapq.heappush(red, (nova_udaljenost, susjed))

    return udaljenosti


#  Primjer grafa:
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 5)],
    'C': [('A', 4), ('B', 2), ('D', 1)],
    'D': [('B', 5), ('C', 1)]
}

#  Poziv funkcije:
print(dijkstra(graph, 'A'))