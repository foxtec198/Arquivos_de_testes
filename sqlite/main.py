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

def inserir(*dado):
    c.execute(f'''
            INSERT INTO dados(nome, cpf, dn)
            VALUES ('{dado[0]}','{dado[1]}','{dado[2]}')
            ''')
    print(f'{dado[0]} Inserido no banco de dados')
    
# inserir('GUILHERME', '12345678910', '24/05/2023')