#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

# ==========================================================
# Latihan 1: Node dan Insert BST
# ==========================================================

# Membuat class Node untuk setiap elemen dalam Binary Search Tree
class Node:
    def __init__(self, data):
        self.data = data      # Menyimpan nilai/data node
        self.left = None      # Pointer ke anak kiri (default None)
        self.right = None     # Pointer ke anak kanan (default None)

# Fungsi untuk memasukkan data ke dalam BST
def insert(root, data):
    if root is None:                # Jika root kosong
        return Node(data)           # Buat node baru dan jadikan root

    if data < root.data:            # Jika data lebih kecil dari root
        root.left = insert(root.left, data)   # Masukkan ke subtree kiri
    elif data > root.data:          # Jika data lebih besar dari root
        root.right = insert(root.right, data) # Masukkan ke subtree kanan

    return root                     # Kembalikan root setelah insert

# Membuat BST (Binary Search Tree)
root = None                         # Inisialisasi root kosong

# Data yang akan dimasukkan ke BST
data_list = [50, 30, 70, 20, 40, 60, 80]

# Melakukan insert setiap data ke dalam BST
for data in data_list:
    root = insert(root, data)       # Update root setiap insert

# Menampilkan pesan jika BST berhasil dibuat
print("BST berhasil dibuat")

# ==========================================================
# Latihan 2: Traversal Inorder
# ==========================================================

# Fungsi untuk melakukan traversal inorder pada BST
def inorder(root):
    if root is not None:            # Jika node tidak kosong
        inorder(root.left)          # Kunjungi subtree kiri terlebih dahulu
        print(root.data, end=" ")   # Tampilkan data node
        inorder(root.right)         # Kunjungi subtree kanan

# Menampilkan hasil traversal inorder
print("Hasil inorder:")

# Memanggil fungsi inorder dengan root BST
inorder(root)

# ==========================================================
# Latihan 3: Search BST
# ==========================================================

# Fungsi untuk mencari nilai (key) dalam Binary Search Tree
def search(root, key):
    if root is None:                # Jika node kosong (tidak ditemukan)
        return False               # Kembalikan False

    if root.data == key:           # Jika data pada node sama dengan key
        return True                # Data ditemukan, kembalikan True

    elif key < root.data:          # Jika key lebih kecil dari data node
        return search(root.left, key)   # Cari di subtree kiri

    else:                          # Jika key lebih besar dari data node
        return search(root.right, key)  # Cari di subtree kanan

# ==========================================================
# Uji pencarian
# ==========================================================

key = 10                           # Nilai yang ingin dicari

# Mengecek apakah key ada di dalam BST
if search(root, key):
    print("Data ditemukan")        # Jika ditemukan
else:
    print("Data tidak ditemukan")  # Jika tidak ditemukan