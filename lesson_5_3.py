# coding=utf8
import random
import collections

print ("Генерируем список из 15ти чисел")

lst = []
i = 15
while i > 0:
    lst.append(int(random.random() * 10))
    i -= 1

print("Получили список из: %s" % lst)
lst.sort()
print("Сортируем список: %s" % lst)
count = collections.Counter(lst)
count_list = count.most_common()

print ("Самое часто встречающееся число  и его кол-во в списке")
print (count_list[0])

