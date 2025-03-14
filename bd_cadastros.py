import mysql.connector

# Função para conectar ao banco de dados
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastros"
    )

# Função para adicionar um usuário
def adicionar_usuario(login, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "INSERT INTO usuarios (login, senha) VALUES (%s, SHA2(%s, 256))"
    valores = (login, senha)
    cursor.execute(sql, valores)
    conexao.commit()
    cursor.close()
    conexao.close()
    print("Usuário cadastrado com sucesso!")

# função para verificar se o usuario existe
def verificar_usuario(login, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM usuarios WHERE login = %s AND senha = SHA2(%s, 256)"
    valores = (login, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    if resultado:
        print("Login bem-sucedido!")
        return True
    else:
        print("Login ou senha incorretos.")
        return False

#adicionando usuarios no banco de dados
# adicionar_usuario("Mauricio","987")
# adicionar_usuario("Sam","123")
