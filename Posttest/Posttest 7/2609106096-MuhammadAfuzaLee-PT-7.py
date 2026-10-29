import os

data_user = {
    "admin": {"password": "admin123", "role": "admin"}
}

data_kunci = {
    "K01": {"nama": "Pintu Depan", "lokasi": "Rak A", "status": "Tersedia", "peminjam": "-"},
    "K02": {"nama": "Gudang", "lokasi": "Rak B", "status": "Tersedia", "peminjam": "-"},
}

batas_login = 3
login_gagal = 0


# ===== Prosedur =====
def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")


def tunggu():
    input("Tekan enter...")


# ===== Fungsi tanpa parameter =====
def input_kode():
    kode = input("Kode kunci: ")
    if kode == "":
        raise ValueError("Kode tidak boleh kosong")
    return kode


def jumlah_dipinjam():
    daftar = list(data_kunci)
    return hitung_dipinjam(daftar, 0)


# ===== Fungsi dengan parameter =====
def cek_login(username, password):
    if username not in data_user or data_user[username]["password"] != password:
        raise ValueError("Username atau password salah")
    return data_user[username]["role"]


# Fungsi rekursif
def hitung_dipinjam(daftar, i):
    if i == len(daftar):
        return 0
    if data_kunci[daftar[i]]["status"] == "Dipinjam":
        return 1 + hitung_dipinjam(daftar, i + 1)
    return hitung_dipinjam(daftar, i + 1)


# ===== Prosedur fitur =====
def lihat_kunci(admin):
    if len(data_kunci) == 0:
        print("Data kunci masih kosong")
    else:
        for kode in data_kunci:
            if admin == True:
                print(kode, "-", data_kunci[kode]["nama"], "-", data_kunci[kode]["lokasi"], "-", data_kunci[kode]["status"], "-", data_kunci[kode]["peminjam"])
            else:
                print(kode, "-", data_kunci[kode]["nama"], "-", data_kunci[kode]["lokasi"], "-", data_kunci[kode]["status"])
        print("Jumlah kunci dipinjam:", jumlah_dipinjam())
    tunggu()


def tambah_kunci():
    try:
        kode = input_kode()
        nama = input("Nama kunci: ")
        lokasi = input("Lokasi: ")
        if nama == "" or lokasi == "":
            raise ValueError("Data tidak boleh kosong")
        if kode in data_kunci:
            raise ValueError("Kode sudah ada")
    except ValueError as e:
        print(e)
    else:
        data_kunci[kode] = {"nama": nama, "lokasi": lokasi, "status": "Tersedia", "peminjam": "-"}
        print("Data berhasil ditambah")
    finally:
        tunggu()


def ubah_kunci():
    try:
        kode = input_kode()
        kunci = data_kunci[kode]
        print("1. Ubah lokasi")
        print("2. Ubah status")
        ubah = input("Pilih: ")
        if ubah == "1":
            lokasi_baru = input("Lokasi baru: ")
            if lokasi_baru == "":
                raise ValueError("Lokasi tidak boleh kosong")
            kunci["lokasi"] = lokasi_baru
            print("Lokasi berhasil diubah")
        elif ubah == "2":
            print("1. Tersedia")
            print("2. Dipinjam")
            st = input("Pilih status: ")
            if st == "1":
                kunci["status"] = "Tersedia"
                kunci["peminjam"] = "-"
                print("Status berhasil diubah")
            elif st == "2":
                kunci["status"] = "Dipinjam"
                kunci["peminjam"] = "admin"
                print("Status berhasil diubah")
            else:
                raise ValueError("Pilihan tidak ada")
        else:
            raise ValueError("Pilihan tidak ada")
    except KeyError:
        print("Kode tidak ditemukan")
    except ValueError as e:
        print(e)
    finally:
        tunggu()


def hapus_kunci():
    try:
        kode = input_kode()
        del data_kunci[kode]
    except KeyError:
        print("Kode tidak ditemukan")
    except ValueError as e:
        print(e)
    else:
        print("Data berhasil dihapus")
    finally:
        tunggu()


def pinjam_kunci(username):
    try:
        kode = input_kode()
        kunci = data_kunci[kode]
        if kunci["status"] == "Dipinjam":
            raise ValueError("Kunci sedang dipinjam")
    except KeyError:
        print("Kode tidak ditemukan")
    except ValueError as e:
        print(e)
    else:
        kunci["status"] = "Dipinjam"
        kunci["peminjam"] = username
        print("Kunci berhasil dipinjam")
    finally:
        tunggu()


def kembalikan_kunci(username):
    try:
        kode = input_kode()
        kunci = data_kunci[kode]
        if kunci["peminjam"] != username:
            raise ValueError("Ini bukan kunci yang kamu pinjam")
    except KeyError:
        print("Kode tidak ditemukan")
    except ValueError as e:
        print(e)
    else:
        kunci["status"] = "Tersedia"
        kunci["peminjam"] = "-"
        print("Kunci berhasil dikembalikan")
    finally:
        tunggu()


def menu_admin():
    while True:
        bersihkan()
        print("MENU ADMIN")
        print("1. Tambah kunci")
        print("2. Lihat daftar kunci")
        print("3. Ubah lokasi atau status")
        print("4. Hapus kunci")
        print("5. Logout")
        try:
            menu = int(input("Pilih: "))
        except ValueError:
            print("Input harus berupa angka")
            tunggu()
        else:
            if menu == 1:
                tambah_kunci()
            elif menu == 2:
                lihat_kunci(True)
            elif menu == 3:
                ubah_kunci()
            elif menu == 4:
                hapus_kunci()
            elif menu == 5:
                break
            else:
                print("Menu tidak ada")
                tunggu()


def menu_pengguna(username):
    while True:
        bersihkan()
        print("MENU PENGGUNA")
        print("1. Lihat daftar kunci")
        print("2. Pinjam kunci")
        print("3. Kembalikan kunci")
        print("4. Logout")
        try:
            menu = int(input("Pilih: "))
        except ValueError:
            print("Input harus berupa angka")
            tunggu()
        else:
            if menu == 1:
                lihat_kunci(False)
            elif menu == 2:
                pinjam_kunci(username)
            elif menu == 3:
                kembalikan_kunci(username)
            elif menu == 4:
                break
            else:
                print("Menu tidak ada")
                tunggu()


def login():
    global login_gagal
    username = input("Username: ")
    password = input("Password: ")
    try:
        role = cek_login(username, password)
    except ValueError as e:
        login_gagal += 1
        print(e)
        print("Gagal login", login_gagal, "dari", batas_login)
        tunggu()
    else:
        login_gagal = 0
        if role == "admin":
            menu_admin()
        else:
            menu_pengguna(username)


def register():
    username = input("Username baru: ")
    password = input("Password baru: ")
    try:
        if username == "" or password == "":
            raise ValueError("Username dan password tidak boleh kosong")
        if username in data_user:
            raise ValueError("Username sudah dipakai")
    except ValueError as e:
        print(e)
    else:
        data_user[username] = {"password": password, "role": "user"}
        print("Register berhasil")
    finally:
        tunggu()


# ===== Program utama =====
while True:
    if login_gagal >= batas_login:
        print("Terlalu banyak gagal login, program dihentikan")
        break

    bersihkan()
    print("SISTEM MANAJEMEN KUNCI CADANGAN")
    print("1. Login")
    print("2. Register")
    print("3. Keluar")
    try:
        pilih = int(input("Pilih: "))
    except ValueError:
        print("Input harus berupa angka")
        tunggu()
    else:
        if pilih == 1:
            login()
        elif pilih == 2:
            register()
        elif pilih == 3:
            print("Program selesai")
            break
        else:
            print("Pilihan tidak ada")
            tunggu()