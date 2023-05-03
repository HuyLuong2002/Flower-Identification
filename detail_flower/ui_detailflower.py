# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'detailflower.ui'
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
    QHBoxLayout, QLabel, QSizePolicy, QTextEdit,
    QVBoxLayout, QWidget)

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
        self.horizontalLayoutWidget = QWidget(Dialog)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(330, 30, 271, 221))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.lb_detailflowerimage = QLabel(self.horizontalLayoutWidget)
        self.lb_detailflowerimage.setObjectName(u"lb_detailflowerimage")
        self.lb_detailflowerimage.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.lb_detailflowerimage)

        self.horizontalLayoutWidget_2 = QWidget(Dialog)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(10, 30, 291, 421))
        self.verticalLayout = QVBoxLayout(self.horizontalLayoutWidget_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_4 = QLabel(self.horizontalLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_4.addWidget(self.label_4)

        self.show_url = QTextEdit(self.horizontalLayoutWidget_2)
        self.show_url.setObjectName(u"show_url")
        self.show_url.setEnabled(False)
        self.show_url.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.show_url)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.horizontalLayoutWidget_2)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.show_plant_name = QTextEdit(self.horizontalLayoutWidget_2)
        self.show_plant_name.setObjectName(u"show_plant_name")
        self.show_plant_name.setEnabled(False)
        self.show_plant_name.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.show_plant_name)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_2 = QLabel(self.horizontalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setLineWidth(5)

        self.horizontalLayout_3.addWidget(self.label_2)

        self.show_common_name = QTextEdit(self.horizontalLayoutWidget_2)
        self.show_common_name.setObjectName(u"show_common_name")
        self.show_common_name.setEnabled(False)
        self.show_common_name.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.show_common_name)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Th\u00f4ng tin hoa", None))
        self.lb_detailflowerimage.setText(QCoreApplication.translate("Dialog", u"Image Label", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Url:", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Plant name:", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Common names", None))
    # retranslateUi

