#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 4 . Membuat Traversal in-order
#========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
        
#Fungsi inorder: left -> root -> right
def inorder(node):
    if node is not None:
        inorder(node.left) # Kunjungi subtree kiri
        print(node.data, end=" ") # Kunjungi root
        inorder(node.right) # Kunjungi subtree kanan
        
# Membuat tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal in-order
print("In-order traversal:")
inorder(root)

# Penjelasan in-order traversal mengunjungi subtree kiri terlebih dahulu, kemudian root, dan terakhir subtree kanan.
# Pada contoh di atas, urutan kunjungan adalah D (subtree kiri dari B), B (root), E (subtree kanan dari B), A (root), F (subtree kiri dari C), C (root), dan G (subtree kanan dari C).
