#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
# Praktikum 13 - Graph III: Spanning Tree 
#========================================================
# =========================================================
# Implementasi Sederhana Algoritma Kruskal
# =========================================================

# Daftar edge: (bobot, node1, node2)
edges = [
    (1, 'C', 'D'),
    (2, 'A', 'C'),
    (3, 'B', 'D'),
    (4, 'A', 'B'),
    (5, 'A', 'D')
]

# Mengurutkan edge berdasarkan bobot terkecil
edges.sort()

mst = []
total_weight = 0

connected = set()

for weight, u, v in edges:

    # Memilih edge yang tidak membentuk cycle sederhana
    if u not in connected or v not in connected:

        mst.append((u, v, weight))
        total_weight += weight

        connected.add(u)
        connected.add(v)

# Menampilkan hasil MST
print("Minimum Spanning Tree:")

for edge in mst:
    print(edge)

print("\nTotal bobot =", total_weight)


# ==================================================
# Jawaban Analisis
# 1. Edge mana yang dipilih pertama kali?
#    - Edge ('C', 'D') dengan bobot 1,
#      karena memiliki bobot paling kecil.

# 2. Mengapa edge dengan bobot paling kecil dipilih lebih dahulu?
#    - Karena algoritma Kruskal bekerja dengan prinsip greedy,
#      yaitu memilih edge dengan bobot terkecil terlebih dahulu
#      agar total bobot MST menjadi minimum.

# 3. Berapa total bobot MST yang dihasilkan?
#    - Total bobot MST adalah 6.
#    - Edge yang terpilih:
#         ('C', 'D', 1)
#         ('A', 'C', 2)
#         ('B', 'D', 3)

# 4. Mengapa edge tertentu tidak dipilih?
#    - Karena edge tersebut dapat membentuk cycle
#      atau tidak diperlukan lagi setelah semua node
#      sudah terhubung.
# ==================================================