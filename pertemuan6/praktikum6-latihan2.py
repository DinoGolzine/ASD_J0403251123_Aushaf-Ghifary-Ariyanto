#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 2 . Melengkapi Potongan Kode
#========================================================

def insertion_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data

#========================================================
#Soal:
#1. Lengkapi kondisi agar menjadi sorting ascending.
#2. Ubah agar menjadi descending.
#========================================================
#Jawab:
#.1
#def insertion_sort(data):
#   for i in range(1, len(data)):
#        key = data[i]
#        j = i - 1

#        #ascending
#        while j >= 0 and data[j] > key:
#            data[j + 1] = data[j]
#            j -= 1

#       data[j + 1] = key

#    return data

#2.
#Cukup balik operator pembanding
#while j >= 0 and data[j] < key:
    
#Kode Lengkap:
def insertion_sort_desc(data):
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1

        # descending
        while j >= 0 and data[j] < key:
            data[j + 1] = data[j]
            j -= 1

        data[j + 1] = key

    return data