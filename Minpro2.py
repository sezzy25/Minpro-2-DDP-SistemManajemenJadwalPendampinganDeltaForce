import os
import random
import math

akun = {
    "admin": {
        "password": "admin123",
        "role": "admin"
    },
    "user": {
        "password": "user123",
        "role": "user"
    }
}
jadwal = []

def login():
    print("LOGIN")
    username = input("Username: ")
    password = input("Password: ")

    if username in akun and akun[username]["password"] == password:
        print(f"Selamat datang, {username}!")
        return akun[username]["role"]
    else:
        print("Username atau password salah")
        return None

def hitung_jumlah():
    jumlah = 0
    for data in jadwal:
        jumlah = jumlah + 1
    return jumlah

def tampilkan_jadwal():
    print("Lihat Jadwal")
    jumlah = hitung_jumlah()
    if jumlah == 0:
        print("Belum ada jadwal")
    else:
        i = 0
        while i < jumlah:
            print(
                i + 1,
                "Nama:", jadwal[i]["nama"],
                "Kategori:", jadwal[i]["kategori"],
                "Harga:", jadwal[i]["harga"],
                "Durasi:", jadwal[i]["durasi"]
            )
            i = i + 1

def tambah_jadwal():
    print("Tambah jadwal")

    nama = input("Masukkan nama user: ")
    kategori = input("Kategori (Ranked/Unranked/Warfare): ")
    harga = int(input("Harga: "))
    durasi = input("Durasi pendampingan: ")

    if nama == "":
        print("Nama tidak boleh kosong")
    elif kategori == "":
        print("Kategori tidak boleh kosong")
    elif harga <= 0:
        print("Harga harus lebih dari 0")
    elif durasi == "":
        print("Durasi tidak boleh kosong")
    else:
        kode = random.randint(1000, 9999)

    data_baru = {
        "nama": nama,
        "kategori": kategori,
        "harga": harga,
        "durasi": durasi
    }
    jadwal.append(data_baru)
    print("Jadwal berhasil ditambahkan")
    print("Kode jadwal:", kode)

def ubah_jadwal():
    jumlah = hitung_jumlah()
    print("Ubah jadwal")

    if jumlah == 0:
        print("Belum ada jadwal")
    else:
        tampilkan_jadwal()
        nomor = int(input("Pilih nomor jadwal yang ingin diubah: "))
        nomor = nomor - 1

        if nomor < 0 or nomor >= jumlah:
            print("Nomor jadwal tidak valid")
        else:
            nama = input("Masukkan nama user: ")
            kategori = input("Kategori(Ranked/Unranked/Warfare): ")
            harga = int(input("Harga: "))
            durasi = input("Durasi pendampingan: ")

            if nama == "":
                print("Nama tidak boleh kosong")
            elif kategori == "":
                print("Kategori tidak boleh kosong")
            elif harga <= 0:
                print("Harga harus lebih dari 0")
            elif durasi == "":
                print("Durasi tidak boleh kosong")
            else:
                jadwal[nomor]["nama"] = nama
                jadwal[nomor]["kategori"] = kategori
                jadwal[nomor]["harga"] = harga
                jadwal[nomor]["durasi"] = durasi
                print("Jadwal berhasil diubah")

def hapus_jadwal():
    jumlah = hitung_jumlah()
    print("Hapus jadwal")\

    if jumlah == 0:
        print("Belum ada jadwal")
    else:
        tampilkan_jadwal()
        nomor = int(input("Pilih nomor jadwal yang ingin dihapus: "))
        nomor = nomor - 1

        if nomor < 0 or nomor >= jumlah:
            print("Nomor jadwal tidak valid")
        else:
            del jadwal[nomor]
            print("Jadwal berhasil dihapus")

def hitung_total():
    harga = int(input("Harga per jam: "))
    durasi = int(input("Durasi pendampingan: "))

    if harga <= 0:
        print("Harga harus lebih dari 0")
    elif durasi <=0:
        print("Durasi harus lebih dari 0")
    else:
        total = math.ceil(harga * durasi)
        print("Total biaya: RP", total)

def menu_admin():
    while True:
        os.system("cls")
        print("\nMenu Admin:")
        print("1. Tambah jadwal")
        print("2. Lihat jadwal")
        print("3. Ubah jadwal")
        print("4. Hapus jadwal")
        print("5. Hitung total biaya")
        print("6. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tambah_jadwal()
        elif pilih == "2":
            tampilkan_jadwal()
        elif pilih == "3":
            ubah_jadwal()
        elif pilih == "4":
            hapus_jadwal()
        elif pilih == "5":
            hitung_total()
        elif pilih == "6":
            print("Keluar dari menu admin")
            break
        else:
            print("Pilihan tidak valid")

        input("Tekan Enter untuk melanjutkan")

def menu_user():
    while True:
        os.system("cls")
        print("Menu User")
        print("1. Lihat jadwal")
        print("2. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            tampilkan_jadwal()
        elif pilih == "2":
            print("Keluar dari menu user")
            break
        else:
            print("Pilihan tidak valid")

        input("Tekan Enter untuk melanjutkan")

while True:       
    role = login()
    if role == "admin":
        menu_admin()
    elif role == "user":
        menu_user()
    else:
        print("Login gagal")


