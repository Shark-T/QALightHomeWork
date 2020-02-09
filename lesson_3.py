# coding=utf8

print ("Приветсвую вас")
a = int(input("Введите число от 1 до 5  "))
b = int(input("Введите число от 2 до 5  "))
c = int(input("Введите число от 51 до 300  "))


def func(a, b, c):
    while a <= c:
        a = a * b
        print(a)


func(a, b, c)
print ("THE END")
