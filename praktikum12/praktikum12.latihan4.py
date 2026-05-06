# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 4: Studi Kasus Jalur Terpendek Lokasi Kampus
# Algoritma: Dijkstra
# ==========================================================

import heapq

# Graph lokasi kampus
# Bobot menunjukkan waktu tempuh dalam menit
graph = {
    'Gerbang': {'Perpustakaan': 6, 'Kantin': 2},
    'Perpustakaan': {'Lab': 3},
    'Kantin': {'Lab': 4, 'Aula': 7},
    'Lab': {'Aula': 1},
    'Aula': {}
}

def dijkstra(graph, start):
    # Inisialisasi jarak awal ke semua node = tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak ke titik awal = 0
    distances[start] = 0

    # Priority queue (jarak, node)
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Lewati jika jarak tidak lebih baik
        if current_distance > distances[current_node]:
            continue

        # Cek semua tetangga
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Update jika lebih kecil
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# Menjalankan algoritma dari node 'Gerbang'
hasil = dijkstra(graph, 'Gerbang')

# Menampilkan hasil
print("Jarak terpendek dari Gerbang Kampus:")
for lokasi, jarak in hasil.items():
    print(lokasi, "=", jarak, "menit")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Lokasi mana yang paling dekat dari Gerbang?
#    Jawaban: Kantin (2 menit)

# 2. Berapa waktu tempuh terpendek dari Gerbang ke Aula?
#    Jawaban:
#    Gerbang -> Kantin -> Lab -> Aula
#    = 2 + 4 + 1 = 7 menit

# 3. Apakah jalur langsung selalu menghasilkan jarak paling kecil? Jelaskan.
#    Jawaban:
#    Tidak selalu. Jalur langsung bisa saja memiliki bobot lebih besar.
#    Contohnya, dari Kantin ke Aula langsung = 7 menit,
#    tetapi melalui Lab (Kantin -> Lab -> Aula) hanya = 4 + 1 = 5 menit.
#    Jadi jalur tidak langsung bisa lebih cepat.

# 4. Mengapa Dijkstra cocok digunakan pada kasus lokasi kampus ini?
#    Jawaban:
#    Karena semua bobot bernilai positif (waktu tempuh tidak mungkin negatif),
#    sehingga Dijkstra dapat bekerja dengan optimal dan efisien
#    untuk mencari jalur tercepat ke semua lokasi.