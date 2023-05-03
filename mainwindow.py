# This Python file uses the following encoding: utf-8
import sys
sys.path.append('./category_flower')
sys.path.append('./share_flower')
sys.path.append('./detail_flower')
import numpy as np
import cv2
from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
import tensorflow as tf
from PySide6 import QtGui, QtCore
from PIL import Image
from database.database import Database
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow
from category_flower.catflower import CatFlowerDialog
from share_flower.shareflower import ShareFlowerDialog
from detail_flower.detailflower import DetailFlowerDialog
class MainWindow(QMainWindow):
    categoryImage=""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.model = tf.saved_model.load('flower_model')
#        self.model = tf.keras.models.load_model('model-resnet50.h5')
        self.ui.browse_button.clicked.connect(self.BrowseImage)
        self.ui.btn_list_flower.clicked.connect(self.OpenListCatFlower)
        self.ui.btn_share.clicked.connect(self.ShareImageToEmail)
        self.ui.btn_viewdetail.clicked.connect(self.ViewDetailFlower)

    def BrowseImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self,"Choose Image", "","Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        self.categoryImage=file_name[0]
        if file_name:
            image = cv2.imread(file_name[0])
            # Điều chỉnh kích thước hình ảnh
            resized_image = cv2.resize(image, (224, 224))
            image = tf.keras.preprocessing.image.img_to_array(resized_image)
            image /= 225.0
            image = tf.expand_dims(image, axis=0)

            prediction = self.model(image)
#            prediction = self.model.predict(image)

            flower_names = ["pink primrose", "hard-leaved pocket orchid", "canterbury bells",
            "sweet pea", "english marigold", "tiger lily", "moon orchid",
            "bird of paradise", "monkshood", "globe thistle", "snapdragon",
            "colt's foot", "king protea", "spear thistle", "yellow iris",
            "globe-flower", "purple coneflower", "peruvian lily", "balloon flower",
            "giant white arum lily", "fire lily", "pincushion flower", "fritillary",
            "red ginger", "grape hyacinth", "corn poppy", "prince of wales feathers",
            "stemless gentian", "artichoke", "sweet william", "carnation",
            "garden phlox", "love in the mist", "mexican aster", "alpine sea holly",
            "ruby-lipped cattleya", "cape flower", "great masterwort", "siam tulip",
            "lenten rose", "barbeton daisy", "daffodil", "sword lily", "poinsettia",
            "bolero deep blue", "wallflower", "marigold", "buttercup", "oxeye daisy",
            "common dandelion", "petunia", "wild pansy", "primula", "sunflower",
            "pelargonium", "bishop of llandaff", "gaura", "geranium", "orange dahlia",
            "pink-yellow dahlia?", "cautleya spicata", "japanese anemone",
            "black-eyed susan", "silverbush", "californian poppy", "osteospermum",
            "spring crocus", "bearded iris", "windflower", "tree poppy", "gazania",
            "azalea", "water lily", "rose", "thorn apple", "morning glory",
            "passion flower", "lotus", "toad lily", "anthurium", "frangipani",
            "clematis", "hibiscus", "columbine", "desert-rose", "tree mallow",
            "magnolia", "cyclamen", "watercress", "canna lily", "hippeastrum",
            "bee balm", "ball moss", "foxglove", "bougainvillea", "camellia", "mallow",
            "mexican petunia", "bromelia", "blanket flower", "trumpet creeper",
            "blackberry lily"]

            # flower_names = ["Daisy","Dandelion","Rose","Sunflower","Tulip"]

            flower_name = flower_names[np.argmax(prediction)]

            pixmap = QtGui.QPixmap(file_name[0]).scaled(500, 500, QtCore.Qt.KeepAspectRatio)
            model_image = QtGui.QPixmap("./image/" + str(np.argmax(prediction) + 1) + ".jpg")
            self.ui.model_label.setPixmap(model_image)

            self.ui.img_label.setPixmap(pixmap)
            self.ui.predict_label.setText(flower_name)
#            self.AddCatFlower()



    def OpenListCatFlower(self):
        catflower_dialog = CatFlowerDialog(self)
        catflower_dialog.exec()

    def ShareImageToEmail(self):
        shareflower_dialog = ShareFlowerDialog(self, self.ui.img_label.pixmap())
        shareflower_dialog.exec()

    def ViewDetailFlower(self):
        # check image choice
        if self.categoryImage == "":
            #create dialog message to user
            dlg = QMessageBox(self)
            dlg.setWindowTitle("Thông báo")
            dlg.setText("Mời chọn hình ảnh để nhận diện")
            # Thiết lập kích thước cho dialog
            dlg.resize(300, 300)  # Kích thước là 300 x 300 pixel
            dlg.exec()
            return
        viewdetailflower_dialog = DetailFlowerDialog(self, self.categoryImage)
        viewdetailflower_dialog.exec()

    def AddCatFlower(self):
        category_name = self.ui.predict_label.text()
        category_image = self.categoryImage
        result = addData(category_name, category_image)

        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        # Thiết lập kích thước cho dialog
        dlg.resize(300, 300)  # Kích thước là 300 x 300 pixel
        dlg.exec()

def addData(name, image):
    #kết nối với database
    db = Database()
    connection = db.getConnection()

    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "INSERT INTO LoaiHoa(ten,anh) VALUES(%s,%s)"
            tuple = (name,image)
            cursor.execute(sql, tuple)
            connection.commit()
        return "Insert data successfully"

    finally:
        # Đóng kết nối
        db.closeConnection(connection)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
