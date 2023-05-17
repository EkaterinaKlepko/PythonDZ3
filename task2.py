# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

n = int(input('Введите количество элементов в списке: '))
my_list = []
for i in range(n):
    my_list.append(int(input('Введите элемент массива: ')))
print(my_list)
x = int(input('Введите число: '))
raznica = x - my_list[0]
temp = 0
for i in my_list:
    if (x - i) < raznica:
        raznica = x - i
        if raznica < 0:
            raznica = -raznica
        temp = i
print(temp)
