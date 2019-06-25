import sqlite3
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()

def function():
    print("До изменений:")
    for row in cursor.execute("SELECT * FROM magasin"):
        print(row)
    dele=input("1-добавить, 2-удалить запись, 3- редактирование \n")
    if dele is '2':
        i=int(input("Введите запись, которую хотите удалить(по id) \n"))
        cursor.execute("DELETE FROM magasin WHERE id =?",(i,))
        conn.commit()
    elif dele is '1':
        print("Введите запись ")
        id=int(input("id(int!) \n"))
        nameshop = input("nameshop  \n")
        thing = input("thing  \n")
        price =int( input("price  \n"))
        sale = input("sale(%)  \n")
        sate = input("sate  \n")
        tel = input("telephone  \n")
        cursor.execute('''INSERT INTO magasin (id,nameshop, thing, price,
                   sale, sate, tel) VALUES (?,?,?,?,?,?,?)''',
                   (id,nameshop, thing, price, sale, sate, tel))
        conn.commit()
    elif dele=='3':
        i1=int(input("Введите номер записи, которую хотите отредактировать \n"))
        i=input("Введите поле, которое хотитет отредакитровать \n")
        i2=input("Введите то, на что хотите изменить запись \n")
        cursor.execute("""UPDATE magasin SET  {0} = ? WHERE id = ?""".format(i),(i2,i1))
        conn.commit()
    print("После изменений ")
    for row in cursor.execute("SELECT * FROM magasin"):
        print(row)
    print("Запустить программу еще раз? 1-да 0-нет")
    answer=input()
    if answer is '1':
        function()
function()