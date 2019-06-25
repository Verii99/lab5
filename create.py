import sqlite3
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()
cursor.execute("""CREATE TABLE IF NOT EXISTS magasin
                  (id integer,nameshop text, thing text, price integer, sale integer,
                   sate text, tel  text)""")