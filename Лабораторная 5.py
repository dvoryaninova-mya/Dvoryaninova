# Задание 5.1
n = int(input("Сколько слов вы хотите ввести: "))
result = ""
for i in range(n):
    word = input("Введите слово: ")
    result = result + word + " "
print("Итоговая строка:", result)


# Задание 5.2
result = ""
while True:
    word = input("Введите слово (или 'stop' для выхода): ")
    if word == "stop":
        break
    result = result + word + " "
print("Итоговая строка:", result)


# Задание 5.3
while True:
    word = input("Введите слово (или 'stop' для выхода): ")
    if word == "stop":
        break
    if "ф" in word.lower():
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")


# Задание 5.4
import random
errors = 0
correct = 0
while errors < 3:
    a = random.randint(1, 10)
    b = random.randint(1, 10)
    answer = int(input(f"{a} + {b} = "))
    if answer == a + b:
        print("Правильно!")
        correct += 1
    else:
        print("Ответ неверный")
        errors += 1
print("Игра окончена. Правильных ответов:", correct)
