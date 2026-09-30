#%% md
# Задача 7. Заполнить файл последовательного доступа N действительными числами, полученным с помощью датчика случайных чисел. Найти сумму максимального и минимального элементов этого файла.
#%%
import random

def fill_file(filename, n):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in range(n):
            number = random.uniform(0, 10.00)
            file.write(f"{number}\n")


def sum_min_max(filename):
    minimum = 0
    maximum = 0

    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            number = float(line)
            if number < minimum:
                minimum = number
            elif number > maximum:
                maximum = number
    return minimum + maximum