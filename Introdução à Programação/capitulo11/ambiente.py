import sqlite3

connection = sqlite3.connect('agenda.db')
cursor = connection.cursor()

create = 'create table agenda (nome text, telefone text)'
values = [('Vinicius', '2305'), ('Alessandra', '0709'), ('Niara', '1234')]
insert = '''insert into agenda (nome, telefone) values (?, ?)'''
select = 'select * from agenda'

cursor.executemany(insert, values)
# cursor.execute('delete from agenda')
cursor.execute(select)
res = cursor.fetchall()

for registro in res:
    print(f'{registro[0]} {registro[1]}')

connection.commit()
cursor.close()
connection.close()
