from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox, QLineEdit
from PySide6.QtCore import Qt, QBuffer, QByteArray, QIODevice
from PySide6.QtGui import QPixmap
import tempfile
import json
import requests
import base64
from ui_detailflower import Ui_Dialog

# pyside6-uic detailflower.ui -o ui_detailflower.py
class DetailFlowerDialog(QDialog):
    def __init__(self, parent=None, imagePath=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        pixmap = QPixmap(imagePath)
        self.ui.lb_detailflowerimage.setPixmap(pixmap)
        self.ui.lb_detailflowerimage.setScaledContents(True)

        # Gửi request đến API của Plant.id với file ảnh

        # encode images to base64
        with open(imagePath, "rb") as file:
            images = [base64.b64encode(file.read()).decode("ascii")]
        response = requests.post(
            "https://api.plant.id/v2/identify",
            json={
                "images": images,
                "modifiers": ["similar_images"],
                "plant_details": ["common_names", "url"],
            },
            headers={
                "Content-Type": "application/json",
                "Api-Key": "43c912s0aZ9f80lORKIEK3tHCIVk5yuq6QkLoUfEvysKeyiaeu",
            }).json()

        for suggestion in response["suggestions"]:
           self.ui.show_plant_name.setText(suggestion["plant_name"])   # Taraxacum officinale
           for common in suggestion["plant_details"]["common_names"]:
               self.ui.show_common_name.setText(self.ui.show_common_name.toPlainText() + " " + common)    # ["Dandelion"]
           self.ui.show_url.setText(suggestion["plant_details"]["url"])    # https://en.wikipedia.org/wiki/Taraxacum_officinale
           break

    def on_cancel_clicked(self):
        self.reject()

