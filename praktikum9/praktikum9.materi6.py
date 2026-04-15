#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 5 . Membuat Struktur Organisasi Perusahaan
#========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
        
#Fungsi preorder: root -> left -> right
def preorder(node):
    if node is not None:
        print(node.data, end=" ") # Kunjungi root
        preorder(node.left) # Kunjungi subtree kiri
        preorder(node.right) # Kunjungi subtree kanan
        
#Membuat tree organisasi perusahaan
root = Node("Direktur")

#child level 1
root.left = Node("Manajer A")
root.right = Node("Manajer B")

#child level 2
root.left.left = Node("Karyawan A1")
root.left.right = Node("Karyawan A2")
root.right.left = Node("Karyawan B1")

# Menampilkan struktur organisasi
print("Struktur Organisasi Perusahaan:")
preorder(root)

# Penjelasan struktur organisasi perusahaan di atas memiliki Direktur sebagai root, dengan dua Manajer (Manajer A dan Manajer B) sebagai child level 1.
# Manajer A memiliki dua Karyawan (Karyawan A1 dan Karyawan A2) sebagai child level 2, sedangkan Manajer B memiliki satu Karyawan (Karyawan B1) sebagai child level 2.
# Traversal pre-order digunakan untuk menampilkan struktur organisasi dengan mengunjungi root terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan.