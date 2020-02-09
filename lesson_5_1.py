# coding=utf8
import random

number = int(random.random() * 1000)

print ("Рандомное число: %s" % number)

mult = 1
summa = 0
while number > 0:
    if number % 10 != 0:
        mult = mult * (number % 10)
    summa = summa + number % 10
    number = number // 10

print ("Сумма цифр: %s" % summa)
