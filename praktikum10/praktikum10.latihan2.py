#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

# ==========================================================
# Latihan 4: Membuat BST yang Tidak Seimbang
# ==========================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data      # Nilai/data pada node
        self.left = None      # Child kiri (default None)
        self.right = None     # Child kanan (default None)

# Fungsi insert untuk Binary Search Tree
def insert(root, data):
    if root is None:                 # Jika root kosong
        return Node(data)            # Buat node baru

    if data < root.data:             # Jika data lebih kecil
        root.left = insert(root.left, data)   # Masuk ke subtree kiri
    elif data > root.data:           # Jika data lebih besar
        root.right = insert(root.right, data) # Masuk ke subtree kanan

    return root                      # Kembalikan root

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:             # Jika node tidak kosong
        print(root.data, end=" ")    # Cetak data
        preorder(root.left)          # Kunjungi kiri
        preorder(root.right)         # Kunjungi kanan

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:                                      # Jika node ada
        print(" " * level + f"{posisi}: {root.data}")          # Tampilkan node dengan indentasi
        tampil_struktur(root.left, level + 1, "L")             # Tampilkan subtree kiri
        tampil_struktur(root.right, level + 1, "R")            # Tampilkan subtree kanan

# -----------------------------
# Program utama
# -----------------------------
root = None                             # Inisialisasi root kosong

# Data dimasukkan berurutan naik
data_list = [10, 20, 30]

# Insert data ke BST
for data in data_list:
    root = insert(root, data)

# Menampilkan hasil preorder
print("Preorder BST:")
preorder(root)

# Menampilkan struktur tree
print("\n\nStruktur BST:")
tampil_struktur(root)