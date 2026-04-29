#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================
# Latihan 1 : BFS
#========================================================
from collections import deque  # import deque untuk antrian (queue) pada BFS

graph = {  # representasi graph dalam bentuk dictionary (adjacency list)
    'Rumah': ['Sekolah', 'Toko'],  # node Rumah terhubung ke Sekolah dan Toko
    'Sekolah': ['Perpustakaan'],   # Sekolah terhubung ke Perpustakaan
    'Toko': ['Pasar'],             # Toko terhubung ke Pasar
    'Perpustakaan': [],            # tidak ada tetangga
    'Pasar': []                    # tidak ada tetangga
}

def bfs(graph, start):  # fungsi BFS dengan parameter graph dan node awal
    visited = set()  # set untuk menyimpan node yang sudah dikunjungi
    queue = deque([start])  # queue (antrian) dimulai dari node awal
    visited.add(start)  # tandai node awal sebagai sudah dikunjungi

    while queue:  # selama queue tidak kosong
        node = queue.popleft()  # ambil node paling depan dari queue
        print(node, end=" ")  # tampilkan node

        for neighbor in graph[node]:  # loop semua tetangga dari node
            if neighbor not in visited:  # cek jika belum dikunjungi
                visited.add(neighbor)  # tandai sebagai dikunjungi
                queue.append(neighbor)  # masukkan ke queue untuk diproses

print("BFS dari Rumah:")  # output judul
bfs(graph, 'Rumah')  # panggil fungsi BFS mulai dari 'Rumah'

# =======================
# Jawaban Analisis:
# 1. Node pertama yang dikunjungi adalah "Rumah"
#    karena BFS dimulai dari node awal (start).
#
# 2. BFS cocok untuk mencari jalur terdekat karena:
#    BFS bekerja secara level (lapisan).
#    Semua node dengan jarak 1 dikunjungi dulu,
#    kemudian jarak 2, dan seterusnya.
#    Sehingga jalur pertama yang ditemukan adalah yang paling pendek.
#
# 3. Jika struktur graph berubah:
#    - Urutan kunjungan bisa berubah tergantung urutan neighbor
#    - Tetapi BFS tetap menjamin menemukan jalur terpendek