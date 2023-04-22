# This Python file uses the following encoding: utf-8
import sys
sys.path.append('./category_flower')
sys.path.append('./share_flower')
import cv2
import numpy as np
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QTableView
from tensorflow.keras.models import load_model
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QUrl, QLibraryInfo
from PySide6.QtCore import QByteArray
from PySide6.QtCore import QBuffer
from PySide6.QtNetwork import QSslSocket
from PySide6.QtNetwork import QNetworkAccessManager, QNetworkRequest, QNetworkReply
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from category_flower.catflower import CatFlowerDialog
from share_flower.shareflower import ShareFlowerDialog

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = load_model('flower_my_model.h5')
        self.ui.browse_button.clicked.connect(self.BrowseImage)
        self.ui.btn_list_flower.clicked.connect(self.OpenListCatFlower)
        self.ui.btn_share.clicked.connect(self.ShareImageToEmail)

    def BrowseImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self,"Choose Image", "","Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        if file_name:
            image = cv2.imread(str(file_name[0]))
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = cv2.resize(image, (224, 224))
            image = np.array(image)/255.0
            image = np.expand_dims(image, axis=0)

            prediction = self.model.predict(image)[0][:5]
            flower_names = ["Daisy", "Dandelion", "Rose", "Sunflower", "Tulip"]
            flower_name = flower_names[np.argmax(prediction)]

            pixmap = QtGui.QPixmap(file_name[0]).scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            if flower_name == "Daisy":
                model_image = QtGui.QPixmap("./image/daisy.jpg").scaled(500, 500)
                self.ui.model_label.setPixmap(model_image)
            elif flower_name == "Dandelion":
                model_image = QtGui.QPixmap("./image/dandelion.jpg").scaled(500, 500)
                self.ui.model_label.setPixmap(model_image)
            elif flower_name == "Rose":
                model_image = QtGui.QPixmap("./image/rose.jpg").scaled(500, 500)
                self.ui.model_label.setPixmap(model_image)
            elif flower_name == "Sunflower":
                model_image = QtGui.QPixmap("./image/sunflower.jpg").scaled(500, 500)
                self.ui.model_label.setPixmap(model_image)
            elif flower_name == "Tulip":
                model_image = QtGui.QPixmap("./image/tulip.jpg").scaled(500, 500)
                self.ui.model_label.setPixmap(model_image)

            self.ui.img_label.setPixmap(pixmap)
            self.ui.predict_label.setText(flower_name)



    def OpenListCatFlower(self):
        catflower_dialog = CatFlowerDialog(self)
        catflower_dialog.exec()

    def ShareImageToEmail(self):
        shareflower_dialog = ShareFlowerDialog(self, self.ui.img_label.pixmap())
        shareflower_dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
