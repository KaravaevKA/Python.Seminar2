#Работа в классе
#Задача 9
#По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# x=int(input('Введите число: '))
# n=1
# while x > 0:
#     n*=x
#     x-=1
# print(n)

#Задача 11
#Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
#Если А не является числом Фибоначчи, выведите число -1.

# def fib(n: int) -> int:
#     old_n = 0
#     new_n = 1
#     fib = 0
#     for i in range(n-1):
#         fib = old_n + new_n
#         old_n, new_n = new_n, fib
#     return fib
# number = int (input ("натуральное число A > 1 - > "))

# flag =True
# i = 1
# while(flag):
#     if fib(i) < number:
#         i+=1
#     elif fib(i) == number:
#         print(i)
#         flag = False
#     else:
#         print(-1)
#         flag = False

#Задача 13. Определить наибольшее кол-во дней с положительной температурой в заданном интервале
# import random
# n = int(input('Введите число дней: '))
# count = 0
# day_max = 0

# for i in range(n):
#     temperature = random.randint(-50, 50)
#     if temperature >0: 
#         count+=1
#     else:
#         if day_max < count:
#             day_max = count
#         count = 0
# if day_max < count:
#     day_max = count
# print(day_max)

#Задача 15

# import random
# num = int(input('Укажите количество арбузов: '))
# min=25
# max=0
# for i in range(num):
#     arbuz=random.randint(3, 25)
#     if arbuz>max:
#         max = arbuz
#     if arbuz<min:
#         min = arbuz
# print(f"Арбуз для тещи: {min} кг. Арбуз себе: {max} кг.")


#ДОМАШНЯЯ РАБОТА
# Задача 10
# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. 
# Выведите минимальное количество монет, которые нужно перевернуть

# import random
# n = int(input('Укажите количество монет: '))
# orel = 0
# reshka = 0
# for i in range(n):
#     monetka = random.randint(0, 1)
#     print(monetka)
#     if monetka == 1:
#         orel+=1
#     else: reshka+=1
# if orel > reshka:
#     print(f'Необходимо перевернуть {reshka} монет')
# elif reshka > orel:
#     print(f'Необходимо перевернуть {orel} монет')
# else:
#     print(f'На столе равное количество монет с орлом и решкой, переворачивайте любые {orel}')

# Задача 12
# x = int(input())
# y = int(input())
# for i in range(x):
#     for j in range(y):
#         if x == i + j and y == i * j:
#             print(i, j)

# Задача 14
# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N

N = int(input('Введите число: '))
numTwo = 1
while numTwo <= N:
    print(numTwo)
    numTwo*=2