#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================
# Latihan 1 : DFS
#========================================================
graph = {  # representasi graph dalam bentuk dictionary
    'A': ['B', 'C'],  # A terhubung ke B dan C
    'B': ['D', 'E'],  # B terhubung ke D dan E
    'C': ['F'],       # C terhubung ke F
    'D': [],          # tidak ada tetangga
    'E': [],          # tidak ada tetangga
    'F': []           # tidak ada tetangga
}

def dfs(graph, node, visited):  # fungsi DFS (rekursif)
    visited.add(node)  # tandai node sebagai dikunjungi
    print(node, end=" ")  # tampilkan node

    for neighbor in graph[node]:  # loop semua tetangga
        if neighbor not in visited:  # jika belum dikunjungi
            dfs(graph, neighbor, visited)  # rekursi ke node tersebut

visited = set()  # set untuk menyimpan node yang sudah dikunjungi
print("DFS dari A:")  # output judul
dfs(graph, 'A', visited)  # panggil DFS dari node A

# =======================
# Jawaban Analisis:
# 1. DFS masuk ke node terdalam terlebih dahulu karena:
#    DFS menggunakan rekursi (stack),
#    sehingga akan terus masuk ke cabang paling dalam
#    sebelum kembali (backtracking).
#
# 2. Jika urutan neighbor diubah:
#    - Urutan hasil DFS juga berubah
#    - DFS sangat bergantung pada urutan neighbor
#
# 3. Perbandingan BFS vs DFS:
#    BFS:
#      - Menelusuri per level
#      - Cocok untuk mencari jalur terpendek
#
#    DFS:
#      - Menelusuri sampai dalam dulu
#      - Cocok untuk eksplorasi semua jalur
#
#    Contoh:
#      BFS: A B C D E F
#      DFS: A B D E C F