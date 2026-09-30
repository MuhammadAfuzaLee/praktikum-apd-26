print("=== RENTAL PS LOABAKUNG ===")

nama = input("Nama: ")
nim = input("NIM: ")

if nama == "Afuzalee" and nim == "096":
    print("1. PS3 - 10000")
    print("2. PS4 - 15000")
    print("3. PS5 - 20000")

    pilih = int(input("Pilih konsol: "))

    if pilih == 1:
        konsol = "PS3"
        harga = 10000
    elif pilih == 2:
        konsol = "PS4"
        harga = 15000
    elif pilih == 3:
        konsol = "PS5"
        harga = 20000
    else:
        print("Pilihan tidak ada")

    jam = int(input("Jumlah jam: "))
    total = harga * jam

    if jam >= 5:
        diskon = total * 8 / 100
    elif jam >= 3:
        diskon = total * 5 / 100
    else:
        diskon = 0

    bayar = total - diskon

    print("=== HASIL ===")
    print("Nama:", nama)
    print("NIM:", nim)
    print("Konsol:", konsol)
    print("Jam:", jam)
    print("Total Harga: Rp", int(total))
    print("Diskon: Rp", int(diskon))
    print("Total Bayar: Rp", int(bayar))

else:
    print("Login gagal")