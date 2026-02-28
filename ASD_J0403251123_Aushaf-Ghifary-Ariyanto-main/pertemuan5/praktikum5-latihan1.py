#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1 
#========================================================

#==========================================================
# Latihan 1: Rekursi Pangkat
#==========================================================

def pangkat(a, n):                     #Fungsi untuk menghitung a^n secara rekursif
    # Base case
    if n == 0:                         #Jika pangkat = 0 (kondisi berhenti)
        return 1                       #Semua bilangan berpangkat 0 bernilai 1
    
    # Recursive case
    return a * pangkat(a, n - 1)       #Mengalikan a dengan hasil pangkat(a, n-1)
                                       #Fungsi memanggil dirinya sendiri
                                       #Nilai n dikurangi 1 setiap pemanggilan
                                       #Proses berlanjut sampai n == 0

print(pangkat(2, 4))                   #Memanggil fungsi dengan a=2 dan n=4
                                       #Alur:
                                       #2 * pangkat(2,3)
                                       #2 * (2 * pangkat(2,2))
                                       #2 * (2 * (2 * pangkat(2,1)))
                                       #2 * (2 * (2 * (2 * pangkat(2,0))))
                                       #2 * 2 * 2 * 2 * 1
                                       #Hasil akhir = 16