# coding=utf8
import sqlite3

conn = sqlite3.connect('PhBook.db')
cur = conn.cursor()


def create_table():
    cur.execute("CREATE TABLE IF NOT EXISTS PhoneBook(id INTEGER PRIMARY KEY, f_name TEXT, l_name TEXT,"
                " phone_number INTEGER, email TEXT)")


create_table()


def create_user():
    user_data = (int(input("Введите ID  - ")),input("Введите Имя - "), input("Введите Фамилию - "),
                     int(input("Введите номер тел. - ")), input("Введите E-mail - "))
    cur.execute("INSERT INTO PhoneBook VALUES(?,?,?,?,?)", user_data)
    conn.commit()


def read_user():
    id1 = input("Введите ID - ")
    cur.execute("SELECT f_name, l_name, phone_number, email FROM PhoneBook WHERE id = ?", id1)
    db_data = cur.fetchall()
    for item in db_data:
        db_data_u = item
    print("Имя - %s" % db_data_u[0])
    print("Фамилия - %s" % db_data_u[1])
    print("Номер тел. - %s" % db_data_u[2])
    print("E-mail - %s" % db_data_u[3])


def upd_num():
    id1 = input("Введите ID - ")
    newNum = input("Ввведите новый телефон - ")
    cur.execute("UPDATE PhoneBook SET phone_number = ? WHERE id = ?", (newNum, id1))
    conn.commit()
    print("Номер заменен на - %s" % newNum)


def upd_email():
    id1 = input("Введите ID - ")
    newEmail = input("Ввведите новый E-mail - ")
    cur.execute("UPDATE PhoneBook SET email = ? WHERE id = ?", (newEmail, id1))
    conn.commit()
    print("E-mail заменен на - %s" % newEmail)


def del_user():
    id1 = input("Введите ID - ")
    cur.execute("DELETE FROM PhoneBook WHERE id = ?",  id1)
    conn.commit()
    print("Запись в книге удалена")



