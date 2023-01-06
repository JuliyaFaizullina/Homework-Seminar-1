number = int(input('Введите количество элементов списка: '))
list = []
sum = 0
for i in range(number):
    list_number = int(input(f'Введите число {i+1} : '))
    list.append(list_number)
    if i % 2 != 0:
        sum += list[i]
print ("Сумма чисел на нечетных позициях равна", sum)