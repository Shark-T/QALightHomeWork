# coding=utf8
import sqlite3
import PbDb

PbDb.create_table()

act = int (input("Телефоная книга \n"
      "Посмотреть, введите 1\n"
      "Добавить запись, введите 2\n"
      "Изменить номер абонента, введите 3\n"
      "Изменить E-mail абонента, введите 4\n"
      "Удалить абонента, введите 5\n"
      "Введите номер 1-5 --  "))

if act == 1:
    PbDb.read_user()
elif act == 2:
    PbDb.create_user()
elif act == 3:
    PbDb.upd_num()
elif act == 4:
    PbDb.upd_email()
elif act == 5:
    PbDb.del_user()
else: print("Введен некоректный номер, перезапустите программу. ")
