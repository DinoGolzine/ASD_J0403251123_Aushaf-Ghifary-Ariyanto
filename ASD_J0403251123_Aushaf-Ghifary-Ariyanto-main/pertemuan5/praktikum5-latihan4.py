#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1 
#========================================================

# ==========================================================
# Latihan 4: Kombinasi Huruf
# ==========================================================

def kombinasi(n, hasil=""):                 # Fungsi rekursif untuk membuat kombinasi huruf A dan B
    if len(hasil) == n:                     # Base case: jika panjang string sudah sama dengan n
        print(hasil)                        # Cetak hasil kombinasi
        return                              # Hentikan rekursi pada cabang ini
    
    kombinasi(n, hasil + "A")               # Choose & explore huruf "A"
                                           # Tambahkan "A" lalu lanjut rekursi
    
    kombinasi(n, hasil + "B")               # Choose & explore huruf "B"
                                           # Tambahkan "B" lalu lanjut rekursi


kombinasi(2)                                # Memanggil fungsi dengan panjang kombinasi 2

# Output:
# AA
# AB
# BA
# BB


# =========================
# Penjelasan Pola Choose & Explore
# =========================

# Setiap langkah memiliki 2 pilihan (choose):
# 1. Tambah "A"
# 2. Tambah "B"

# Fungsi akan mengeksplorasi semua kemungkinan sampai panjang = n.
# Struktur percabangan membentuk pohon biner (setiap node punya 2 cabang).

# Untuk n = 2:

#          ""
#        /     \
#      A         B
#     / \       / \
#   AA  AB     BA  BB

# =========================
# Jumlah Kombinasi
# =========================

# Setiap posisi memiliki 2 pilihan (A atau B).
# Jika panjang kombinasi = n,
# maka jumlah kombinasi = 2^n.

# Untuk n = 2:
# 2^2 = 4 kombinasi

# Jika n = 3:
# 2^3 = 8 kombinasi

# Kesimpulan:
# Jumlah kombinasi bertambah secara eksponensial.
# Rumus umum: total kombinasi = 2^n.