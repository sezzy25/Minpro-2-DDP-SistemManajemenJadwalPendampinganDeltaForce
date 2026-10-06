# Minpro-2-DDP-JasaPendampinganDeltaForce

**Nama**  : **Abdul Azis Zulkarnain**

**NIM**   : **2609116051**

**Kelas** : **B**  

## Deskripsi Tugas

Program ini dibuat untuk mengelola jadwal pendampingan game saya. Ada dua akun, yaitu admin dan user. Admin bisa menambah, melihat, mengubah, menghapus jadwal, dan menghitung biaya. User hanya bisa melihat jadwal. Program ini menggunakan Python dengan list, dictionary, fungsi, percabangan, dan perulangan.
 

## 1. Library
<img width="222" height="61" alt="Screenshot 2026-10-06 115830" src="https://github.com/user-attachments/assets/17bc5df9-bdc7-4ca0-879a-66125a66c4c0" />

import os
Mengambil library os, dipake buat menjalankan perintah sistem, di sini dibuat os.system("cls").

import random
Buat menghasilkan angka acak, dipake untuk kode jadwal.

import math
Library matematika, dipake untuk math.ceil().

## 2. Daftar Akun
<img width="397" height="197" alt="Screenshot 2026-10-06 120105" src="https://github.com/user-attachments/assets/6b3ceb83-40b9-4ea7-840e-985db01795b5" />

akun = {}
Membuat dictionary yang menyimpan data login, lalu ada akun dan juga role admin dan user beserta passwordnya

## 3. Jadwal
<img width="145" height="12" alt="Screenshot 2026-10-06 120604" src="https://github.com/user-attachments/assets/8a7a26c2-8dc5-41e2-8a6a-b9d2de50426a" />

jadwal = []
Buat nyimpan data jadwal.

## 4. Fungsi Login

<img width="605" height="225" alt="Screenshot 2026-10-06 120742" src="https://github.com/user-attachments/assets/37dfd079-1583-4136-b850-1916027a22eb" />

def login():
Membuat fungsi bernama login, print untuk nampilkan "Login", lalu input meminta username dan pw akun, ada for in dst yang berfungsi mengecek username di dictionary dan password yang dimasukkan itu sama dan else kalo login salah

## 5. Hitung Jumlah
<img width="347" height="113" alt="Screenshot 2026-10-06 125120" src="https://github.com/user-attachments/assets/69021a1f-e400-4cb8-a686-faaeb33dfcb4" />

def hitung_jumlah():
Membuat fungsi untuk menghitung jumlah data dalam jadwal, jumlah = 0 nilai awal jumlah adalah 0, for data in jadwal: mengulang setiap data yang ada di jadwal,
jumlah = jumlah + 1 setiap menemukan satu jadwal, jumlah ditambah 1.

## 6. Menampilkan Jadwal

<img width="538" height="316" alt="Screenshot 2026-10-06 130423" src="https://github.com/user-attachments/assets/2c8149dc-d6c7-4777-b020-323faad2616d" />

def tampilkan_jadwal():
Membuat fungsi untuk melihat jadwal, print("Lihat Jadwal") menampilkan judul, jumlah = hitung_jumlah() mengambil jumlah jadwal, if jumlah == 0: mengecek apakah belum ada jadwal, print("Belum ada jadwal") kalau kosong, tampilkan pesan, else: kalau ada jadwal, i = 0 membuat nomor indeks mulai dari 0, while i < jumlah: mengulang selama i masih lebih kecil dari jumlah jadwal, print menampilkan data jadwal, i + 1 supaya nomor yang dilihat user mulai dari 1, bukan 0, jadwal[i]["nama"] mengambil nama dari jadwal ke-i, i = i + 1 pindah ke jadwal berikutnya

## 7. Tambah Jadwal

<img width="690" height="558" alt="Screenshot 2026-10-06 134334" src="https://github.com/user-attachments/assets/3d71c6a2-27b7-4c1b-838a-09abb482cf4b" />

def tambah_jadwal():membuat fungsi untuk menambahkan jadwal, nama = input("Masukkan nama user: ") meminta nama user, kategori = input("Kategori (Ranked/Unranked/Warfare): ") meminta kategori, harga = int(input("Harga: ")) meminta harga dan mengubah input menjadi integer, durasi = input("Durasi pendampingan: ") meminta durasi, if nama == "":mengecek apakah nama kosong, elif kategori == "": mengecek kategori kosong, elif harga <= 0: mengecek harga harus lebih dari 0, elif durasi == "": mengecek durasi kosong, else: kode = random.randint(1000, 9999) kalau semua data dianggap valid, program membuat kode acak 1000 sampai 9999, data_baru = {} membuat dictionary berisi data jadwal baru, jadwal.append(data_baru) memasukkan data baru ke list jadwal, print("Jadwal berhasil ditambahkan") menampilkan pesan berhasil, print("Kode jadwal:", kode) menampilkan kode jadwal.

## 8. Ubah Jadwal

<img width="667" height="546" alt="Screenshot 2026-10-06 134552" src="https://github.com/user-attachments/assets/930dbe40-15e3-40fc-acc5-1a13aab07083" />

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

## 9. Hapus Jadwal

<img width="586" height="272" alt="Screenshot 2026-10-06 142952" src="https://github.com/user-attachments/assets/73f8e410-16fa-4d20-90c5-92c34b87cb9a" />

def hapus_jadwal():
Fungsi untuk menghapus jadwal.

jumlah = hitung_jumlah()
Menghitung jumlah jadwal.

tampilkan_jadwal()
Menampilkan jadwal agar user bisa memilih.

nomor = int(input(...))
nomor = nomor - 1
Mengambil nomor pilihan dan mengubahnya menjadi indeks.

if nomor < 0 or nomor >= jumlah:
Mengecek nomor valid atau tidak.

del jadwal[nomor]
Menghapus jadwal dari list.

## 10. Hitung Total

<img width="500" height="198" alt="Screenshot 2026-10-06 152228" src="https://github.com/user-attachments/assets/584dd002-5822-46bc-a1c0-4f6ffc1459ac" />

Hitung total biaya
def hitung_total():
Fungsi menghitung biaya.

harga = int(input("Harga per jam: "))
Input harga per jam.

durasi = int(input("Durasi pendampingan: "))
Input durasi.

if harga <= 0:
Mengecek harga.

elif durasi <= 0:
Mengecek durasi.

total = math.ceil(harga * durasi)
Menghitung harga × durasi.

## 11. Menu Admin

<img width="473" height="502" alt="Screenshot 2026-10-06 153036" src="https://github.com/user-attachments/assets/f3c58393-aa2e-47fe-bfdc-4362abb2bc3a" />

Menu admin
def menu_admin():
Membuat fungsi menu khusus admin.

while True:
Menu terus berulang sampai user memilih keluar.

os.system("cls")
Membersihkan layar Windows.

print("1. Tambah jadwal") sampai print("6. Keluar")
Menampilkan pilihan menu.

pilih = input("Pilih menu: ")
Mengambil pilihan admin.

if pilih == "1":
    tambah_jadwal()
Kalau pilih 1, jalankan tambah jadwal.

elif pilih == "2":
    tampilkan_jadwal()
Kalau pilih 2, tampilkan jadwal.

elif pilih == "3":
    ubah_jadwal()
Kalau pilih 3, ubah jadwal.

elif pilih == "4":
    hapus_jadwal()
Kalau pilih 4, hapus jadwal.

elif pilih == "5":
    hitung_total()
Kalau pilih 5, hitung biaya.

elif pilih == "6":
    break
Keluar dari perulangan menu admin.

else:
    print("Pilihan tidak valid")
Kalau input bukan 1 sampai 6.

## 12. Menu User

<img width="487" height="306" alt="Screenshot 2026-10-06 160113" src="https://github.com/user-attachments/assets/166d922d-688c-49f8-891a-8c428f04ceba" />

Menu user
def menu_user():
Membuat menu khusus user.

while True:
Menu terus berjalan.

User cuma punya:
1. Lihat jadwal
2. Keluar
if pilih == "1":
    tampilkan_jadwal()
User bisa melihat jadwal

elif pilih == "2":
    break
User keluar dari menu

## 13. Program 

<img width="351" height="156" alt="Screenshot 2026-10-06 160329" src="https://github.com/user-attachments/assets/d40b85a6-47b7-4654-8a77-5b648bf522f2" />

while True:
Program login terus berulang.

role = login()
Menjalankan login dan menyimpan hasilnya ke role.

if role == "admin":
    menu_admin()
Kalau role admin, masuk menu admin.

elif role == "user":
    menu_user()
Kalau role user, masuk menu user.

else:
    print("Login gagal")
Kalau login gagal, tampilkan pesan dan kembali ke login.

## ADMIN
## 14. Output Tambah Jadwal 

<img width="332" height="262" alt="Screenshot 2026-10-06 160801" src="https://github.com/user-attachments/assets/b274c15c-5074-4062-ab33-66d5600f09be" />

## 15. Output Lihat Jadwal

<img width="413" height="180" alt="Screenshot 2026-10-06 160820" src="https://github.com/user-attachments/assets/2ec7eabc-c1a0-4cd1-a802-ec5740cf9a72" />

## 16. Output Ubah Jadwal

<img width="427" height="287" alt="Screenshot 2026-10-06 160916" src="https://github.com/user-attachments/assets/3063f53a-5a46-49e8-a85e-a7864bfea39f" />

<img width="451" height="182" alt="Screenshot 2026-10-06 160936" src="https://github.com/user-attachments/assets/870810e6-ca35-433a-8218-7c1f72ad3106" />

## 17. Output Hapus Jadwal

<img width="431" height="217" alt="Screenshot 2026-10-06 161033" src="https://github.com/user-attachments/assets/5c9e39f2-dedb-430b-b6bb-69d935a9e7f0" />

<img width="296" height="177" alt="Screenshot 2026-10-06 161042" src="https://github.com/user-attachments/assets/3ddbd45c-ed1f-41a3-88e9-55ab63025391" />

## 18. Output Hitung Total Biaya

<img width="312" height="195" alt="Screenshot 2026-10-06 161108" src="https://github.com/user-attachments/assets/036b7cc8-b4ed-4a10-91fc-c5f89f26673a" />

## USER
## 19. Output Lihat Jadwal

<img width="383" height="120" alt="Screenshot 2026-10-06 161210" src="https://github.com/user-attachments/assets/3908934e-7d2c-464f-ab1b-bf86956a5d12" />




























