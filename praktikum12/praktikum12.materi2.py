# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path 
# Materi 2
# Fungsi untuk menghitung jarak terpendek menggunakan algoritma Bellman-Ford
def bellman_ford(graph, start):
    # Inisialisasi jarak semua node ke tak hingga (infinity)
    # Artinya, pada awalnya belum diketahui jalur ke node tersebut
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Proses relaksasi dilakukan sebanyak (jumlah node - 1) kali
    # Hal ini karena jalur terpanjang dalam graf tanpa siklus memiliki maksimal (V-1) edge
    for _ in range(len(graph) - 1):
        # Iterasi setiap node dalam graf
        for node in graph:
            # Iterasi setiap tetangga dari node tersebut
            for neighbor, weight in graph[node].items():
                # Jika jarak ke node sekarang tidak tak hingga (artinya bisa dicapai)
                if distances[node] != float('inf'):
                    # Cek apakah jalur melalui node ini lebih pendek
                    if distances[node] + weight < distances[neighbor]:
                        # Jika ya, perbarui jarak ke neighbor
                        distances[neighbor] = distances[node] + weight

    # (Opsional) Deteksi siklus negatif
    # Jika masih bisa dilakukan relaksasi, berarti terdapat negative cycle
    for node in graph:
        for neighbor, weight in graph[node].items():
            if distances[node] != float('inf'):
                if distances[node] + weight < distances[neighbor]:
                    print("Graph mengandung siklus negatif!")
                    return None

    # Mengembalikan hasil jarak terpendek
    return distances


# Contoh graf dengan kemungkinan bobot negatif
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'C': -3, 'D': 2},
    'C': {'D': 3},
    'D': {}
}

# Menjalankan algoritma Bellman-Ford dari node 'A'
hasil = bellman_ford(graph, 'A')

# Menampilkan hasil
print("Jarak terpendek dari node A ke semua node:")
print(hasil)