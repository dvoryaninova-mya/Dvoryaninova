# # Задача 6.1
# def delitsa_na_3(num):
#     return num % 3 == 0
# number = int(input("Введите число: "))
# if delitsa_na_3(number):
#     print ("Делится на 3")
# else:
#     print("Не делится на 3")



# # Задача 6.2
# def delenie_100(num):
#     return 100 // num
# try:
#     num = int(input ("Введите число: "))
#     res = delenie_100(num)
#     print ("Результат: ", res)
# except ValueError:
#     print ("Ошибка: введено не число!")
# except ZeroDevisionError:
#     print ("Ошибка: деление на ноль")



# Задача 6.3
def magic_date (day, month, year):
    return day * month == year % 100
day = int(input("Введите день: "))
month = int(input("Введите месяц: "))
year = int(input("Введите год: "))
if magic_date (day, month, year):
    print ("Дата магическая!")
else:
    print ("Дата не магическая!")



# Задача 6.4
def lucky_ticket(ticket):
    if not ticket.isdigit():
        return "Ошибка: введите только цифры!"
    if len(ticket) % 2 != 0:
        return "Ошибка: количество цифр должно быть чётным!"
    half = len(ticket) // 2
    first_half = ticket[:half]
    second_half = ticket[half:]
    sum1 = 0
    for digit in first_half:
        sum1 = sum1 + int(digit)
    sum2 = 0
    for digit in second_half:
        sum2 = sum2 + int(digit)
    if sum1 == sum2:
        return True
    else:
        return False
ticket = input("Введите номер билета: ")
result = lucky_ticket(ticket)
if result == True:
    print("Билет", ticket, "- счастливый!")
elif result == False:
    print("Билет", ticket, "- не счастливый")
else:
    print(result)
