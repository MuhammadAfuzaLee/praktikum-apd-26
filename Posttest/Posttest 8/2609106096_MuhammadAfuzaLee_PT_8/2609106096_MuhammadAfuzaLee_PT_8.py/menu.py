from utils import bersihkan, tunggu, tampil_menu
from kunci import lihat_kunci, tambah_kunci, ubah_kunci, hapus_kunci
from peminjaman import pinjam_kunci, kembalikan_kunci


def menu_admin():
    while True:
        bersihkan()
        tampil_menu("MENU ADMIN", ["Tambah kunci", "Lihat daftar kunci", "Ubah lokasi atau status", "Hapus kunci", "Logout"])
        try:
            menu = int(input("Pilih: "))
        except ValueError:
            print("Input harus berupa angka")
            tunggu()
        else:
            if menu == 1:
                lihat_kunci(True)
                tambah_kunci()
            elif menu == 2:
                lihat_kunci(True)
            elif menu == 3:
                lihat_kunci(True)
                ubah_kunci()
            elif menu == 4:
                lihat_kunci(True)
                hapus_kunci()
            elif menu == 5:
                break
            else:
                print("Menu tidak ada")
                tunggu()


def menu_pengguna(username):
    while True:
        bersihkan()
        tampil_menu("MENU PENGGUNA", ["Lihat daftar kunci", "Pinjam kunci", "Kembalikan kunci", "Logout"])
        try:
            menu = int(input("Pilih: "))
        except ValueError:
            print("Input harus berupa angka")
            tunggu()
        else:
            if menu == 1:
                lihat_kunci(False)
            elif menu == 2:
                lihat_kunci(False)
                pinjam_kunci(username)
            elif menu == 3:
                lihat_kunci(False)
                kembalikan_kunci(username)
            elif menu == 4:
                break
            else:
                print("Menu tidak ada")
                tunggu()
