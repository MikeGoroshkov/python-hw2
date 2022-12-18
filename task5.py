# Реализуйте алгоритм перемешивания списка.
import random

initial_list = [1,2,3,4,5,6,7]
new_list = initial_list
for _ in new_list:
    index_1 = random.randrange(len(new_list))
    index_2 = random.randrange(len(new_list))
    temp = new_list[index_1]
    new_list[index_1] = new_list[index_2]
    new_list[index_2] = temp
print(new_list)