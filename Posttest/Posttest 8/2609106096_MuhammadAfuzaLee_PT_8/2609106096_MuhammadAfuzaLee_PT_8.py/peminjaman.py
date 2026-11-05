from data import data_kunci
from utils import tunggu, input_kode, waktu_sekarang


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
        kunci["waktu"] = waktu_sekarang()
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
        kunci["waktu"] = "-"
        print("Kunci berhasil dikembalikan")
    finally:
        tunggu()
