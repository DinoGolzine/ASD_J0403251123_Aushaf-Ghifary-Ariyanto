#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 3 . Membuat Traversal pre-order
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
        
# Membuat tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal pre-order
print("Pre-order traversal:")
preorder(root)

# penjelasan pre-order traversal mengunjungi root terlebih dahulu, kemudian subtree kiri, dan terakhir subtree kanan.
# Pada contoh di atas, urutan kunjungan adalah A (root), B (subtree kiri), D (subtree kiri dari B), E (subtree kanan dari B), C (subtree kanan),
# F (subtree kiri dari C), dan G (subtree kanan dari C).