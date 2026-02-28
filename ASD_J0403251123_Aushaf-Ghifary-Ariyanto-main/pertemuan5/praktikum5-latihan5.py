#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1 
#========================================================

# ==========================================================
# Studi Kasus: Generator PIN
# ==========================================================

def buat_pin(panjang, hasil=""):                 # Fungsi backtracking untuk membuat semua kemungkinan PIN
    if len(hasil) == panjang:                    # Base case: jika panjang PIN sudah sesuai
        print("PIN:", hasil)                     # Cetak PIN
        return                                   # Hentikan cabang ini
    
    for angka in ["0", "1", "2"]:                # Pilihan angka yang bisa digunakan
        buat_pin(panjang, hasil + angka)         # Choose & explore → tambah angka lalu lanjut rekursi


buat_pin(3)                                      # Membuat semua PIN 3 digit

# Jumlah kombinasi:
# Setiap digit memiliki 3 pilihan (0,1,2)
# Total kemungkinan = 3^3 = 27 kombinasi


# ==========================================================
# Diskusi: Mencegah angka yang sama muncul berulang
# ==========================================================

# Pada kode di atas, angka boleh berulang.
# Contoh hasil: 000, 011, 222, dll.

# Jika ingin MENCEGAH angka yang sama muncul lebih dari sekali
# (misalnya tidak boleh 00 atau 121 karena ada angka berulang),
# maka kita perlu mengecek sebelum menambahkan angka.

# Contoh modifikasi:

def buat_pin_unik(panjang, hasil=""):            # Versi tanpa angka berulang
    if len(hasil) == panjang:
        print("PIN:", hasil)
        return
    
    for angka in ["0", "1", "2"]:
        if angka not in hasil:                   # Cegah angka yang sudah dipakai
            buat_pin_unik(panjang, hasil + angka)


# Jika panjang = 3 dan angka hanya 0,1,2,
# maka semua digit harus berbeda.
# Jumlah kemungkinan menjadi 3! = 6 kombinasi:
# 012, 021, 102, 120, 201, 210


# ==========================================================
# Kesimpulan
# ==========================================================

# Dengan pengulangan:
# Total = 3^n  (karena setiap posisi punya 3 pilihan)

# Tanpa pengulangan:
# Total = permutasi
# Untuk 3 digit unik dari 0,1,2 → 3! = 6

# Cara mencegah angka berulang:
# Tambahkan kondisi:
# if angka not in hasil
# sebelum melakukan recursive call.