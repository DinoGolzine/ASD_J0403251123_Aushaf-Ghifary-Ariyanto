class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("null")

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next  
            current.next = prev      
            prev = current           
            current = next_node      
        self.head = prev


llist = LinkedList()
elements = input("Masukkan elemen untuk Linked List (pisahkan dengan koma): ")
data_list = [int(x.strip()) for x in elements.split(",")]

for data in data_list:
    llist.append(data)

print("\nLinked List sebelum dibalik:")
llist.display()
llist.reverse()
print("Linked List setelah dibalik:")
llist.display()
