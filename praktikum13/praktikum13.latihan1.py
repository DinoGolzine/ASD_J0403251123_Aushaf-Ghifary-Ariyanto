#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
# Praktikum 13 - Graph III: Spanning Tree 
#========================================================
# Daftar edge graph
edges = [
    ('A', 'B'),
    ('A', 'C'),
    ('A', 'D'),
    ('C', 'D'),
    ('B', 'D')
]

# Contoh spanning tree yang valid
spanning_tree = [
    ('A', 'C'),
    ('C', 'D'),
    ('D', 'B')
]

# Menampilkan edge pada graph
print("Edge pada graph:")
for edge in edges:
    print(edge)

# Menampilkan spanning tree
print("\nSpanning Tree:")
for edge in spanning_tree:
    print(edge)

# Menampilkan jumlah edge
print("\nJumlah edge graph =", len(edges))
print("Jumlah edge spanning tree =", len(spanning_tree))


# ==================================================
# Jawaban Analisis
# 1. Perbedaan graph awal dan spanning tree:
#    - Graph awal memiliki semua edge yang tersedia.
#    - Spanning tree hanya mengambil edge yang diperlukan
#      untuk menghubungkan semua node tanpa membentuk cycle.

# 2. Mengapa spanning tree tidak boleh memiliki cycle?
#    - Karena tujuan spanning tree adalah menghubungkan
#      semua node dengan jalur minimum.
#    - Jika ada cycle, berarti ada edge berlebih dan
#      graph tidak lagi berbentuk tree.

# 3. Mengapa jumlah edge spanning tree selalu lebih sedikit?
#    - Karena spanning tree untuk n node selalu memiliki
#      n - 1 edge.
#    - Pada graph ini ada 4 node, sehingga spanning tree
#      hanya memiliki 3 edge.
# ==================================================