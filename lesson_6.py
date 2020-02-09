# coding=utf8

pb = {}

i = 2
while i >= 0:
    pb[input('Введите имя: ')] = input('Введите телефон: ')
    i -= 1

print("Справочник создан")
name = input("Введите имя абонента ")

for key in pb:
    if key == name:
        print("У абонента - " + str.upper(name) + " Номер :" + pb[key])
