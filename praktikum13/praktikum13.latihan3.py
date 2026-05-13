#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
# Praktikum 13 - Graph III: Spanning Tree 
#========================================================
# =========================================================
# Implementasi Algoritma Prim
# =========================================================

import heapq

graph = {
    'A': {'B': 4, 'C': 2, 'D': 5},
    'B': {'A': 4, 'D': 3},
    'C': {'A': 2, 'D': 1},
    'D': {'A': 5, 'B': 3, 'C': 1}
}

def prim(graph, start):

    visited = set([start])
    edges = []

    # Memasukkan edge dari node awal ke priority queue
    for neighbor, weight in graph[start].items():
        heapq.heappush(edges, (weight, start, neighbor))

    mst = []
    total_weight = 0

    while edges:

        weight, u, v = heapq.heappop(edges)

        # Jika node belum dikunjungi
        if v not in visited:

            visited.add(v)

            mst.append((u, v, weight))
            total_weight += weight

            # Menambahkan edge baru dari node yang dipilih
            for neighbor, w in graph[v].items():

                if neighbor not in visited:
                    heapq.heappush(edges, (w, v, neighbor))

    return mst, total_weight


# Menjalankan algoritma Prim dari node A
mst, total = prim(graph, 'A')

print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("\nTotal bobot =", total)


# ==================================================
# Jawaban Analisis
# 1. Node awal apa yang digunakan?
#    - Node awal yang digunakan adalah node 'A'.

# 2. Edge mana yang dipilih pertama kali?
#    - Edge ('A', 'C') dengan bobot 2,
#      karena merupakan bobot terkecil dari node awal A.

# 3. Bagaimana Prim menentukan edge berikutnya?
#    - Prim memilih edge dengan bobot paling kecil
#      yang menghubungkan node yang sudah dikunjungi
#      dengan node yang belum dikunjungi.

# 4. Berapa total bobot MST yang dihasilkan?
#    - Total bobot MST adalah 6.
#    - Edge yang dipilih:
#         ('A', 'C', 2)
#         ('C', 'D', 1)
#         ('D', 'B', 3)

# 5. Apa perbedaan pendekatan Prim dan Kruskal?
#    - Prim membangun MST mulai dari satu node
#      lalu memperluas ke node lain secara bertahap.
#
#    - Kruskal memilih edge dengan bobot terkecil
#      secara global tanpa memulai dari node tertentu.
# ==================================================