from sqlite3 import connect, Cursor

conn = connect('sqlite/db/banco_dados.db')
c = conn.cursor()
