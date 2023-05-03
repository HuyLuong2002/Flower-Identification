# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'catflower.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QLabel,
    QLayout, QLineEdit, QPushButton, QSizePolicy,
    QTableView, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 600)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(110, 440, 272, 30))
        self.horizontalLayout = QHBoxLayout(self.verticalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(10, 2, 10, 2)
        self.btn_add_catflower = QPushButton(self.verticalLayoutWidget)
        self.btn_add_catflower.setObjectName(u"btn_add_catflower")
        self.btn_add_catflower.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.horizontalLayout.addWidget(self.btn_add_catflower)

        self.btn_update_catflower = QPushButton(self.verticalLayoutWidget)
        self.btn_update_catflower.setObjectName(u"btn_update_catflower")
        self.btn_update_catflower.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.horizontalLayout.addWidget(self.btn_update_catflower)

        self.btn_delete_catflower = QPushButton(self.verticalLayoutWidget)
        self.btn_delete_catflower.setObjectName(u"btn_delete_catflower")
        self.btn_delete_catflower.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.horizontalLayout.addWidget(self.btn_delete_catflower)

        self.edt_flower_name = QLineEdit(Form)
        self.edt_flower_name.setObjectName(u"edt_flower_name")
        self.edt_flower_name.setGeometry(QRect(190, 310, 211, 31))
        self.edt_flower_name.setInputMethodHints(Qt.ImhNoPredictiveText|Qt.ImhPreferLowercase|Qt.ImhPreferNumbers|Qt.ImhPreferUppercase)
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(280, 35, 251, 31))
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 320, 67, 17))
        font1 = QFont()
        font1.setPointSize(13)
        self.label_2.setFont(font1)
        self.tbl_category = QTableView(Form)
        self.tbl_category.setObjectName(u"tbl_category")
        self.tbl_category.setGeometry(QRect(110, 90, 601, 201))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(110, 370, 67, 17))
        self.label_3.setFont(font1)
        self.edt_flower_image = QLineEdit(Form)
        self.edt_flower_image.setObjectName(u"edt_flower_image")
        self.edt_flower_image.setGeometry(QRect(190, 360, 211, 31))
        self.edt_flower_image.setInputMethodHints(Qt.ImhNoPredictiveText|Qt.ImhPreferLowercase|Qt.ImhPreferNumbers|Qt.ImhPreferUppercase)
        self.horizontalLayoutWidget = QWidget(Form)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(460, 310, 251, 191))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.image_cat = QLabel(self.horizontalLayoutWidget)
        self.image_cat.setObjectName(u"image_cat")
        self.image_cat.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.image_cat)

        self.btn_uploadImage = QPushButton(Form)
        self.btn_uploadImage.setObjectName(u"btn_uploadImage")
        self.btn_uploadImage.setGeometry(QRect(410, 360, 31, 31))
        self.btn_uploadImage.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Qu\u1ea3n l\u00fd danh s\u00e1ch c\u00e1c lo\u00e0i hoa", None))
        self.btn_add_catflower.setText(QCoreApplication.translate("Form", u"Th\u00eam", None))
        self.btn_update_catflower.setText(QCoreApplication.translate("Form", u"S\u1eeda", None))
        self.btn_delete_catflower.setText(QCoreApplication.translate("Form", u"X\u00f3a", None))
        self.label.setText(QCoreApplication.translate("Form", u"Danh s\u00e1ch c\u00e1c lo\u00e0i hoa", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"T\u00ean hoa:", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u1ea2nh lo\u00e0i:", None))
        self.image_cat.setText(QCoreApplication.translate("Form", u"\u1ea2nh lo\u00e0i", None))
        self.btn_uploadImage.setText(QCoreApplication.translate("Form", u"...", None))
    # retranslateUi

