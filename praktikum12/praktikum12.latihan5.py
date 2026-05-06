# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path
# ==========================================================
# Latihan 5: Studi Kasus Shortest Path Antar Kota
# Algoritma: Dijkstra
# ==========================================================

import heapq

# 1. Representasi graph berbobot menggunakan dictionary
# Bobot menunjukkan jarak/waktu tempuh antar kota
graph = {
    'Bogor': {'Jakarta': 5, 'Depok': 2},
    'Depok': {'Jakarta': 2, 'Bandung': 6},
    'Jakarta': {'Bandung': 7},
    'Bandung': {}
}

# 2. Fungsi Dijkstra
def dijkstra(graph, start):
    # Inisialisasi semua jarak ke tak hingga
    distances = {node: float('inf') for node in graph}

    # Jarak ke node awal = 0
    distances[start] = 0

    # Priority queue untuk memilih node dengan jarak terkecil
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Jika jarak saat ini lebih besar dari yang sudah dicatat, lewati
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            distance = current_distance + weight

            # Jika ditemukan jarak lebih kecil, update
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


# 3. Penentuan node awal
start_node = 'Bogor'

# Menjalankan algoritma
hasil = dijkstra(graph, start_node)

# 4. Output hasil
print("Jarak terpendek dari Bogor:")
for kota, jarak in hasil.items():
    print(f"{start_node} -> {kota} = {jarak}")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Node awal yang digunakan apa?
#    Jawaban: Bogor

# 2. Node mana yang memiliki jarak paling kecil dari node awal?
#    Jawaban: Depok (2)

# 3. Node mana yang memiliki jarak paling besar dari node awal?
#    Jawaban: Bandung (8)

# 4. Jelaskan bagaimana algoritma Dijkstra bekerja pada kasus yang Anda buat.
#    Jawaban:
#    Algoritma Dijkstra bekerja dengan memilih node dengan jarak terkecil
#    dari node awal, lalu memperbarui jarak ke tetangganya (relaksasi).
#    Pada kasus ini:
#    - Dari Bogor, pertama dipilih Depok (2), bukan Jakarta (5)
#    - Dari Depok, ditemukan jalur lebih pendek ke Jakarta (2 + 2 = 4)
#      dibandingkan langsung dari Bogor (5)
#    - Kemudian dihitung jalur ke Bandung:
#      Bogor -> Depok -> Bandung = 2 + 6 = 8
#    - Semua node diproses hingga diperoleh jarak minimum ke setiap kota