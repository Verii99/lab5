import sqlite3
conn = sqlite3.connect("BD.db")
cursor = conn.cursor()
magasin=[(1,'Детский мир','Игрушка Слон',1700,20,'detmir.com','999-99-99'),
           (2,'Кошкин дом','Лоток',400,5,'catshop.ru','988-98-89'),
           (3,'Зебра','Помидоры',88,10,'zebra.ru','888-77-66'),
           (4,'Bershka','Джинсы',2100,0,'bershka.ru','487-98-4'),
           (5,'Hoff','Диван',27000,35,'hoff.com','124-54-78'),
           (6,'Fuzetea','Сок',45,0,'teasoc.com','453-78-78')]
cursor.executemany("INSERT INTO magasin VALUES (?,?,?,?,?,?,?)", magasin)
conn.commit()