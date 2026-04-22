#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

# ==========================================================
# Latihan 6: Rotasi Kanan pada BST Tidak Seimbang
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
        tampil_struktur(root.left, level + 1, "L")             # Subtree kiri
        tampil_struktur(root.right, level + 1, "R")            # Subtree kanan

# Fungsi rotasi kanan
def rotate_right(y):
    x = y.left        # x adalah child kiri dari y
    T2 = x.right      # Simpan subtree kanan milik x (sementara)

    # Proses rotasi
    x.right = y       # y menjadi child kanan dari x
    y.left = T2       # Subtree kiri y diganti dengan T2

    return x          # x menjadi root baru setelah rotasi

# -----------------------------
# Program utama
# -----------------------------

# Membuat tree tidak seimbang:
# 30 -> 20 -> 10 (condong ke kiri)
root = Node(30)
root.left = Node(20)
root.left.left = Node(10)

# Sebelum rotasi
print("Preorder sebelum rotasi kanan:")
preorder(root)

print("\n\nStruktur sebelum rotasi kanan:")
tampil_struktur(root)

# Melakukan rotasi kanan pada root
root = rotate_right(root)

# Setelah rotasi
print("\nPreorder sesudah rotasi kanan:")
preorder(root)

print("\n\nStruktur sesudah rotasi kanan:")
tampil_struktur(root)