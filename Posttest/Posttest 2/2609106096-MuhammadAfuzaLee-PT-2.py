merchandise_1 = 45000
merchandise_2 = 50000
merchandise_3 = 60000
merchandise_4 = 75000
merchandise_5 = 90000
merchandise_6 = 120000

harga_merchandise = [
    merchandise_1,
    merchandise_2,
    merchandise_3,
    merchandise_4,
    merchandise_5,
    merchandise_6
]

biaya_bungkus = 7500
total_harga = merchandise_1 + merchandise_2 + merchandise_3 + merchandise_4 + merchandise_5 + merchandise_6

rata_rata = total_harga / len(harga_merchandise)

nim = 96

bolean = nim > rata_rata

kurs_usd = 16500
total_usd = total_harga / kurs_usd

barang_2_sampai_4 = harga_merchandise[-5:-2]

print("Merchandise 1 :", merchandise_1)
print("Merchandise 2 :", merchandise_2)
print("Merchandise 3 :", merchandise_3)
print("Merchandise 4 :", merchandise_4)
print("Merchandise 5 :", merchandise_5)
print("Merchandise 6 :", merchandise_6)
print("Harga Merchandise :", harga_merchandise)
print("Biaya Bungkus Kado :", biaya_bungkus)
print("Total Harga :", total_harga)
print("Rata-rata :", rata_rata)
print("NIM :", nim)
print("Bolean :", bolean)
print("Total dalam USD :", total_usd)
print("Barang 2 sampai 4 :", barang_2_sampai_4)