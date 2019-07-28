import os
import sys
import shutil

# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

'''
def make_dir():
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
        print(dir_path)
        try:
            os.mkdir(dir_path)
        except FileExistsError:
            print('Такая директория уже существует')
'''


def make_dir(name):
    try:
        os.makedirs(name)
    except FileExistsError:
        print('Такая директория уже существует')


if __name__ == '__main__':
    make_dir("dir_1")

'''
def del_dir():
    for i in range(9):
        dir_path = os.path.join(os.getcwd(), 'dir_' + str(i + 1))
        print(dir_path)
        try:
            os.rmdir(dir_path)
        except FileExistsError:
            print('Такой директории не существует')
'''


def del_dir(name):
    try:
        os.removedirs(name)
    except FileExistsError:
        print('Такой директории не существует')


if __name__ == '__main__':
    del_dir("dir_1")

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

'''
def list_dir():
    l_dir = os.listdir(os.getcwd())
    print(l_dir)
'''


def list_dir():
    _path = os.listdir()
    print("Список файлов текущей директории:")
    for index, element in enumerate(_path, start=1):
        if os.path.isdir(element):
            print(f"{index}. {element}")


if __name__ == '__main__':
    list_dir()

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.


def copy_file():
    file_name = os.path.realpath(__file__)
    new_file = file_name + ".copy"

    if os.path.isfile(new_file) != True:
        shutil.copy(file_name, new_file)
        print(f"{new_file} создан")
    else:
        print("Файл уже скопирован")


if __name__ == '__main__':
    copy_file()
