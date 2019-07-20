# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1


def fibonacci(n, m):
    f = []
    a = 0
    b = 1
    i = 0

    while i < m:
        a = a + b
        b = a - b
        i += 1
        if i >= n:
            f.append(a)

    print(f)


fibonacci(1, 15)
print()

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()


def sort_to_max(origin_list):
    swap = True  # запуск цикла хотя бы один раз
    while swap:
        swap = False
        for i in range(len(origin_list) - 1):
            if origin_list[i] > origin_list[i + 1]:
                origin_list[i], origin_list[i + 1] = origin_list[i + 1], origin_list[i]  # меняем элементы
                swap = True


bubble_sort = [2, 10, -12, 2.5, 20, -11, 4, 4, 0]

sort_to_max(bubble_sort)
print(bubble_sort)
print()

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


def filter_func(func, iterior):
    array = []

    for i in iterior:

        if func(i) is True:
            array.append(i)

    print(array)


arrayFilter = [4, 5, 2, 7, 11, -5, 5, 1, 9, 9, 0]

filter_func(lambda x: x < 5, arrayFilter)
print()

# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


a1 = [2, 1]
a2 = [2, 2]
a3 = [1, 1]
a4 = [1, 2]


def paral(a1, a2, a3, a4):
    a, b, c, d = a1, a2, a3, a4

    per = 0

    while per < 3:
        length_a = b[0] - a[0]
        length_b = d[0] - c[0]
        length_c = c[1] - a[1]
        length_d = d[1] - b[1]

        if length_a == length_b and length_c == length_d:
            print("Данные точки являются вершинами параллелограмма")
            break
        else:
            a, b, c, d = b, c, d, a
            per += 1
    else:
        print("Данные точки не являются вершинами параллелограмма")


paral(a1, a2, a3, a4)
