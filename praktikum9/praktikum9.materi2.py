#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 2 . Membuat Binary search tree
#========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
        
# Membuat root
root = Node("A")

# Membuat child level 1
root.left = Node("B")
root.right = Node("C")

# Membuat child level 2
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menampilkan isi node
print("Data pada root: ", root.data)
print("Data kiri root: ", root.left.data)
print("Data kanan root: ", root.right.data)
print("Data kiri dari B: ", root.left.left.data)
print("Data kanan dari B: ", root.left.right.data)
print("Data kiri dari C: ", root.right.left.data)
print("Data kanan dari C: ", root.right.right.data)

# Lanjutkan kode program nya untuk keseluruhan tree --> tambahkan child di sisi kanan dari node D, E, F, dan G sesuai dengan kebutuhan.

# Penjelasan: Pada latihan ini, kita membuat sebuah kelas Node yang memiliki atribut data untuk menyimpan nilai node,
# serta left dan right untuk menyimpan referensi ke child kiri dan kanan. Kemudian kita membuat sebuah tree dengan root "A" dan menambahkan child di level 1 dan level 2.
# Terakhir, kita menampilkan isi dari node-node tersebut untuk memastikan bahwa tree telah terbentuk dengan benar.