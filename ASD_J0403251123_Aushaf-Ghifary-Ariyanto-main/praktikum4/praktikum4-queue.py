#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

#========================================================
#Implementasi Dasar : Queue Berbaris Linked List
#========================================================

class Node:
    def __init__(self,data): #Konstruktor
        self.data = data #Menyimpan nilai / data
        self.next = None #Pointer ke note berikutnya

#Queue dengan 2 pointer : front dan rear
class QueueLL:
    def __init__(self):
        self.front = None #Node paling depan
        self.rear = None #Node paling belakang

    def enqueue(self,data):
        #Menambah data di belakang (rear)
        nodeBaru = Node(data)

        #Jika queue kososng, front dan rear menunjk ke node yang sama
        if self.rear is None and self.front is None:
            self.front = nodeBaru
            self.rear = nodeBaru
            return

        #Jika queue tidak kosong:
        #Rear lama menunjuk ke node baru
        self.rear.next = nodeBaru
        #Rear pindah ke node baru
        self.rear = nodeBaru


    def dequeue(self):
        #Menghapus data dari depan

        # 1) data yang paling depan
        data_terhapus = self.front.data

        # 2) Geser front ke node berikutnya
        self.front = self.front.next

        # 3) Jika setelah geser front menjadi none, maka queue kosong
        #Rear juga harus jadi none
        if self.front is None:
            self.rear = None
        
        return data_terhapus


    def tampilkan(self):
        #Menampilkan isi queue dari front ke rear
        current = self.front
        print("Front -> ", end="->")
        while current is not None:
            print(current.data, end="->")
            current = current.next
        print("None - Rear di node terakhir")

#Instantiasi objek class QueueLL
queue = QueueLL()
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
queue.tampilkan()

queue.dequeue()
queue.tampilkan()

