#========================================================
#Nama: Aushaf Ghifary Ariyanto
#NIM: J0403251123
#Kelas: TPL-B1  
#========================================================

# =======================================================
# Tugas Hands-On: Sistem Antrian Bengkel Motor
# =======================================================

class Node:
    def __init__(self, no, nama, servis):
        self.no = no
        self.nama = nama
        self.servis = servis
        self.next = None


class QueueBengkel:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, no, nama, servis):
        # Tambahkan data ke antrian
        new_node = Node(no, nama, servis)
        if self.rear is None:  # Jika antrian kosong
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        print("Pelanggan berhasil ditambahkan ke antrian.")

    def dequeue(self):
        # Layani pelanggan terdepan
        if self.front is None:
            print("Antrian kosong.")
            return

        removed = self.front
        self.front = self.front.next

        if self.front is None:  # Jika setelah dequeue antrian kosong
            self.rear = None

        print(f"Melayani pelanggan: {removed.nama} ({removed.servis})")

    def tampilkan(self):
        # Tampilkan seluruh antrian
        if self.front is None:
            print("Antrian kosong.")
            return

        current = self.front
        print("\nDaftar Antrian:")
        while current:
            print(f"No: {current.no} | Nama: {current.nama} | Servis: {current.servis}")
            current = current.next


def main():
    q = QueueBengkel()
    while True:
        print("\n=== Sistem Antrian Bengkel ===")
        print("1. Tambah Pelanggan")
        print("2. Layani Pelanggan")
        print("3. Lihat Antrian")
        print("4. Keluar")
        pilih = input("Pilih menu: ")

        if pilih == "1":
            no = input("No Antrian : ")
            nama = input("Nama : ")
            servis = input("Servis : ")
            q.enqueue(no, nama, servis)

        elif pilih == "2":
            q.dequeue()

        elif pilih == "3":
            q.tampilkan()

        elif pilih == "4":
            break

        else:
            print("Pilihan tidak valid")


if __name__ == "__main__":
    main()