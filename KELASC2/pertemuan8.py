# # # huruf = list("Python")

# # # print(huruf)

# # # hasil = pow(3, 2, 2)

# # # print(hasil)

# # # buah = ["Apel", "Jeruk", "Mangga"]

# # # hasil = enumerate(buah)

# # # print(list(hasil))

# # buah = ["Apel", "Jeruk", "Mangga", "Anggur", "Melon"]

# # bagian = slice(1, 5, 2)
# # # 1, 5, 2
# # # start, stop, step

# # print(buah[bagian])
# # # Output: ['Jeruk', 'Mangga', 'Anggur']

# # kelas = "b"
# # def tampilkan():
# #     nama = "Dinda"
# #     umur = 19

# #     print(locals())

# # tampilkan()

# # # Output:
# # # {'nama': 'Dinda', 'umur': 19}

# # teks = "Saya belajar Java"
# # hasil = teks.replace("Java", "Python")

# # print(hasil)
# # # Output: Saya belajar Python

# # teks = "apel apel apel"
# # print(teks.replace("apel", "jeruk", 2))

# # Output: jeruk jeruk apel

# from prettytable import PrettyTable
# # Membuat objek tabel dan menentukan nama-nama kolom
# tabel = PrettyTable()
# tabel.field_names = ["NIM", "Nama Mahasiswa", "Prodi"]
# # Menambahkan satu baris data ke dalam tabel
# tabel.add_row(["2609106096", "pujale", "Informatika"])
# # Menambahkan beberapa baris data sekaligus menggunakan list di dalam list
# tabel.add_rows([
#     ["2609106096", "pujaa", "Informatika"],
#     ["2609116088", "geminifer", "Sistem Informasi"]
# ])

# tabel.align["Nama Mahasiswa"] = "l"
# print(tabel)

