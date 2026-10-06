username = "Afuzalee"
password = "096"

print("=== REKAP PENGELUARAN BULAN INI ===")

berhasil = False
for i in range(3):
    user = input("Username : ")
    pw = input("Password : ")

    if user == username and pw == password:
        print("Login Berhasil")
        berhasil = True
        break
    else:
        print("Login Anda Gagal. Sisa percobaan:", 2 - i)

if berhasil == False:
    print("Percobaan habis, Program berhenti")
else:
    uang_bulanan = 0
    total_pengeluaran = 0

    while uang_bulanan <= 0:
        uang_bulanan = int(input("Masukkan uang saku awal : Rp"))

    while uang_bulanan > 0:
        print("")
        print("=== MENU UTAMA ===")
        print("[1] Catat Pengeluaran")
        print("[2] Cek Sisa Uang Saku")
        print("[3] Keluar")
        pilihan = input("Pilih menu (1-3) : ")

        if pilihan == "1":
            lagi = "Ya"
            while lagi == "Ya" :
                nominal = int(input("Nominal pengeluaran : Rp"))

                if nominal <= 0:
                    print("Nominal harus lebih dari 0")
                elif nominal > uang_bulanan:
                    print("Uang saku tidak cukup! Sisa Rp", uang_bulanan)
                else:
                    uang_bulanan = uang_bulanan - nominal
                    total_pengeluaran = total_pengeluaran + nominal
                    print("Sisa uang saku : Rp", uang_bulanan)

                    if uang_bulanan == 0:
                        break

                lagi = input("Apakah Anda ingin mencatat pengeluaran lagi? (YA/Tidak) : ")

        elif pilihan == "2":
            print("Sisa uang saku    : Rp", uang_bulanan)
            print("Total pengeluaran : Rp", total_pengeluaran)
        elif pilihan == "3":
            print("Thank You")
            break
        else:
            print("Pilihan tidak ada")

    if uang_bulanan == 0:
        print("Uang saku mu sudah habis")
        print("Total pengeluaran : Rp", total_pengeluaran)