from data import data_user, batas_login
from utils import tunggu
from menu import menu_admin, menu_pengguna

login_gagal = 0


def cek_login(username, password):
    if username not in data_user or data_user[username]["password"] != password:
        raise ValueError("Username atau password salah")
    return data_user[username]["role"]


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
