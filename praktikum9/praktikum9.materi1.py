#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 1 . Membuat Node
#========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
    
# Membuat root
root = Node("A")
    
# Menampilkan isi node
print("Data pada root: ", root.data)
print("Data kiri root: ", root.left)
print("Data child kanan root: ", root.right)

# Penjelasan: Pada latihan ini, kita membuat sebuah kelas Node yang memiliki atribut data untuk menyimpan nilai node,
# serta left dan right untuk menyimpan referensi ke child kiri dan kanan. Kemudian kita membuat sebuah node root dengan nilai "A" dan menampilkan isi dari node tersebut.