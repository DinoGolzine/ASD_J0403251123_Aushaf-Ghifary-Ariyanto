#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

# ==========================================================
# Latihan 5: Rotasi Kiri pada BST Tidak Seimbang
# ==========================================================

# Class Node untuk menyimpan data BST
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nilai node
        self.left = None      # Child kiri
        self.right = None     # Child kanan

# Fungsi preorder untuk melihat isi tree
def preorder(root):
    if root is not None:             # Jika node tidak kosong
        print(root.data, end=" ")    # Tampilkan data
        preorder(root.left)          # Kunjungi subtree kiri
        preorder(root.right)         # Kunjungi subtree kanan

# Fungsi untuk menampilkan struktur tree
def tampil_struktur(root, level=0, posisi="Root"):
    if root is not None:                                      # Jika node ada
        print(" " * level + f"{posisi}: {root.data}")          # Tampilkan node dengan indentasi
        tampil_struktur(root.left, level + 1, "L")             # Tampilkan subtree kiri
        tampil_struktur(root.right, level + 1, "R")            # Tampilkan subtree kanan

# Fungsi rotasi kiri
def rotate_left(x):
    y = x.right        # y adalah child kanan dari x
    T2 = y.left        # Simpan subtree kiri milik y (sementara)

    # Proses rotasi
    y.left = x         # x menjadi child kiri dari y
    x.right = T2       # Subtree kanan x diganti dengan T2

    return y           # y menjadi root baru setelah rotasi

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree yang tidak seimbang:
# 10 -> 20 -> 30 (condong ke kanan)
root = Node(10)
root.right = Node(20)
root.right.right = Node(30)

# Menampilkan sebelum rotasi
print("Preorder sebelum rotasi kiri:")
preorder(root)

print("\n\nStruktur sebelum rotasi kiri:")
tampil_struktur(root)

# Melakukan rotasi kiri pada root
root = rotate_left(root)

# Menampilkan setelah rotasi
print("\nPreorder sesudah rotasi kiri:")
preorder(root)

print("\n\nStruktur sesudah rotasi kiri:")
tampil_struktur(root)