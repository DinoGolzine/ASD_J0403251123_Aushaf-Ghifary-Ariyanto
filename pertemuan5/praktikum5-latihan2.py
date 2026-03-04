#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1 
#========================================================

# ==========================================================
# Latihan 2: Tracing Rekursi
# ==========================================================

def countdown(n):                          # Fungsi rekursif untuk menghitung mundur
    if n == 0:                             # Base case (kondisi berhenti)
        print("Selesai")                    # Dieksekusi saat n sudah 0
        return                              # Menghentikan pemanggilan rekursi
    
    print("Masuk:", n)                      # Dieksekusi sebelum masuk ke rekursi (fase turun)
    countdown(n - 1)                        # Pemanggilan rekursif dengan n dikurangi 1
                                            # Program masuk lebih dalam ke stack
    print("Keluar:", n)                     # Dieksekusi setelah rekursi selesai (fase naik/backtracking)


countdown(3)                                # Pemanggilan awal dengan n = 3

# Alur eksekusi:
# Masuk: 3
#   Masuk: 2
#     Masuk: 1
#       Selesai
#     Keluar: 1
#   Keluar: 2
# Keluar: 3

# Penjelasan mengapa "Keluar" muncul terbalik:
# Karena rekursi menggunakan sistem stack (LIFO = Last In First Out).
# Saat countdown(3) dipanggil, ia menunggu countdown(2) selesai.
# countdown(2) menunggu countdown(1), dan seterusnya.
# Setelah mencapai base case (n == 0), fungsi mulai selesai satu per satu dari yang terakhir dipanggil.
# Maka yang keluar pertama adalah n = 1, lalu 2, lalu 3.
# Itulah sebabnya output "Keluar" tampil dalam urutan terbalik.