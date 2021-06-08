from encryption import *
from decryption import *


def get_path_to_file():
    path_to_file = input("Введите путь до файла: ")
    return path_to_file


def get_file_password():
    password = input("Введите пароль: ")
    return password


def choose_the_action():
    choose = input("Выберите\nЗашифровать/расшифровать файл(ы): ")
    if choose == "зашифровать":
        dir_walk(get_path_to_file(), get_file_password())
    elif choose == "расшифровать":
        dir_walk_1(get_path_to_file(), get_file_password())
    else:
        print("Error")


if __name__ == '__main__':
    while True:
        choose_the_action()
