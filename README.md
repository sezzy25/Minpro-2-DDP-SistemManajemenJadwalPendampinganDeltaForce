# Minpro-2-DDP-JasaPendampinganDeltaForce

**Nama**  : **Abdul Azis Zulkarnain**

**NIM**   : **2609116051**

**Kelas** : **B**  

## Deskripsi Tugas

Program ini dibuat untuk mengelola jadwal pendampingan game saya. Ada dua akun, yaitu admin dan user. Admin bisa menambah, melihat, mengubah, menghapus jadwal, dan menghitung biaya. User hanya bisa melihat jadwal. Program ini menggunakan Python dengan list, dictionary, fungsi, percabangan, dan perulangan.
 

<img width="222" height="61" alt="Screenshot 2026-10-06 115830" src="https://github.com/user-attachments/assets/17bc5df9-bdc7-4ca0-879a-66125a66c4c0" />

import os
Mengambil library os, dipake buat menjalankan perintah sistem, di sini dibuat os.system("cls").

import random
Buat menghasilkan angka acak, dipake untuk kode jadwal.

import math
Library matematika, dipake untuk math.ceil().

<img width="397" height="197" alt="Screenshot 2026-10-06 120105" src="https://github.com/user-attachments/assets/6b3ceb83-40b9-4ea7-840e-985db01795b5" />

akun = {}
→ Membuat dictionary yang menyimpan data login.

"admin"
Username pertama.

"password": "admin123"
Password akun admin.

"role": "admin"
Menentukan admin punya akses menu admin.

"user"
Username kedua.

"password": "user123"
Password akun user.

"role": "user"
Menentukan user masuk ke menu user.

<img width="145" height="12" alt="Screenshot 2026-10-06 120604" src="https://github.com/user-attachments/assets/8a7a26c2-8dc5-41e2-8a6a-b9d2de50426a" />

jadwal = []
Buat nyimpan data jadwal.

<img width="605" height="225" alt="Screenshot 2026-10-06 120742" src="https://github.com/user-attachments/assets/37dfd079-1583-4136-b850-1916027a22eb" />

Fungsi login
def login():
Membuat fungsi bernama login.

print("LOGIN")
Menampilkan tulisan LOGIN.

username = input("Username: ")
Meminta username dari pengguna.

password = input("Password: ")
Meminta password.

if username in akun and akun[username]["password"] == password:
Mengecek 2 hal

Username ada di dictionary akun.
Password yang dimasukkan sama dengan password akun.

print(f"Selamat datang, {username}!")
Menampilkan ucapan berdasarkan username.

return akun[username]["role"]
Mengembalikan role, misalnya "admin" atau "user".

else:
Dijalankan kalau login salah.

print("Username atau password salah")
Menampilkan pesan kesalahan.

return None
Mengembalikan nilai kosong karena login gagal.

<img width="347" height="113" alt="Screenshot 2026-10-06 125120" src="https://github.com/user-attachments/assets/69021a1f-e400-4cb8-a686-faaeb33dfcb4" />

Menghitung jumlah jadwal
def hitung_jumlah():
Membuat fungsi untuk menghitung jumlah data dalam jadwal.

jumlah = 0
Nilai awal jumlah adalah 0.

for data in jadwal:
Mengulang setiap data yang ada di jadwal.

jumlah = jumlah + 1
Setiap menemukan satu jadwal, jumlah ditambah 1.

<img width="538" height="316" alt="Screenshot 2026-10-06 130423" src="https://github.com/user-attachments/assets/2c8149dc-d6c7-4777-b020-323faad2616d" />

Menampilkan jadwal
def tampilkan_jadwal():
Membuat fungsi untuk melihat jadwal.

print("Lihat Jadwal")
Menampilkan judul.

jumlah = hitung_jumlah()
Mengambil jumlah jadwal.

if jumlah == 0:
Mengecek apakah belum ada jadwal.

print("Belum ada jadwal")
Kalau kosong, tampilkan pesan.

else:
Kalau ada jadwal.

i = 0
Membuat nomor indeks mulai dari 0.

while i < jumlah:
Mengulang selama i masih lebih kecil dari jumlah jadwal.

print
Menampilkan data jadwal.

i + 1
Supaya nomor yang dilihat user mulai dari 1, bukan 0.

jadwal[i]["nama"]
Mengambil nama dari jadwal ke-i.

i = i + 1
Pindah ke jadwal berikutnya.

<img width="690" height="558" alt="Screenshot 2026-10-06 134334" src="https://github.com/user-attachments/assets/3d71c6a2-27b7-4c1b-838a-09abb482cf4b" />

Tambah jadwal
def tambah_jadwal():
Membuat fungsi untuk menambahkan jadwal.

nama = input("Masukkan nama user: ")
Meminta nama user.

kategori = input("Kategori (Ranked/Unranked/Warfare): ")
Meminta kategori.

harga = int(input("Harga: "))
Meminta harga dan mengubah input menjadi integer.

durasi = input("Durasi pendampingan: ")
Meminta durasi.

if nama == "":
Mengecek apakah nama kosong.

elif kategori == "":
Mengecek kategori kosong.

elif harga <= 0:
Mengecek harga harus lebih dari 0.

elif durasi == "":
Mengecek durasi kosong.

else:
    kode = random.randint(1000, 9999)
Kalau semua data dianggap valid, program membuat kode acak 1000 sampai 9999.

data_baru = {}
Membuat dictionary berisi data jadwal baru.

jadwal.append(data_baru)
Memasukkan data baru ke list jadwal.

print("Jadwal berhasil ditambahkan")
Menampilkan pesan berhasil.

print("Kode jadwal:", kode)
Menampilkan kode jadwal.

<img width="667" height="546" alt="Screenshot 2026-10-06 134552" src="https://github.com/user-attachments/assets/930dbe40-15e3-40fc-acc5-1a13aab07083" />

Ubah jadwal
def ubah_jadwal():
Fungsi untuk mengubah jadwal.

jumlah = hitung_jumlah()
Mengambil jumlah jadwal.

if jumlah == 0:
Kalau tidak ada jadwal, tampilkan pesan.

tampilkan_jadwal()
Menampilkan semua jadwal.

nomor = int(input("Pilih nomor jadwal yang ingin diubah: "))
User memilih nomor jadwal.

nomor = nomor - 1
Mengubah nomor yang dilihat user menjadi indeks list.

if nomor < 0 or nomor >= jumlah:
Mengecek apakah nomor tidak valid.

nama = input(...)

kategori = input(...)

harga = int(input(...))

durasi = input(...)

Meminta data baru.

jadwal[nomor]["nama"] = nama
Mengganti nama jadwal.

jadwal[nomor]["kategori"] = kategori

jadwal[nomor]["harga"] = harga

jadwal[nomor]["durasi"] = durasi

Mengganti data lainnya.















