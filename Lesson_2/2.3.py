""" 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.
in
6

out
[2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
14.071 """

num = int(input('Input your number: '))
sum_of_nums = 0
list_of_nums = []

for i in range(1, num + 1):
    res = round((1 + 1 / i) ** i, 3)
    list_of_nums.append(res)
    sum_of_nums += res

print(list_of_nums)
print(sum_of_nums)