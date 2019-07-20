# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.


def my_round(number, ndigits):  # 2.1234567

    number *= (10 ** ndigits)  # 212345.67
    number_1 = number % 1  # 0.67

    if number_1 >= 0.5:
        number += (1 - number_1)
    else:
        number -= number_1

    number /= (10 ** ndigits)
    return number


print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))


# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить


def lucky_ticket(ticket_number):
    tn_list = str(ticket_number)

    first = 0  # первые 3 числа
    last = 0  # последние 3 числа

    if len(tn_list) != 6:
        return False

    for i in range(3):
        first += int(tn_list[i])
        last += int(tn_list[-i - 1])

    return first == last


print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
