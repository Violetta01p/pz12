import random


# Створення списку чисел з повторами
numbers = [random.randint(1, 100) for _ in range(1000)]


# Словник для підрахунку повторів
counter = {}


# Підрахунок
for number in numbers:
   if number in counter:
       counter[number] += 1
   else:
       counter[number] = 1


# Пошук числа з найбільшою кількістю повторів
max_number = None
max_count = 0


for number in counter:
   if counter[number] > max_count:
       max_count = counter[number]
       max_number = number


print(f"Число, що найчастіше повторюється: {max_number}, кількість повторень: {max_count}")
