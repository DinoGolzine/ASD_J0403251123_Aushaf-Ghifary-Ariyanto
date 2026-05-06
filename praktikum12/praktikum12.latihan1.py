# Nama  : Aushaf Ghifary Ariyanto
# NIM   : J0403251123
# Kelas : TPL_B1
# Praktikum 12 - Graph II: Shortest Path 
# ==========================================================
# Latihan 1: Weighted Graph dan Perhitungan Jalur
# ==========================================================

# Representasi weighted graph menggunakan dictionary bersarang
graph = {
    'A': {'B': 4, 'C': 2},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

# Menghitung dua kemungkinan jalur dari A ke D
jalur_1 = graph['A']['B'] + graph['B']['D']  # A -> B -> D
jalur_2 = graph['A']['C'] + graph['C']['D']  # A -> C -> D

# Menampilkan hasil perhitungan bobot
print("Jalur 1: A -> B -> D =", jalur_1)
print("Jalur 2: A -> C -> D =", jalur_2)

# Menentukan jalur terpendek
if jalur_1 < jalur_2:
    print("Jalur terpendek adalah A -> B -> D")
else:
    print("Jalur terpendek adalah A -> C -> D")


# ==========================================================
# Jawaban Analisis:
# ==========================================================

# 1. Berapa total bobot jalur A -> B -> D?
#    Jawaban: 4 + 5 = 9

# 2. Berapa total bobot jalur A -> C -> D?
#    Jawaban: 2 + 1 = 3

# 3. Jalur mana yang dipilih sebagai jalur terpendek?
#    Jawaban: A -> C -> D, karena memiliki total bobot lebih kecil (3)

# 4. Mengapa jalur terpendek tidak selalu ditentukan dari jumlah edge yang paling sedikit?
#    Jawaban:
#    Karena setiap edge memiliki bobot (weight) yang berbeda.
#    Jalur dengan jumlah edge lebih sedikit bisa saja memiliki total bobot lebih besar.
#    Sebaliknya, jalur dengan edge lebih banyak bisa lebih ringan jika bobot tiap edge kecil.
#    Oleh karena itu, yang diperhitungkan adalah total bobot, bukan jumlah edge.