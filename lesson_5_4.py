# coding=utf8

drinks = "Vodka Vine Rum Tequila"
print (u"У нас есть такие напитки: {0}".format(drinks))
lst_drinks = drinks.split()
print (u"Самое длинное слово напитка это - {0}".format(max(lst_drinks, key=len)))