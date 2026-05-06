# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path 
# Materi 1
# Mengimpor modul heapq untuk membuat priority queue (antrian prioritas)
import heapq

# Representasi graf dalam bentuk dictionary
# Setiap node memiliki tetangga dan bobot (weight) ke tetangga tersebut
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

def dijkstra(graph, start):
    # Inisialisasi jarak semua node ke tak hingga (infinity)
    # Artinya belum ada jalur yang diketahui
    distances = {node: float('inf') for node in graph}

    # Jarak dari node awal ke dirinya sendiri adalah 0
    distances[start] = 0

    # Priority queue untuk memilih node dengan jarak terkecil
    # Format: (jarak, node)
    pq = [(0, start)]

    # Selama masih ada node dalam antrian
    while pq:
        # Mengambil node dengan jarak terkecil
        current_distance, current_node = heapq.heappop(pq)

        # Jika jarak saat ini lebih besar dari yang sudah tercatat, abaikan
        if current_distance > distances[current_node]:
            continue

        # Periksa semua tetangga dari node saat ini
        for neighbor, weight in graph[current_node].items():
            # Hitung jarak baru melalui node saat ini
            distance = current_distance + weight

            # Jika jarak baru lebih kecil, perbarui
            if distance < distances[neighbor]:
                distances[neighbor] = distance

                # Masukkan ke priority queue untuk diproses selanjutnya
                heapq.heappush(pq, (distance, neighbor))

    # Mengembalikan hasil jarak terpendek dari node awal ke semua node
    return distances


# Menjalankan fungsi Dijkstra dengan titik awal 'A'
hasil = dijkstra(graph, 'A')

# Menampilkan hasil jarak terpendek
print("Jarak terpendek dari node A ke semua node:")
print(hasil)