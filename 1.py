""" 1. Напишите программу, которая принимает на вход цифру, обозначающую день недели, и проверяет, является ли этот день выходным.
*Пример:*

- 6 -> да
- 7 -> да
- 1 -> нет """

n = int(input("Enter your number: "))

if 1 <= n <= 5 :
    print("No")
elif 6 <= n <= 7:
    print("Yes")
else:
    print("Not valid")