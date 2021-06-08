import pyAesCrypt
import os


def decrypt_file(file, password):
    # создаём буфер
    buffer_size = 512 * 1024
    # вызываем метод decrypt
    pyAesCrypt.decryptFile(
        str(file),
        str(os.path.splitext(file)[0]),
        password,
        buffer_size
    )
    # выводим дешифрованный файл в консоль
    print(f"Файл {os.path.splitext(file)[0]} расшифрован")
    # удаляем старый файл
    os.remove(file)


def dir_walk_1(directory, password):
    for name in os.listdir(directory):
        path = os.path.join(directory, name)
        if os.path.isfile(path):
            try:
                decrypt_file(path, password)
            except Exception as ex:
                print(ex)
        else:
            dir_walk_1(path, password)
