from sqlite3 import connect

conn = connect('sqlite/db/banco_dados.db')
c = conn.cursor()

def criar_tabela():
    c.execute('''
            CREATE TABLE IF NOT EXISTS dados(
                id INTEGER PRIMARY KEY AUTOINCREMENT, 
                nome TEXT,
                cpf INTEGER,
                dn TEXT) 
            ''')

def inserir(*dado):
    c.execute(f'''
            INSERT INTO dados(
                nome, 
                cpf, 
                dn)
            VALUES(
                '{dado[0]}',
                '{dado[1]}',
                '{dado[2]}')
            ''')
    conn.commit()
    print(f'{dado[0]} Inserido no banco de dados')
    
def cons(*dados_cons):
    dados = c.execute(f'''
              SELECT nome, cpf, dn FROM dados
              WHERE id = '{dados_cons[0]}'
              ''').fetchall()
    try:
        for i in dados[0]:
            print(i)
    except IndexError:
        print('Funcionario não encontrado!')

while True:
    ent = input('Digite o id: ')
    if ent.lower() == 'sair' : break
    cons(ent)