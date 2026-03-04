#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1 
#========================================================

# ==========================================================
# Latihan 3: Mencari Nilai Maksimum
# ==========================================================

def cari_maks(data, index=0):                  # Fungsi rekursif untuk mencari nilai maksimum dalam list
    # Base case
    if index == len(data) - 1:                 # Jika sudah di elemen terakhir
        return data[index]                     # Kembalikan nilai elemen terakhir (tidak ada pembanding lagi)
    
    # Recursive case
    maks_sisa = cari_maks(data, index + 1)     # Panggil fungsi untuk mencari maksimum dari sisa list (index+1)
                                               # Fungsi terus maju sampai elemen terakhir
    
    if data[index] > maks_sisa:                # Bandingkan elemen sekarang dengan maksimum sisa list
        return data[index]                     # Jika lebih besar, kembalikan elemen sekarang
    else:
        return maks_sisa                       # Jika tidak, kembalikan maksimum dari sisa list


angka = [3, 7, 2, 9, 5]                        # List data yang akan dicari nilai maksimumnya
print("Nilai maksimum:", cari_maks(angka))     # Memanggil fungsi, output: 9


# =========================
# Penjelasan Alur Program
# =========================

# Pemanggilan awal:
# cari_maks([3,7,2,9,5], 0)

# Proses turun (rekursi maju sampai base case):
# index 0 → panggil index 1
# index 1 → panggil index 2
# index 2 → panggil index 3
# index 3 → panggil index 4
# index 4 → Base case tercapai → return 5

# Proses naik (backtracking/perbandingan):
# index 3 → bandingkan 9 dengan 5 → return 9
# index 2 → bandingkan 2 dengan 9 → return 9
# index 1 → bandingkan 7 dengan 9 → return 9
# index 0 → bandingkan 3 dengan 9 → return 9

# Hasil akhir: 9


# =========================
# Kesimpulan
# =========================
# Base Case:
# Terjadi saat index berada di elemen terakhir.
# Mengembalikan nilai tersebut sebagai dasar perbandingan.

# Recursive Case:
# Fungsi memanggil dirinya sendiri dengan index + 1.
# Setelah mencapai base case, nilai dibandingkan satu per satu saat kembali (naik).
# Proses naik inilah yang menentukan nilai maksimum akhir.