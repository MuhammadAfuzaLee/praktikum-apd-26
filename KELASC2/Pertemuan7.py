# # def nama_fungsi():
# # pernyataan
# # return hasil yang diinginkan

# # Fungsi Tanpa Parameter
# # def luas_persegi_panjang():
# #     luas = 3 * 5
# #     return luas
# # #Kita panggil fungsinya
# # print("Luas persegi panjang:", luas_persegi_panjang())

# # # Fungsi dengan Parameter
# # def luas_persegi(sisi):
# #     luas = sisi * sisi
# #     return luas
# # #Kita panggil fungsinya lalu argumen kita adalah angka 7
# # print("Luas persegi:", luas_persegi(7))

# #Prosedur
# #Tanpa parameter
# # def pengumuman(matkul):
# # #     print(f"Hari ini Pengujian Proyek Akhir {matkul}")
# # # #Pemanggilan Prosedur
# # # pengumuman("apd")

# # nama = "Larry"
# # prodi = "Informatika"
# # #Membuat variabel lokal
# # def data():
# #     nama = "Teknik Kedokteran"
# #     prodi = "Kedokteran Lanjut"
# #     print("Nama:", nama)
# #     print("Prodi:", prodi)

# # data()
# # #Mengakses variabel global
# # print("Nama:", nama)
# # print("Prodi:", prodi)

# # def hitung_mundur (n) :
# #     if n == 0:
# #         print("MATI")
# #     else:
# #         print(n)
# #         hitung_mundur(n-500)

# # hitung_mundur(5000)

# buku = []

# def lihat_buku():
#     if len(buku) == 0:
#         print("Belum ada data buku")
#     else:
#         print("ID Buku | Judul Buku")
#         for indeks in range(len(buku)):
#             print(indeks, "|", buku[indeks])

# def tambah_buku():
#     buku_baru = input("Judul Buku: ")
#     buku.append(buku_baru)
#     print("Buku berhasil ditambahkan!")

# def edit_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku_baru = input("Judul baru: ")
#         buku[indeks] = buku_baru
#         print("Buku berhasil diupdate!")

# def hapus_buku():
#     lihat_buku()
#     indeks = int(input("Masukkan ID Buku: "))
#     if indeks == len(buku) or indeks < 0:
#         print("ID tidak valid")
#     else:
#         buku.remove(buku[indeks])
#         print("Buku berhasil dihapus!")

# def tampilkan_menu():
#     print("\n")
#     print("========= MENU =========")
#     print("[1] Lihat Data Buku")
#     print("[2] Tambahkan Data Buku")
#     print("[3] Edit Data Buku")
#     print("[4] Hapus Data Buku")
#     print("[5] Keluar")

#     menu = input("PILIH MENU> ")
#     print("\n")

#     if menu == "1":
#         lihat_buku()
#     elif menu == "2":
#         tambah_buku()
#     elif menu == "3":
#         edit_buku()
#     elif menu == "4":
#         hapus_buku()
#     elif menu == "5":
#         exit()
#     else:
#         print("Pilihan tidak valid!")

# while (True):
#     tampilkan_menu()

# umur = int(input('Masukkan Angka : '))
# print(umur) #input 'cinta APD'

# try:
#     umur = int(input("Masukkan Umur Anda : "))
#     if umur < 7:
#         raise ValueError("Anda Masih TK")
#     if umur < 17:
#         raise ValueError("Anda Masih di Bawah Umur")
# except ValueError as e:
#     print(e)
# else:
#     print(f"Umur Kamu Adalah {Umur}")
# finally:
#     print("Program Selesai")