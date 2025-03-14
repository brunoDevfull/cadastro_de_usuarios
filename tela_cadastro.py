# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tela_cadastroSKVdXy.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(460, 931)
        self.verticalLayout_3 = QVBoxLayout(Form)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.DADOS_PESSOAIS = QFrame(Form)
        self.DADOS_PESSOAIS.setObjectName(u"DADOS_PESSOAIS")
        self.DADOS_PESSOAIS.setStyleSheet(u"background-color: rgb(46, 94, 226);\n"
"font: 9pt \"Nirmala UI\";")
        self.DADOS_PESSOAIS.setFrameShape(QFrame.Shape.StyledPanel)
        self.DADOS_PESSOAIS.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.DADOS_PESSOAIS)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.title_dados_pessoais = QLabel(self.DADOS_PESSOAIS)
        self.title_dados_pessoais.setObjectName(u"title_dados_pessoais")
        self.title_dados_pessoais.setStyleSheet(u"font: 14pt \"Comic Sans MS\";\n"
"")

        self.verticalLayout.addWidget(self.title_dados_pessoais)

        self.nome_completo = QLabel(self.DADOS_PESSOAIS)
        self.nome_completo.setObjectName(u"nome_completo")
        self.nome_completo.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.nome_completo)

        self.lineEdit_nome_completo = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_nome_completo.setObjectName(u"lineEdit_nome_completo")
        self.lineEdit_nome_completo.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 9pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.lineEdit_nome_completo)

        self.label_sexo = QLabel(self.DADOS_PESSOAIS)
        self.label_sexo.setObjectName(u"label_sexo")
        self.label_sexo.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.label_sexo)

        self.sx_masculino = QRadioButton(self.DADOS_PESSOAIS)
        self.sx_masculino.setObjectName(u"sx_masculino")

        self.verticalLayout.addWidget(self.sx_masculino)

        self.sx_feminino = QRadioButton(self.DADOS_PESSOAIS)
        self.sx_feminino.setObjectName(u"sx_feminino")

        self.verticalLayout.addWidget(self.sx_feminino)

        self.dataNascimento = QLabel(self.DADOS_PESSOAIS)
        self.dataNascimento.setObjectName(u"dataNascimento")
        self.dataNascimento.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.dataNascimento)

        self.lineEdit_dataNascimento = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_dataNascimento.setObjectName(u"lineEdit_dataNascimento")
        self.lineEdit_dataNascimento.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit_dataNascimento)

        self.cpf = QLabel(self.DADOS_PESSOAIS)
        self.cpf.setObjectName(u"cpf")
        self.cpf.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.cpf)

        self.lineEdit_cpf = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_cpf.setObjectName(u"lineEdit_cpf")
        self.lineEdit_cpf.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit_cpf)

        self.email = QLabel(self.DADOS_PESSOAIS)
        self.email.setObjectName(u"email")
        self.email.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.email)

        self.lineEdit_email = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_email.setObjectName(u"lineEdit_email")
        self.lineEdit_email.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit_email)

        self.label_login = QLabel(self.DADOS_PESSOAIS)
        self.label_login.setObjectName(u"label_login")
        self.label_login.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        self.lineEdit_login.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit_login)

        self.label_senha = QLabel(self.DADOS_PESSOAIS)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout.addWidget(self.label_senha)

        self.lineEdit_senha = QLineEdit(self.DADOS_PESSOAIS)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.lineEdit_senha)


        self.verticalLayout_3.addWidget(self.DADOS_PESSOAIS)

        self.ENDERECO = QFrame(Form)
        self.ENDERECO.setObjectName(u"ENDERECO")
        self.ENDERECO.setStyleSheet(u"background-color: rgb(46, 94, 226);\n"
"font: 9pt \"Nirmala UI\";")
        self.ENDERECO.setFrameShape(QFrame.Shape.StyledPanel)
        self.ENDERECO.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.ENDERECO)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.title_endereco = QLabel(self.ENDERECO)
        self.title_endereco.setObjectName(u"title_endereco")
        self.title_endereco.setStyleSheet(u"font: 14pt \"Comic Sans MS\";")

        self.verticalLayout_2.addWidget(self.title_endereco)

        self.cep = QLabel(self.ENDERECO)
        self.cep.setObjectName(u"cep")
        self.cep.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.cep)

        self.lineEdit_cep = QLineEdit(self.ENDERECO)
        self.lineEdit_cep.setObjectName(u"lineEdit_cep")
        self.lineEdit_cep.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_cep)

        self.cidade = QLabel(self.ENDERECO)
        self.cidade.setObjectName(u"cidade")
        self.cidade.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.cidade)

        self.lineEdit_cidade = QLineEdit(self.ENDERECO)
        self.lineEdit_cidade.setObjectName(u"lineEdit_cidade")
        self.lineEdit_cidade.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_cidade)

        self.estado = QLabel(self.ENDERECO)
        self.estado.setObjectName(u"estado")
        self.estado.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.estado)

        self.lineEdit_estado = QLineEdit(self.ENDERECO)
        self.lineEdit_estado.setObjectName(u"lineEdit_estado")
        self.lineEdit_estado.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_estado)

        self.rua = QLabel(self.ENDERECO)
        self.rua.setObjectName(u"rua")
        self.rua.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.rua)

        self.lineEdit_rua = QLineEdit(self.ENDERECO)
        self.lineEdit_rua.setObjectName(u"lineEdit_rua")
        self.lineEdit_rua.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_rua)

        self.numero = QLabel(self.ENDERECO)
        self.numero.setObjectName(u"numero")
        self.numero.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.numero)

        self.lineEdit_numero = QLineEdit(self.ENDERECO)
        self.lineEdit_numero.setObjectName(u"lineEdit_numero")
        self.lineEdit_numero.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_numero)

        self.bairro = QLabel(self.ENDERECO)
        self.bairro.setObjectName(u"bairro")
        self.bairro.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.bairro)

        self.lineEdit_bairro = QLineEdit(self.ENDERECO)
        self.lineEdit_bairro.setObjectName(u"lineEdit_bairro")
        self.lineEdit_bairro.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_bairro)

        self.complemento = QLabel(self.ENDERECO)
        self.complemento.setObjectName(u"complemento")
        self.complemento.setStyleSheet(u"font: 10pt \"Nirmala UI\";")

        self.verticalLayout_2.addWidget(self.complemento)

        self.lineEdit_complemento = QLineEdit(self.ENDERECO)
        self.lineEdit_complemento.setObjectName(u"lineEdit_complemento")
        self.lineEdit_complemento.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.lineEdit_complemento)


        self.verticalLayout_3.addWidget(self.ENDERECO)

        self.pushButton_cadastrar = QPushButton(Form)
        self.pushButton_cadastrar.setObjectName(u"pushButton_cadastrar")
        self.pushButton_cadastrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 13pt \"Nirmala UI\";\n"
"\n"
"background-color: rgb(0, 176, 0);")

        self.verticalLayout_3.addWidget(self.pushButton_cadastrar)

        self.pushButton_cancelar = QPushButton(Form)
        self.pushButton_cancelar.setObjectName(u"pushButton_cancelar")
        self.pushButton_cancelar.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"font: 13pt \"Nirmala UI\";")

        self.verticalLayout_3.addWidget(self.pushButton_cancelar)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.title_dados_pessoais.setText(QCoreApplication.translate("Form", u"DADOS PESSOAIS", None))
        self.nome_completo.setText(QCoreApplication.translate("Form", u"Nome Completo", None))
        self.label_sexo.setText(QCoreApplication.translate("Form", u"Sexo", None))
        self.sx_masculino.setText(QCoreApplication.translate("Form", u"Masculino", None))
        self.sx_feminino.setText(QCoreApplication.translate("Form", u"Feminino", None))
        self.dataNascimento.setText(QCoreApplication.translate("Form", u"Data de Nascimento", None))
        self.cpf.setText(QCoreApplication.translate("Form", u"CPF", None))
        self.email.setText(QCoreApplication.translate("Form", u"Email", None))
        self.label_login.setText(QCoreApplication.translate("Form", u"Crie seu Login", None))
        self.label_senha.setText(QCoreApplication.translate("Form", u"Crie sua Senha", None))
        self.title_endereco.setText(QCoreApplication.translate("Form", u"ENDERE\u00c7O", None))
        self.cep.setText(QCoreApplication.translate("Form", u"CEP", None))
        self.cidade.setText(QCoreApplication.translate("Form", u"Cidade", None))
        self.estado.setText(QCoreApplication.translate("Form", u"Estado", None))
        self.rua.setText(QCoreApplication.translate("Form", u"Rua", None))
        self.numero.setText(QCoreApplication.translate("Form", u"Numero", None))
        self.bairro.setText(QCoreApplication.translate("Form", u"Bairro", None))
        self.complemento.setText(QCoreApplication.translate("Form", u"Complemento - opcional", None))
        self.pushButton_cadastrar.setText(QCoreApplication.translate("Form", u"CADASTRAR", None))
        self.pushButton_cancelar.setText(QCoreApplication.translate("Form", u"CANCELAR", None))
    # retranslateUi

