#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
# Praktikum 13 - Graph III: Spanning Tree 
#========================================================
# ==========================================
# STUDI KASUS: JARINGAN KABEL ANTAR GEDUNG
# Menggunakan Algoritma Kruskal (Minimum Spanning Tree)
# ==========================================

# Daftar edge dalam format: (biaya, gedung1, gedung2)
edges = [                              # Menyimpan semua hubungan antar gedung beserta biayanya
    (4, "GedungA", "GedungB"),         # Edge A-B dengan biaya 4
    (2, "GedungA", "GedungC"),         # Edge A-C dengan biaya 2
    (3, "GedungB", "GedungD"),         # Edge B-D dengan biaya 3
    (1, "GedungC", "GedungD"),         # Edge C-D dengan biaya 1
    (5, "GedungA", "GedungD")          # Edge A-D dengan biaya 5
]

# Daftar semua gedung (vertex)
vertices = ["GedungA", "GedungB", "GedungC", "GedungD"]   # Menyimpan semua simpul graf

# Struktur parent untuk Union-Find
parent = {}                           # Dictionary untuk menyimpan parent setiap vertex

# Inisialisasi setiap vertex menjadi parent dirinya sendiri
for v in vertices:                    # Melakukan perulangan untuk setiap gedung
    parent[v] = v                     # Parent awal dari setiap gedung adalah dirinya sendiri

# Fungsi untuk mencari root (induk utama)
def find(v):                          # Fungsi find untuk mencari root dari vertex
    if parent[v] != v:                # Jika parent bukan dirinya sendiri
        parent[v] = find(parent[v])   # Path compression untuk mempercepat pencarian
    return parent[v]                  # Mengembalikan root dari vertex

# Fungsi untuk menggabungkan dua himpunan
def union(v1, v2):                    # Fungsi union untuk menyatukan dua set
    root1 = find(v1)                  # Mencari root dari vertex pertama
    root2 = find(v2)                  # Mencari root dari vertex kedua
    if root1 != root2:                # Jika kedua vertex berada pada set yang berbeda
        parent[root2] = root1         # Menggabungkan root2 ke root1
        return True                   # Mengembalikan True karena union berhasil
    return False                      # Mengembalikan False jika sudah berada pada set yang sama

# Mengurutkan edge berdasarkan biaya terkecil
edges.sort()                          # Mengurutkan list edge secara ascending berdasarkan biaya

# Menyimpan hasil Minimum Spanning Tree (MST)
mst = []                              # List untuk menyimpan edge yang terpilih
total_biaya = 0                       # Variabel untuk menyimpan total biaya minimum

# Proses algoritma Kruskal
for biaya, u, v in edges:             # Mengambil setiap edge yang sudah diurutkan
    if union(u, v):                   # Jika edge tidak membentuk siklus
        mst.append((u, v, biaya))     # Menambahkan edge ke MST
        total_biaya += biaya          # Menambahkan biaya edge ke total biaya

# Menampilkan hasil edge yang dipilih
print("Edge yang dipilih untuk jaringan kabel minimum:")   # Menampilkan judul output
for u, v, biaya in mst:               # Perulangan untuk setiap edge dalam MST
    print(f"{u} - {v} = {biaya}")     # Menampilkan edge beserta biayanya

# Menampilkan total biaya minimum
print("\nTotal biaya minimum:", total_biaya)   # Menampilkan jumlah total biaya

# ==========================================
# Jawaban Analisis:
# 1. Algoritma yang digunakan adalah Kruskal.
# 2. Edge yang dipilih:
#    - GedungC - GedungD = 1
#    - GedungA - GedungC = 2
#    - GedungB - GedungD = 3
# 3. Total biaya minimum = 6
# 4. MST cocok digunakan karena:
#    - Menghubungkan semua gedung.
#    - Tidak membentuk siklus.
#    - Memberikan total biaya paling kecil.
# ==========================================