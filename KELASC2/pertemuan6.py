# # # # Membuat Set
# # # # kartu = {"merah", "merah", "biru", "hijau"}
# # # # print(kartu)

# # # # set menggunakan list
# # # # matkul = ["apd", "orsikom", "apd", "kalkulus"]
# # # # sks = set(matkul)
# # # # print(sks)

# # # #set menggunakan tuple
# # # # buah = set(("apel", "jeruk", "mangga", "apel"))
# # # # print(buah)

# # # # Mengakses elemen pada Set
# # # # angka_ganjil = {1, 3, 5, 7, 9}
# # # # for angka in angka_ganjil:
# # # # print (angka)

# # # #Menambahkan elemen pada Set
# # # # kelas = {"a", "b", "c"}
# # # # kelas.add("d")
# # # # print(kelas)

# # # # #Menghapus elemen pada Set
# # # # buah = {"apel", "mangga", "jeruk"}
# # # # buah.remove("mangga")
# # # # print(buah)

# # # # Operasi Himpunan pada Set
# # # # aslab1 = {"fina", "shasha", "risma"}
# # # # aslab2 = {"larry", "attar", "haekal"}
# # # # gabung = aslab1.union(aslab2)
# # # # print(gabung)

# # # # Biodata = {
# # # # "Nama" : "Afuza Lee",
# # # # "NIM" : 2609106096,
# # # # "KRS" : ["Struktur Data", "Basis Data"],
# # # # "Mahasiswa_Aktif" : True,
# # # # "Instagram" : "afuza_29"
# # # # }
# # # # print(f"Nama saya adalah {Biodata['Nama']}")
# # # # print(f"Saya mengambil mata kuliah {Biodata['KRS'][0]} dan {Biodata['KRS'][1]}")

# # # game = {
# # # "pou" : "chill",
# # # "genshin impact" : "action",
# # # "valorant" : "fps",
# # # "minecraft" : "sandbox",
# # # "mobile legend" : "moba"
# # # }
# # # # Perulangan untuk menampilkan key
# # # for i in game:
# # #     print(i)
# # # for i in game.keys():
# # #     print(i)

# # # # Perulangan untuk menampilkan value
# # #     for i in game.values():
# # # print(i)

# # # # Perulangan untuk menampilkan key dan value
# # # for i, j in game.items():
# # # print(f"{i} adalah jenis game {j}")

# # # # Menambah item secara langsung
# # # game["resident evil"] = "horror"
# # # print(game)

# # Menambah item menggunakan metode .update()
# # game.update({"resident evil" : "horror"})
# # print(game)

# # Menambah key dan value menggunakan metode setdefault()
# # tambah = game.setdefault("resident evil", "horror")
# # print(game)
# # print("Tipe game", game.setdefault("grow a garden", "gardening"))

# # mengubah Item Dalam Dictionary
# # 1.Menambah item secara langsung
# # print(game)
# # game["genshin impact"] = "adventure"
# # print(game)

# # 2.Mengubah item menggunakan metode .update()
# # print(game)
# # game.update({"genshin impact" : "adventure"})
# # print(game)


# # Menghapus Item Dalam Dictionary
# # 1.Menghapus menggunakan metode del
# aset = {
# "jenis" : "rumah",
# "harga" : 120000000,
# "alamat" : "Jl. Raya No. 1",
# "berpenghuni" : True,
# "luas" : "120m x 80m"
# }

# print(aset)
# del aset["luas"]
# print(aset)
# print(aset.get("luas"))

# 2.Menghapus menggunakan metode pop()
# print(aset)
# cache = aset.pop("luas")
# print(aset)
# print(aset.get("luas"))
# print(cache)

# 3.Menghapus menggunakan metode clear()
# print(aset)
# aset.clear()
# print(aset)