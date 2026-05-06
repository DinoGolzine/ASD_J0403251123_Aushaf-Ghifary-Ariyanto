# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 3: Implementasi Bellman-Ford
# ==========================================================

# Weighted graph dengan bobot negatif
graph = {
    'A': {'B': 5, 'C': 4},
    'B': {},
    'C': {'B': -2}
}

def bellman_ford(graph, start):
    """
    Fungsi untuk mencari jarak terpendek dari node start
    ke seluruh node lain menggunakan algoritma Bellman-Ford.
    """

    # Semua jarak awal dibuat tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak dari start ke start adalah 0
    distances[start] = 0

    # Bellman-Ford melakukan relaksasi sebanyak jumlah node - 1
    for _ in range(len(graph) - 1):

        # Periksa semua edge
        for node in graph:
            for neighbor, weight in graph[node].items():

                # Jika jarak ke node saat ini sudah diketahui,
                # dan ditemukan jarak yang lebih kecil ke neighbor,
                # maka lakukan update jarak
                if distances[node] != float('inf') and distances[node] + weight < distances[neighbor]:
                    distances[neighbor] = distances[node] + weight

    return distances


# Menjalankan algoritma
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A:")
for node, distance in hasil.items():
    print(node, "=", distance)


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa bobot langsung dari A ke B?
#    Jawaban: 5

# 2. Berapa total bobot jalur A -> C -> B?
#    Jawaban: 4 + (-2) = 2

# 3. Jalur mana yang menghasilkan jarak lebih kecil menuju B?
#    Jawaban: Jalur A -> C -> B, karena total bobotnya 2
#    lebih kecil dibandingkan jalur langsung A -> B (5)

# 4. Mengapa Bellman-Ford dapat digunakan pada graph dengan bobot negatif?
#    Jawaban:
#    Karena Bellman-Ford tidak langsung menetapkan jarak final dalam satu langkah,
#    tetapi melakukan relaksasi berulang kali sehingga tetap bisa menemukan
#    jarak minimum meskipun terdapat bobot negatif.

# 5. Apa yang dimaksud dengan proses relaksasi edge?
#    Jawaban:
#    Relaksasi adalah proses memperbarui jarak suatu node jika ditemukan
#    jalur yang lebih pendek melalui edge tertentu.

# 6. Apa perbedaan utama Bellman-Ford dan Dijkstra?
#    Jawaban:
#    - Bellman-Ford dapat menangani bobot negatif, sedangkan Dijkstra tidak.
#    - Bellman-Ford lebih lambat (O(V * E)), sedangkan Dijkstra lebih cepat
#      dengan bantuan priority queue (O((V + E) log V)).
#    - Bellman-Ford dapat mendeteksi siklus negatif, sedangkan Dijkstra tidak.