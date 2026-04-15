#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Latihan 5 . Membuat Traversal post-order
#========================================================

class Node:
    def __init__(self, data):
        self.data = data # Menyimpan Nilai Node
        self.left = None # Child Kiri
        self.right = None # Child Kanan
        
#Fungsi postorder: left -> right -> root
def postorder(node):
    if node is not None:
        postorder(node.left) # Kunjungi subtree kiri
        postorder(node.right) # Kunjungi subtree kanan
        print(node.data, end=" ") # Kunjungi root

# Membuat tree
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.left.left = Node("D")
root.left.right = Node("E")
root.right.left = Node("F")
root.right.right = Node("G")

# Menjalankan traversal post-order
print("Post-order traversal:")
postorder(root) 

# Penjelasan post-order traversal mengunjungi subtree kiri terlebih dahulu, kemudian subtree kanan, dan terakhir root.
# Pada contoh di atas, urutan kunjungan adalah D (subtree kiri dari B), E (subtree kanan dari B), B (root), F (subtree kiri dari C), G (subtree kanan dari C), C (root), dan A (root).

