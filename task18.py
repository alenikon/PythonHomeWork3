# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X.
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве.
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
A=[]
N = int(input('Введите количество элементов в массиве N:  '))
for i in range(N):
    A.append(random.triangular(0, 10))
    A[i] = round(A[i],1)
print(A)
X = float(input('Введите искомое число:  '))
min = abs(X - A[0])
index = 0
for i in range(N):
    count = abs(X - A[i])
    if count < min:
        min = count
        index = i
#       print(A[i])
print(f'Наиболее близкое к искомому: {A[index]}')

# if count == 3 or count == 4:
#     print(f'Число {X} встречается в массиве {count} раза')
# else: print(f'Число {X} встречается в массиве {count} раз')

# if orel < reshka:
#     print(f'Переверните {orel} монет с орла на решку, их меньше всего')
# elif orel == reshka:
#     print(f'Количество орлов и решек одинаково, по {orel} штук')

# n = int(input('Введите число N'))
# i = 0
# while 2 ** i <= n:
#     print('2 в степени ', i, ' = ', 2 ** i)
#     i += 1