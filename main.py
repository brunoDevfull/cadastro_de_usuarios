from PySide6.QtWidgets import QApplication, QWidget, QMessageBox
from PySide6.QtCore import QCoreApplication
import sys
import mysql.connector
from login import login_form
from tela_cadastro import Ui_Form 

class LoginApp(QWidget, login_form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.btn_login.clicked.connect(self.verificar_login)

    def verificar_login(self):
        login = self.lineEdit_login.text()
        senha = self.lineEdit_senha.text()

        if verificar_usuario(login, senha):
            QMessageBox.information(self, "Sucesso", "Login bem-sucedido!")
            self.cadastro_window = CadastroApp()
            self.cadastro_window.show()
            self.close()
        else:
            QMessageBox.warning(self, "Erro", "Login ou senha incorretos.")

        
def verificar_usuario(login, senha):
    conexao = conectar()
    cursor = conexao.cursor()
    sql = "SELECT * FROM usuarios WHERE login = %s AND senha = SHA2(%s, 256)"
    valores = (login, senha)
    cursor.execute(sql, valores)
    resultado = cursor.fetchone()
    cursor.close()
    conexao.close()
    return resultado is not None

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastros"
    )


class CadastroApp(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton_cadastrar.clicked.connect(self.cadastrar_usuario)

    def cadastrar_usuario(self):
        login = self.lineEdit_login.text()
        senha = self.lineEdit_senha.text()

        if adicionar_usuario(login, senha):
            QMessageBox.information(self, "Sucesso", "Usuário cadastrado com sucesso!")
            self.login_window = LoginApp()
            self.login_window.show()
            self.close()
            
        else:
            QMessageBox.warning(self, "Erro", "Erro ao cadastrar usuário.")

def adicionar_usuario(login, senha):
    try:
        conexao = conectar()
        cursor = conexao.cursor()
        sql = "INSERT INTO usuarios (login, senha) VALUES (%s, SHA2(%s, 256))"
        valores = (login, senha)
        cursor.execute(sql, valores)
        conexao.commit()
        cursor.close()
        conexao.close()
        return True
    except mysql.connector.Error as err:
        print(f"Erro: {err}")
        return False

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="cadastros"
    )

if __name__ == "__main__":
    app = QApplication(sys.argv)
    form = LoginApp()
    form.show()
    sys.exit(app.exec())



    