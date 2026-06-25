import csv
import os

CSV_FILE = "buku.csv"

# =========================
# NODE BUKU (LINKED LIST)
# =========================
class BookNode:
    def __init__(self, book_id, judul, pengarang, stok):
        self.book_id = str(book_id)
        self.judul = judul
        self.pengarang = pengarang
        self.stok = int(stok)
        self.next = None


# =========================
# LINKED LIST BUKU
# =========================
class LinkedList:
    def __init__(self):
        self.head = None

    def tambah_buku(self, book_id, judul, pengarang, stok):
        if self.cari_buku(book_id):
            print("ID sudah digunakan!")
            return False

        node = BookNode(book_id, judul, pengarang, stok)

        if self.head is None:
            self.head = node
            return True

        current = self.head
        while current.next:
            current = current.next

        current.next = node
        return True

    def tampilkan_buku(self):
        if self.head is None:
            print("Data buku kosong.")
            return

        current = self.head

        print("\n===== DAFTAR BUKU =====")

        while current:
            print(
                f"{current.book_id} | "
                f"{current.judul} | "
                f"{current.pengarang} | "
                f"Stok: {current.stok}"
            )
            current = current.next

    def cari_buku(self, keyword):
        current = self.head

        while current:
            if (
                current.book_id == str(keyword)
                or current.judul.lower() == str(keyword).lower()
            ):
                return current

            current = current.next

        return None

    def hapus_buku(self, book_id):
        current = self.head
        prev = None

        while current:
            if current.book_id == str(book_id):

                if prev is None:
                    self.head = current.next
                else:
                    prev.next = current.next

                return True

            prev = current
            current = current.next

        return False

    def edit_buku(self, book_id, judul, pengarang, stok):
        buku = self.cari_buku(book_id)

        if buku:
            buku.judul = judul
            buku.pengarang = pengarang
            buku.stok = int(stok)
            return True

        return False

    def ke_list(self):
        data = []
        current = self.head

        while current:
            data.append([
                current.book_id,
                current.judul,
                current.pengarang,
                current.stok
            ])
            current = current.next

        return data

# =========================
# NODE ANTRIAN (QUEUE)
# =========================
class QueueNode:
    def __init__ (self, nama, judul):
        self.nama = nama
        self.judul = judul
        self.next = None


# =========================
# QUEUE
# =========================
class Queue:
    def __init__ (self):
        self.front = None
        self.rear = None

    def enqueue(self, nama, judul):
        node = QueueNode(nama, judul)

        if self.rear is None:
            self.front = node
            self.rear = node
            return

        self.rear.next = node
        self.rear = node

    def dequeue(self):
        if self.front is None:
            return None

        data = (self.front.nama, self.front.judul)

        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return data

    def tampilkan(self):
        if self.front is None:
            print("Antrian kosong.")
            return

        current = self.front
        nomor = 1

        print("\n===== ANTRIAN PEMINJAMAN =====")

        while current:
            print(f"{nomor}. {current.nama} - {current.judul}")
            current = current.next
            nomor += 1


# =========================
# CSV
# =========================
def buat_csv_awal():
    if os.path.exists(CSV_FILE):
        return

    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "judul", "pengarang", "stok"])

        writer.writerow(["1", "Antologi Rasa", "Ika Natassa", "5"])
        writer.writerow(["2", "Dilan: Dia adalah Dilanku Tahun 1990", "Pidi Baiq", "7"])
        writer.writerow(["3", "Kambing Jantan", "Raditya Dika", "4"])
        writer.writerow(["4", "Bajaj Bajuri", "Aris Nugraha", "3"])
        writer.writerow(["5", "Danur", "Risa Saraswati", "6"])
        writer.writerow(["6", "Sewu Dino", "SimpleMan", "5"])
        writer.writerow(["7", "Laskar Pelangi", "Andrea Hirata", "8"])
        writer.writerow(["8", "Totto-chan: Gadis Cilik di Jendela", "Tetsuko Kuroyanagi", "4"])


def load_csv(perpustakaan):
    with open(CSV_FILE, "r", encoding="utf-8") as file:
        reader = csv.reader(file)

        next(reader)

        for row in reader:
            perpustakaan.tambah_buku(
                row[0],
                row[1],
                row[2],
                row[3]
            )


def simpan_csv(perpustakaan):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        writer.writerow(["id", "judul", "pengarang", "stok"])

        for data in perpustakaan.ke_list():
            writer.writerow(data)


# =========================
# BUBBLE SORT
# =========================
def sort_judul(perpustakaan):
    data = perpustakaan.ke_list()

    n = len(data)

    for i in range(n):
        for j in range(n - i - 1):

            if data[j][1].lower() > data[j + 1][1].lower():
                data[j], data[j + 1] = data[j + 1], data[j]

    return data


def tampil_sort(data):
    print("\n===== HASIL SORTING =====")

    for item in data:
        print(
            f"{item[0]} | "
            f"{item[1]} | "
            f"{item[2]} | "
            f"Stok: {item[3]}"
        )

# =========================
# MENU UTAMA
# =========================
def main():
    buat_csv_awal()

    perpustakaan = LinkedList()
    antrian = Queue()

    load_csv(perpustakaan)

    while True:

        print("\n===== SISTEM MANAJEMEN PERPUSTAKAAN =====")
        print("1. Tambah Buku")
        print("2. Lihat Buku")
        print("3. Cari Buku")
        print("4. Urutkan Buku")
        print("5. Edit Buku")
        print("6. Hapus Buku")
        print("7. Tambah Antrian Peminjaman")
        print("8. Layani Antrian")
        print("9. Lihat Antrian")
        print("0. Keluar")

        pilihan = input("Pilih menu: ")

        # CREATE
        if pilihan == "1":

            book_id = input("ID Buku      : ")
            judul = input("Judul        : ")
            pengarang = input("Pengarang    : ")

            try:
                stok = int(input("Stok         : "))

                if stok < 0:
                    print("Stok tidak boleh negatif.")
                    continue

            except:
                print("Stok harus berupa angka.")
                continue

            if perpustakaan.tambah_buku(
                book_id,
                judul,
                pengarang,
                stok
            ):
                simpan_csv(perpustakaan)
                print("Buku berhasil ditambahkan.")

        # READ
        elif pilihan == "2":
            perpustakaan.tampilkan_buku()

        # SEARCH
        elif pilihan == "3":

            keyword = input("Masukkan ID atau Judul: ")

            buku = perpustakaan.cari_buku(keyword)

            if buku:
                print("\nData ditemukan")
                print("ID        :", buku.book_id)
                print("Judul     :", buku.judul)
                print("Pengarang :", buku.pengarang)
                print("Stok      :", buku.stok)
            else:
                print("Data tidak ditemukan.")

        # SORT
        elif pilihan == "4":

            hasil = sort_judul(perpustakaan)
            tampil_sort(hasil)

        # UPDATE
        elif pilihan == "5":

            book_id = input("Masukkan ID Buku: ")

            buku = perpustakaan.cari_buku(book_id)

            if buku is None:
                print("Buku tidak ditemukan.")
                continue

            judul = input("Judul Baru      : ")
            pengarang = input("Pengarang Baru  : ")

            try:
                stok = int(input("Stok Baru       : "))

                if stok < 0:
                    print("Stok tidak boleh negatif.")
                    continue

            except:
                print("Stok harus angka.")
                continue

            perpustakaan.edit_buku(
                book_id,
                judul,
                pengarang,
                stok
            )

            simpan_csv(perpustakaan)

            print("Data berhasil diubah.")

        # DELETE
        elif pilihan == "6":

            book_id = input("Masukkan ID Buku: ")

            if perpustakaan.hapus_buku(book_id):
                simpan_csv(perpustakaan)
                print("Buku berhasil dihapus.")
            else:
                print("Buku tidak ditemukan.")

        # ENQUEUE
        elif pilihan == "7":

            nama = input("Nama Peminjam : ")
            judul = input("Judul Buku    : ")

            buku = perpustakaan.cari_buku(judul)

            if buku is None:
                print("Buku tidak ditemukan.")
                continue

            if buku.stok <= 0:
                print("Stok buku habis.")
                continue

            antrian.enqueue(nama, judul)

            print("Masuk ke antrian peminjaman.")

        # DEQUEUE
        elif pilihan == "8":

            data = antrian.dequeue()

            if data is None:
                print("Antrian kosong.")
                continue

            nama = data[0]
            judul = data[1]

            buku = perpustakaan.cari_buku(judul)

            if buku:
                buku.stok -= 1
                simpan_csv(perpustakaan)

            print(
                f"{nama} berhasil meminjam "
                f"buku '{judul}'"
            )

        # LIHAT ANTRIAN
        elif pilihan == "9":
            antrian.tampilkan()

        # KELUAR
        elif pilihan == "0":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak tersedia.")


# =========================
# PROGRAM UTAMA
# =========================
if __name__ == "__main__":
    main()