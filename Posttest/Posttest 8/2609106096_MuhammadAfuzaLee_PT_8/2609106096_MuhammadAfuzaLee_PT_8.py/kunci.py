from prettytable import PrettyTable
from data import data_kunci
from utils import tunggu, input_kode, waktu_sekarang, jumlah_dipinjam


def lihat_kunci(admin):
    if len(data_kunci) == 0:
        print("Data kunci masih kosong")
    else:
        tabel = PrettyTable()
        tabel.title = "DAFTAR KUNCI CADANGAN"
        if admin:
            tabel.field_names = ["No", "Kode", "Nama", "Lokasi", "Status", "Peminjam", "Waktu Pinjam"]
        else:
            tabel.field_names = ["No", "Kode", "Nama", "Lokasi", "Status"]
        for nomor, kode in enumerate(sorted(data_kunci), start=1):
            kunci = data_kunci[kode]
            baris = [nomor, kode, kunci["nama"], kunci["lokasi"], kunci["status"]]
            if admin:
                baris += [kunci["peminjam"], kunci["waktu"]]
            tabel.add_row(baris)
        tabel.align["Nama"] = "l"
        tabel.align["Lokasi"] = "l"
        print(tabel)
        print("Jumlah kunci dipinjam:", jumlah_dipinjam(), "dari", len(data_kunci))
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
        data_kunci[kode] = {"nama": nama, "lokasi": lokasi, "status": "Tersedia", "peminjam": "-", "waktu": "-"}
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
                kunci["waktu"] = "-"
                print("Status berhasil diubah")
            elif st == "2":
                kunci["status"] = "Dipinjam"
                kunci["peminjam"] = "admin"
                kunci["waktu"] = waktu_sekarang()
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
