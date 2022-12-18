# Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

n = int(input("Ведите число: "))
list_numbers = []
summ = 0
for i in range(1, n+1):
    value = (1+1/i)**i
    list_numbers.append(value)
    summ += value
print(list_numbers)
print(summ)
