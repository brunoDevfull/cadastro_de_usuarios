# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginKxOARj.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class login_form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        Form.setStyleSheet(u"background-color: rgb(57, 146, 255);")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"selection-background-color: rgb(62, 97, 255);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_login = QLabel(self.frame)
        self.label_login.setObjectName(u"label_login")
        font = QFont()
        font.setFamilies([u"Comic Sans MS"])
        font.setPointSize(25)
        font.setBold(True)
        font.setItalic(False)
        self.label_login.setFont(font)
        self.label_login.setStyleSheet(u"background-color: rgb(57, 146, 255);\n"
"text-align: center;")

        self.verticalLayout_2.addWidget(self.label_login)

        self.lineEdit_login = QLineEdit(self.frame)
        self.lineEdit_login.setObjectName(u"lineEdit_login")
        palette = QPalette()
        brush = QBrush(QColor(255, 255, 255, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        palette.setBrush(QPalette.Active, QPalette.Window, brush)
        brush1 = QBrush(QColor(62, 97, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush1)
        self.lineEdit_login.setPalette(palette)
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit_login.setFont(font1)
        self.lineEdit_login.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"text-align: center;")

        self.verticalLayout_2.addWidget(self.lineEdit_login)


        self.verticalLayout.addWidget(self.frame)

        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_senha = QLabel(self.frame_2)
        self.label_senha.setObjectName(u"label_senha")
        self.label_senha.setFont(font)

        self.verticalLayout_3.addWidget(self.label_senha)

        self.lineEdit_senha = QLineEdit(self.frame_2)
        self.lineEdit_senha.setObjectName(u"lineEdit_senha")
        self.lineEdit_senha.setFont(font1)
        self.lineEdit_senha.setStyleSheet(u"background-color: rgb(65, 172, 154);\n"
"background-color: rgb(255, 255, 255);")

        self.verticalLayout_3.addWidget(self.lineEdit_senha)


        self.verticalLayout.addWidget(self.frame_2)

        self.btn_login = QPushButton(Form)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))

        self.verticalLayout.addWidget(self.btn_login)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.lineEdit_login.setPlaceholderText(QCoreApplication.translate("Form", u"digite seu email", None))
        self.label_senha.setText(QCoreApplication.translate("Form", u"SENHA", None))
        self.lineEdit_senha.setPlaceholderText(QCoreApplication.translate("Form", u"digite sua senha", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"LOGAR", None))
    # retranslateUi

