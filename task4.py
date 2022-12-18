# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

import random

n = int(input("Ведите число: "))
list_numbers = []
for _ in range(n):
    list_numbers.append(random.randrange(-n, n+1))
product = 1
positions = open('file.txt', 'r')
for line in positions:
    product *= list_numbers[int(line)]
print(list_numbers)
print(product)