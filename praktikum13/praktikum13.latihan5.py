#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
# Praktikum 13 - Graph III: Spanning Tree 
#========================================================
# ==========================================================
# PROGRAM MINIMUM SPANNING TREE (MST)
# Kasus 1: Jaringan Jalan Antar Kota
# Algoritma: Kruskal
# Kode ini kompatibel untuk dijalankan di VS Code (R)
# ==========================================================

# Membuat data edge (sisi) dan bobotnya
edges <- data.frame(
  from = c("Bogor", "Bogor", "Depok", "Jakarta", "Depok"),   # Kota asal
  to = c("Jakarta", "Depok", "Jakarta", "Bandung", "Bandung"), # Kota tujuan
  weight = c(5, 2, 3, 6, 4),                                 # Bobot/jarak
  stringsAsFactors = FALSE                                   # Simpan sebagai karakter
)

# Menampilkan graph awal
cat("=== Weighted Graph ===\n")
print(edges)
cat("\n")

# Mengurutkan edge berdasarkan bobot terkecil
edges_sorted <- edges[order(edges$weight), ]

# Menampilkan edge yang sudah diurutkan
cat("=== Edge Setelah Diurutkan ===\n")
print(edges_sorted)
cat("\n")

# Membuat daftar semua vertex
vertices <- unique(c(edges$from, edges$to))

# Inisialisasi parent untuk Union-Find
parent <- setNames(vertices, vertices)

# Fungsi untuk mencari root
find_root <- function(x) {
  while (parent[x] != x) {
    x <- parent[x]
  }
  return(x)
}

# Fungsi untuk menggabungkan dua set
union_set <- function(x, y) {
  root_x <- find_root(x)
  root_y <- find_root(y)

  if (root_x != root_y) {
    # <<- diperlukan agar variabel parent di luar fungsi ikut berubah
    parent[root_y] <<- root_x
  }
}

# Membuat data frame kosong untuk MST
mst <- data.frame(
  from = character(0),
  to = character(0),
  weight = numeric(0),
  stringsAsFactors = FALSE
)

# Variabel total bobot MST
total_weight <- 0

# Proses algoritma Kruskal
for (i in 1:nrow(edges_sorted)) {

  # Ambil data edge ke-i
  u <- edges_sorted$from[i]
  v <- edges_sorted$to[i]
  w <- edges_sorted$weight[i]

  # Jika tidak membentuk siklus
  if (find_root(u) != find_root(v)) {

    # Tambahkan edge ke MST
    mst <- rbind(mst, edges_sorted[i, ])

    # Gabungkan kedua vertex
    union_set(u, v)

    # Tambahkan bobot ke total
    total_weight <- total_weight + w
  }

  # Jika jumlah edge MST sudah = jumlah vertex - 1, hentikan
  if (nrow(mst) == length(vertices) - 1) {
    break
  }
}

# Menampilkan hasil MST
cat("=== Minimum Spanning Tree (MST) ===\n")
print(mst)
cat("\n")

# Menampilkan total bobot minimum
cat("Total Bobot Minimum =", total_weight, "\n\n")

# ==========================================================
# JAWABAN ANALISIS
# ==========================================================
cat("=== Jawaban Analisis ===\n")
cat("1. Kasus yang dipilih: Jaringan Jalan Antar Kota\n")
cat("2. Algoritma yang digunakan: Kruskal\n")
cat("3. Edge yang dipilih dalam MST:\n")

# Menampilkan edge yang terpilih
for (i in 1:nrow(mst)) {
  cat("   -", mst$from[i], "-", mst$to[i], "(", mst$weight[i], ")\n")
}

cat("4. Total bobot MST =", total_weight, "\n")
cat("5. Edge tertentu tidak dipilih karena membentuk siklus\n")
cat("   atau memiliki bobot lebih besar dibanding edge lain.\n")