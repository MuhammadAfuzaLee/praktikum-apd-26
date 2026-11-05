import os
from datetime import datetime
from prettytable import PrettyTable
from data import data_kunci


def bersihkan():
    os.system("cls" if os.name == "nt" else "clear")


def tunggu():
    input("Tekan enter...")


def waktu_sekarang():
    return datetime.now().strftime("%d-%m-%Y %H:%M")


def input_kode():
    kode = input("Kode kunci: ").upper()
    if kode == "":
        raise ValueError("Kode tidak boleh kosong")
    return kode


def tampil_menu(judul, daftar_menu):
    tabel = PrettyTable()
    tabel.title = judul
    tabel.field_names = ["No", "Menu"]
    tabel.align["Menu"] = "l"
    tabel.min_width["Menu"] = max(len(judul) - 5, 10)
    for nomor, menu in enumerate(daftar_menu, start=1):
        tabel.add_row([nomor, menu])
    print(tabel)


def hitung_dipinjam(daftar, i):
    if i == len(daftar):
        return 0
    if data_kunci[daftar[i]]["status"] == "Dipinjam":
        return 1 + hitung_dipinjam(daftar, i + 1)
    return hitung_dipinjam(daftar, i + 1)


def jumlah_dipinjam():
    daftar = list(data_kunci)
    return hitung_dipinjam(daftar, 0)
