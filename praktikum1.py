#Praktikun 1 : Konsep ADT dan File Handling
#Latihan Dasar 1 : Membaca Seluruh isi file
#=========================================

#membuka file dengan read "r"
with open("datamahasiswa.txt", 'r', encoding='utf-8') as file:
  isi_file = file.read()
print(isi_file)
print('======= Hasil Read =======')
print("Tipe Data:", type(isi_file))
print("Jumlah Karakter", len(isi_file))
print("jumlah baris", isi_file.count("\n")+1)

#Membuka file perbaris
print("===Membaca File per Baris===")
jumlah_baris = 0
with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        jumlah_baris = jumlah_baris + 1
        baris = baris.strip()
        print("Baris ke-", jumlah_baris)
        print ("Isinya", baris)
        
#Praktikun 1 : Konsep ADT dan File Handling
#Latihan Dasar 2 : presing perbaris menjadi kolom data
#=========================================
with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
      baris = baris.strip()
      nim, nama, nilai = baris.split(',')
      print('NIM : ', nim,"| NAMA : ", nama,"| NILAi : ", nilai)
      
#Praktikun 1 : Konsep ADT dan File Handling
#Latihan Dasar 3 : Membaca file dan menyimpan file
#=========================================
data_list = []
with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(',')
        data_list.append([nim,nama,int(nilai)])
        
print("==== Data Mahasiswa Dalam List ====")
print(data_list)

print("==== Jumlah Record Dalam List ====")
print("Jumlah Record", len(data_list))

print("==== Menampilkan Data Record Tertentu ====")
print('Contoh Record Pertama: ', data_list[0])

#Praktikun 1 : Konsep ADT dan File Handling
#Latihan Dasar 4 : Membaca file dan menyimpan file ke dictionary
#=========================================
data_dict = {} #buat variabel untuk dictionary
with open("datamahasiswa.txt","r", encoding="utf-8") as file:
    for baris in file:
        baris = baris.strip()
        nim, nama, nilai = baris.split(",")
        #Simpan data mahasiswa ke dictionary dengan key NIM
        data_dict[nim] = {
            "nama":nama,
            "nilai": int(nilai)
        }
print("\n==== Data Mahasiswa dalam Dictionary ===")
print(data_dict)