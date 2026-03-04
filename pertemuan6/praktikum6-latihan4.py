#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 4 . Memahami Kode Program (Merge Sort)
#========================================================

#def merge_sort(data):
#   if len(data) <= 1:
#        return data

#    mid = len(data) // 2
#    left = data[:mid]
#    right = data[mid:]

#    left_sorted = merge_sort(left)
#    right_sorted = merge_sort(right)

#    return merge_sort(left_sorted, right_sorted)

#========================================================
#Soal:
#1. Apa yang dimaksud dengan base case?
#2. Mengapa fungsi memanggil dirinya sendiri?
#3. Apa tujuan fungsi merge()?
#========================================================
#Jawab:
#1. Base case adalah kondisi yang menghentikan rekursi.
#Dalam kode:
#if len(data) <= 1:
    #return data

#Artinya, jika list berisi 0 atau 1 elemen, maka list tersebut sudah otomatis terurut, sehingga tidak perlu dipecah lagi. Tanpa base case, fungsi akan memanggil dirinya tanpa henti (infinite recursion)

#2. Fungsi memanggil dirinya sendiri karena merge sort menggunakan algoritma rekursif. Tujuan pemanggilan diri sendiri adalah memecah data menjadi bagian yang lebih kecil

#3. Menggabungkan dua list yang sudah terurut. Merge() akan membandingkan elemen pertama dari kedua list, memilih yang lebih kecil, lalu memasukkannya ke list baru hingga semua elemen habis
