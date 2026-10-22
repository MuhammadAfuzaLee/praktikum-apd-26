import os

data_user = {
    "admin": {"password": "admin123", "role": "admin"}
}

data_kunci = {
    "K01": {"nama": "Pintu Depan", "lokasi": "Rak A", "status": "Tersedia", "peminjam": "-"},
    "K02": {"nama": "Gudang", "lokasi": "Rak B", "status": "Tersedia", "peminjam": "-"},
}


def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")


def lihat_kunci(admin):
    if len(data_kunci) == 0:
        print("Data kunci masih kosong")
    else:
        for kode in data_kunci:
            if admin == True:
                print(kode, "-", data_kunci[kode]["nama"], "-", data_kunci[kode]["lokasi"], "-", data_kunci[kode]["status"], "-", data_kunci[kode]["peminjam"])
            else:
                print(kode, "-", data_kunci[kode]["nama"], "-", data_kunci[kode]["lokasi"], "-", data_kunci[kode]["status"])
    input("Tekan enter...")


def tambah_kunci():
    kode = input("Kode kunci: ")
    nama = input("Nama kunci: ")
    lokasi = input("Lokasi: ")
    if kode == "" or nama == "" or lokasi == "":
        print("Data tidak boleh kosong")
    elif data_kunci.get(kode) != None:
        print("Kode sudah ada")
    else:
        data_kunci[kode] = {"nama": nama, "lokasi": lokasi, "status": "Tersedia", "peminjam": "-"}
        print("Data berhasil ditambah")
    input("Tekan enter...")


def ubah_kunci():
    kode = input("Kode kunci yang diubah: ")
    if data_kunci.get(kode) == None:
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
                data_kunci[kode]["lokasi"] = lokasi_baru
                print("Lokasi berhasil diubah")
        elif ubah == "2":
            print("1. Tersedia")
            print("2. Dipinjam")
            st = input("Pilih status: ")
            if st == "1":
                data_kunci[kode]["status"] = "Tersedia"
                data_kunci[kode]["peminjam"] = "-"
                print("Status berhasil diubah")
            elif st == "2":
                data_kunci[kode]["status"] = "Dipinjam"
                data_kunci[kode]["peminjam"] = "admin"
                print("Status berhasil diubah")
            else:
                print("Pilihan tidak ada")
        else:
            print("Pilihan tidak ada")
    input("Tekan enter...")


def hapus_kunci():
    kode = input("Kode kunci yang dihapus: ")
    if data_kunci.get(kode) == None:
        print("Kode tidak ditemukan")
    else:
        del data_kunci[kode]
        print("Data berhasil dihapus")
    input("Tekan enter...")


def pinjam_kunci(username):
    kode = input("Kode kunci: ")
    if data_kunci.get(kode) == None:
        print("Kode tidak ditemukan")
    elif data_kunci[kode]["status"] == "Dipinjam":
        print("Kunci sedang dipinjam")
    else:
        data_kunci[kode]["status"] = "Dipinjam"
        data_kunci[kode]["peminjam"] = username
        print("Kunci berhasil dipinjam")
    input("Tekan enter...")


def kembalikan_kunci(username):
    kode = input("Kode kunci: ")
    if data_kunci.get(kode) == None:
        print("Kode tidak ditemukan")
    elif data_kunci[kode]["peminjam"] != username:
        print("Ini bukan kunci yang kamu pinjam")
    else:
        data_kunci[kode]["status"] = "Tersedia"
        data_kunci[kode]["peminjam"] = "-"
        print("Kunci berhasil dikembalikan")
    input("Tekan enter...")


def menu_admin():
    while True:
        bersihkan()
        print("MENU ADMIN")
        print("1. Tambah kunci")
        print("2. Lihat daftar kunci")
        print("3. Ubah lokasi atau status")
        print("4. Hapus kunci")
        print("5. Logout")
        menu = input("Pilih: ")

        if menu == "1":
            tambah_kunci()
        elif menu == "2":
            lihat_kunci(True)
        elif menu == "3":
            ubah_kunci()
        elif menu == "4":
            hapus_kunci()
        elif menu == "5":
            break
        else:
            print("Menu tidak ada")
            input("Tekan enter...")


def menu_pengguna(username):
    while True:
        bersihkan()
        print("MENU PENGGUNA")
        print("1. Lihat daftar kunci")
        print("2. Pinjam kunci")
        print("3. Kembalikan kunci")
        print("4. Logout")
        menu = input("Pilih: ")

        if menu == "1":
            lihat_kunci(False)
        elif menu == "2":
            pinjam_kunci(username)
        elif menu == "3":
            kembalikan_kunci(username)
        elif menu == "4":
            break
        else:
            print("Menu tidak ada")
            input("Tekan enter...")


def login():
    username = input("Username: ")
    password = input("Password: ")
    akun = data_user.get(username)

    if akun == None or akun["password"] != password:
        print("Username atau password salah")
        input("Tekan enter...")
    elif akun["role"] == "admin":
        menu_admin()
    else:
        menu_pengguna(username)


def register():
    username = input("Username baru: ")
    password = input("Password baru: ")
    if username == "" or password == "":
        print("Username dan password tidak boleh kosong")
    elif data_user.get(username) != None:
        print("Username sudah dipakai")
    else:
        data_user[username] = {"password": password, "role": "user"}
        print("Register berhasil")
    input("Tekan enter...")


while True:
    bersihkan()
    print("SISTEM MANAJEMEN KUNCI CADANGAN")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    pilih = input("Pilih: ")

    if pilih == "1":
        login()
    elif pilih == "2":
        register()
    elif pilih == "3":
        print("Program selesai")
        break
    else:
        print("Pilihan tidak ada")
        input("Tekan enter...") 