# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1150, 600)
        MainWindow.setStyleSheet(u"background-color: rgb(246, 245, 244);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(60, 80, 521, 271))
        self.gridLayout_2 = QGridLayout(self.verticalLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.predict_label = QLabel(self.verticalLayoutWidget)
        self.predict_label.setObjectName(u"predict_label")
        self.predict_label.setStyleSheet(u"gridline-color: rgb(61, 56, 70);")
        self.predict_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.predict_label, 1, 0, 1, 1)

        self.img_label = QLabel(self.verticalLayoutWidget)
        self.img_label.setObjectName(u"img_label")
        self.img_label.setStyleSheet(u"")
        self.img_label.setScaledContents(True)
        self.img_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.img_label, 0, 0, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.browse_button = QPushButton(self.verticalLayoutWidget)
        self.browse_button.setObjectName(u"browse_button")
        self.browse_button.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.gridLayout_4.addWidget(self.browse_button, 0, 0, 1, 1)

        self.btn_viewdetail = QPushButton(self.verticalLayoutWidget)
        self.btn_viewdetail.setObjectName(u"btn_viewdetail")
        self.btn_viewdetail.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.gridLayout_4.addWidget(self.btn_viewdetail, 0, 1, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)

        self.gridLayoutWidget = QWidget(self.centralwidget)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(80, 380, 486, 80))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_share = QPushButton(self.gridLayoutWidget)
        self.btn_share.setObjectName(u"btn_share")
        self.btn_share.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.gridLayout.addWidget(self.btn_share, 0, 1, 1, 1)

        self.btn_list_flower = QPushButton(self.gridLayoutWidget)
        self.btn_list_flower.setObjectName(u"btn_list_flower")
        self.btn_list_flower.setStyleSheet(u"background-color: rgb(98, 160, 234);")

        self.gridLayout.addWidget(self.btn_list_flower, 0, 0, 1, 1)

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(600, 50, 521, 271))
        self.gridLayout_3 = QGridLayout(self.verticalLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setHorizontalSpacing(0)
        self.gridLayout_3.setVerticalSpacing(5)
        self.gridLayout_3.setContentsMargins(0, 10, 0, 10)
        self.model_title = QLabel(self.verticalLayoutWidget_2)
        self.model_title.setObjectName(u"model_title")
        font = QFont()
        font.setBold(True)
        self.model_title.setFont(font)
        self.model_title.setAlignment(Qt.AlignHCenter|Qt.AlignTop)

        self.gridLayout_3.addWidget(self.model_title, 0, 0, 1, 1)

        self.model_label = QLabel(self.verticalLayoutWidget_2)
        self.model_label.setObjectName(u"model_label")
        self.model_label.setAutoFillBackground(False)
        self.model_label.setScaledContents(True)
        self.model_label.setAlignment(Qt.AlignCenter)

        self.gridLayout_3.addWidget(self.model_label, 1, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1150, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Ph\u1ea7n m\u1ec1m nh\u1eadn di\u1ec7n hoa", None))
        self.predict_label.setText(QCoreApplication.translate("MainWindow", u"Predict Label", None))
        self.img_label.setText(QCoreApplication.translate("MainWindow", u"Image Label", None))
        self.browse_button.setText(QCoreApplication.translate("MainWindow", u"Upload Image", None))
        self.btn_viewdetail.setText(QCoreApplication.translate("MainWindow", u"Xem chi ti\u1ebft", None))
        self.btn_share.setText(QCoreApplication.translate("MainWindow", u"Chia s\u1ebb", None))
        self.btn_list_flower.setText(QCoreApplication.translate("MainWindow", u"Danh s\u00e1ch c\u00e1c lo\u00e0i hoa", None))
        self.model_title.setText(QCoreApplication.translate("MainWindow", u"\u1ea2nh m\u1eabu", None))
        self.model_label.setText(QCoreApplication.translate("MainWindow", u"Image Label", None))
    # retranslateUi

