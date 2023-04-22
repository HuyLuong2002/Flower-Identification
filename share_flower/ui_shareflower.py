# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'shareflower.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(640, 480)
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setGeometry(QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayoutWidget = QWidget(Dialog)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(100, 40, 441, 240))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label_3 = QLabel(self.verticalLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        font = QFont()
        font.setBold(True)
        self.label_3.setFont(font)

        self.verticalLayout.addWidget(self.label_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.verticalLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.edt_myemail = QLineEdit(self.verticalLayoutWidget)
        self.edt_myemail.setObjectName(u"edt_myemail")
        self.edt_myemail.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.horizontalLayout_2.addWidget(self.edt_myemail)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_5 = QLabel(self.verticalLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_3.addWidget(self.label_5)

        self.edt_mypassword = QLineEdit(self.verticalLayoutWidget)
        self.edt_mypassword.setObjectName(u"edt_mypassword")
        self.edt_mypassword.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_3.addWidget(self.edt_mypassword)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.label_4 = QLabel(self.verticalLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)

        self.verticalLayout.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.edt_personemail = QLineEdit(self.verticalLayoutWidget)
        self.edt_personemail.setObjectName(u"edt_personemail")
        self.edt_personemail.setInputMethodHints(Qt.ImhEmailCharactersOnly)

        self.horizontalLayout.addWidget(self.edt_personemail)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_6 = QLabel(self.verticalLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font)

        self.verticalLayout.addWidget(self.label_6)

        self.edt_emailcontent = QTextEdit(self.verticalLayoutWidget)
        self.edt_emailcontent.setObjectName(u"edt_emailcontent")

        self.verticalLayout.addWidget(self.edt_emailcontent)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Chia se hoa", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"From:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Email: ", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Password:", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"To:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Email:", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"Content:", None))
    # retranslateUi

