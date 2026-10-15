import os

data_user = [["admin", "admin123", "admin"]]

data_kunci = [
    ["K01", "Pintu Depan", "Rak A", "Tersedia", "-"],
    ["K02", "Gudang", "Rak B", "Tersedia", "-"],
]

while True:
    os.system("cls" if os.name == "nt" else "clear")
    print("SISTEM MANAJEMEN KUNCI CADANGAN")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        username = input("Username: ")
        password = input("Password: ")
        akun = ""
        for u in data_user:
            if u[0] == username and u[1] == password:
                akun = u

        if akun == "":
            print("Username atau password salah")
            input("Tekan enter...")

        elif akun[2] == "admin":
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("MENU ADMIN")
                print("1. Tambah kunci")
                print("2. Lihat daftar kunci")
                print("3. Ubah lokasi atau status")
                print("4. Hapus kunci")
                print("5. Logout")
                menu = input("Pilih: ")

                if menu == "1":
                    kode = input("Kode kunci: ")
                    nama = input("Nama kunci: ")
                    lokasi = input("Lokasi: ")
                    ada = False
                    for k in data_kunci:
                        if k[0] == kode:
                            ada = True
                    if kode == "" or nama == "" or lokasi == "":
                        print("Data tidak boleh kosong")
                    elif ada == True:
                        print("Kode sudah ada")
                    else:
                        data_kunci.append([kode, nama, lokasi, "Tersedia", "-"])
                        print("Data berhasil ditambah")
                    input("Tekan enter...")

                elif menu == "2":
                    if len(data_kunci) == 0:
                        print("Data kunci masih kosong")
                    else:
                        for k in data_kunci:
                            print(k[0], "-", k[1], "-", k[2], "-", k[3], "-", k[4])
                    input("Tekan enter...")

                elif menu == "3":
                    kode = input("Kode kunci yang diubah: ")
                    urutan = -1
                    for i in range(len(data_kunci)):
                        if data_kunci[i][0] == kode:
                            urutan = i
                    if urutan == -1:
                        print("Kode tidak ditemukan")
                    else:
                        print("1. Ubah lokasi")
                        print("2. Ubah status")
                        ubah = input("Pilih: ")
                        if ubah == "1":
                            lokasi_baru = input("Lokasi baru: ")
                            if lokasi_baru == "":
                                print("Lokasi tidak boleh kosong")
                            else:
                                data_kunci[urutan][2] = lokasi_baru
                                print("Lokasi berhasil diubah")
                        elif ubah == "2":
                            print("1. Tersedia")
                            print("2. Dipinjam")
                            st = input("Pilih status: ")
                            if st == "1":
                                data_kunci[urutan][3] = "Tersedia"
                                data_kunci[urutan][4] = "-"
                                print("Status berhasil diubah")
                            elif st == "2":
                                data_kunci[urutan][3] = "Dipinjam"
                                data_kunci[urutan][4] = "admin"
                                print("Status berhasil diubah")
                            else:
                                print("Pilihan tidak ada")
                        else:
                            print("Pilihan tidak ada")
                    input("Tekan enter...")

                elif menu == "4":
                    kode = input("Kode kunci yang dihapus: ")
                    urutan = -1
                    for i in range(len(data_kunci)):
                        if data_kunci[i][0] == kode:
                            urutan = i
                    if urutan == -1:
                        print("Kode tidak ditemukan")
                    else:
                        data_kunci.pop(urutan)
                        print("Data berhasil dihapus")
                    input("Tekan enter...")

                elif menu == "5":
                    break

                else:
                    print("Menu tidak ada")
                    input("Tekan enter...")

        else:
            while True:
                os.system("cls" if os.name == "nt" else "clear")
                print("MENU PENGGUNA")
                print("1. Lihat daftar kunci")
                print("2. Pinjam kunci")
                print("3. Kembalikan kunci")
                print("4. Logout")
                menu = input("Pilih: ")

                if menu == "1":
                    if len(data_kunci) == 0:
                        print("Data kunci masih kosong")
                    else:
                        for k in data_kunci:
                            print(k[0], "-", k[1], "-", k[2], "-", k[3])
                    input("Tekan enter...")

                elif menu == "2":
                    kode = input("Kode kunci: ")
                    urutan = -1
                    for i in range(len(data_kunci)):
                        if data_kunci[i][0] == kode:
                            urutan = i
                    if urutan == -1:
                        print("Kode tidak ditemukan")
                    elif data_kunci[urutan][3] == "Dipinjam":
                        print("Kunci sedang dipinjam")
                    else:
                        data_kunci[urutan][3] = "Dipinjam"
                        data_kunci[urutan][4] = akun[0]
                        print("Kunci berhasil dipinjam")
                    input("Tekan enter...")

                elif menu == "3":
                    kode = input("Kode kunci: ")
                    urutan = -1
                    for i in range(len(data_kunci)):
                        if data_kunci[i][0] == kode:
                            urutan = i
                    if urutan == -1:
                        print("Kode tidak ditemukan")
                    elif data_kunci[urutan][4] != akun[0]:
                        print("Ini bukan kunci yang kamu pinjam")
                    else:
                        data_kunci[urutan][3] = "Tersedia"
                        data_kunci[urutan][4] = "-"
                        print("Kunci berhasil dikembalikan")
                    input("Tekan enter...")

                elif menu == "4":
                    break

                else:
                    print("Menu tidak ada")
                    input("Tekan enter...")

    elif pilih == "2":
        username = input("Username baru: ")
        password = input("Password baru: ")
        sudah_ada = False
        for u in data_user:
            if u[0] == username:
                sudah_ada = True
        if username == "" or password == "":
            print("Username dan password tidak boleh kosong")
        elif sudah_ada == True:
            print("Username sudah dipakai")
        else:
            data_user.append([username, password, "user"])
            print("Register berhasil")
        input("Tekan enter...")

    elif pilih == "3":
        print("Program selesai")
        break

    else:
        print("Pilihan tidak ada")
        input("Tekan enter...")