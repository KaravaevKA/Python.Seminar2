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
