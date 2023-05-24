from sqlite3 import connect, Cursor

conn = connect('sqlite/db/banco_dados.db')
c = conn.cursor()

c.execute('''
          CREATE TABLE IF NOT EXISTS dados
          (
              id INTEGER PRIMARY KEY AUTOINCREMENT, 
              nome TEXT,
              cpf INTEGER,
              dn TEXT
          )
          ''')