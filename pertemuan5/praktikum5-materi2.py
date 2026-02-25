#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Materi Rekursif : Call Stack
# Tracing bilangan (masuk-keluar) 
# input 3
# Masuk 1 - 2 - 3
# Keluar
#========================================================

def hitung(n):
    
    #base case
    if n == 0:
        print("Selesai")
        return
    
    print("Masuk:", n)
    hitung(n-1) #Recursive case
    print("Keluar", n)

print("====== Program Tracing ======")
hitung(5)   