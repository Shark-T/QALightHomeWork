# coding=utf8

type_l = ["Hello", 2, "world", 3, 25.3]
print ("Привет, у нас есть список")
print (type_l)
print ("Состоящий из - ")


# def decode_list(li):
#     for item in li:
#         if isinstance(item, int):
#             print("Целое число")
#         elif isinstance(item, str):
#             print("Строка")
#         else:
#             print("Другое")


for item in type_l:
        if isinstance(item, int):
            print("Целое число")
        elif isinstance(item, str):
            print("Строка")
        else:
            print("Другое")

# print(decode_list(type_l))

print ("Пока )))")

# companies = ["Microsoft", "Google", "Oracle", "Apple"]
# i = 0
# while i < len(companies):
#     print(companies[i])
#     i += 1
