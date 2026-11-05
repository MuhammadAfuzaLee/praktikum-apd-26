import auth
from data import batas_login
from utils import bersihkan, tunggu, tampil_menu

while True:
    if auth.login_gagal >= batas_login:
        print("Terlalu banyak gagal login, program dihentikan")
        break

    bersihkan()
    tampil_menu("SISTEM MANAJEMEN KUNCI CADANGAN", ["Login", "Register", "Keluar"])
    try:
        pilih = int(input("Pilih: "))
    except ValueError:
        print("Input harus berupa angka")
        tunggu()
    else:
        if pilih == 1:
            auth.login()
        elif pilih == 2:
            auth.register()
        elif pilih == 3:
            print("Program selesai")
            break
        else:
            print("Pilihan tidak ada")
            tunggu()
