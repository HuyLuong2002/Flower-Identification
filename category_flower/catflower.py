# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../database')
from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox, QFileDialog
from PySide6.QtGui import QStandardItem, QStandardItemModel, QPixmap
from PySide6.QtCore import Qt
from ui_catflower import Ui_Form
from database.database import Database
#pyside6-uic catflower.ui -o ui_catflower.py

id = -1
class CatFlowerDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        data = getData(self)

        # Tạo model
        model = QStandardItemModel(len(data), 3)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Image')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
            model.setItem(row, 2, QStandardItem(str(item['anh'])))

        # Chỉnh sửa cho table
        # Thiết lập chế độ chỉnh sửa cột cho cả bảng
        header = self.ui.tbl_category.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.Interactive)

        # Thiết lập độ rộng cho cột đầu tiên là 100 pixel
        header.resizeSection(0, 100)

        # Co giãn cột cuối cùng để điền vào khoảng trống của QHeaderView
        header.setStretchLastSection(True)

        # Thiết lập độ rộng của QTableView bằng độ rộng của QHeaderView
        self.ui.tbl_category.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tbl_category.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.ui.tbl_category.clicked.connect(self.HandleCellClick)
        self.ui.btn_add_catflower.clicked.connect(self.AddCatFlower)
        self.ui.btn_update_catflower.clicked.connect(self.UpdateCatFlower)
        self.ui.btn_delete_catflower.clicked.connect(self.DeleteCatFlower)
        self.ui.btn_uploadImage.clicked.connect(self.UploadImage)
        self.ui.tbl_category.setModel(model)

    def HandleCellClick(self, index):
        # Lấy dòng được chọn
        row = index.row()
        global id
        # Lấy các giá trị của ô trong dòng được chọn
        model_table = self.ui.tbl_category.model()
        id = model_table.data(model_table.index(row, 0))
        name = model_table.data(model_table.index(row, 1))
        image = model_table.data(model_table.index(row, 2))
        # Tạo QPixmap từ đường dẫn tệp
        pixmap = QPixmap(image)

        self.ui.edt_flower_name.setText(name)
        self.ui.edt_flower_image.setText(image)
        self.ui.image_cat.setPixmap(pixmap)
        # Co giãn hình ảnh cho vừa với QLabel
        self.ui.image_cat.setScaledContents(True)

    def UploadImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        file_name = QFileDialog.getOpenFileName(self,"Choose Image", "","Image Files (*.png *.jpg *.jpeg *.bmp)", options=options)
        self.ui.edt_flower_image.setText(file_name[0])

    def AddCatFlower(self):
        category_name = self.ui.edt_flower_name.text()
        category_image = self.ui.edt_flower_image.text()
        result = addData(category_name, category_image)

        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 3)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Image')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
            model.setItem(row, 2, QStandardItem(str(item['anh'])))
        self.ui.tbl_category.setModel(model)

        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        # Thiết lập kích thước cho dialog
        dlg.resize(300, 300)  # Kích thước là 300 x 300 pixel
        dlg.exec()

    def UpdateCatFlower(self):
        category_name = self.ui.edt_flower_name.text()
        category_image = self.ui.edt_flower_image.text()
        result = updateData(category_name, category_image, id)
        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 3)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Image')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
            model.setItem(row, 2, QStandardItem(str(item['anh'])))
        self.ui.tbl_category.setModel(model)
        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        # Thiết lập kích thước cho dialog
        dlg.resize(300, 300)  # Kích thước là 300 x 300 pixel
        dlg.exec()

    def DeleteCatFlower(self):
        result = deleteData(id)
        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 3)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        model.setHeaderData(2, Qt.Horizontal, 'Image')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
            model.setItem(row, 2, QStandardItem(str(item['anh'])))
        self.ui.tbl_category.setModel(model)
        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        # Thiết lập kích thước cho dialog
        dlg.resize(300, 300)  # Kích thước là 300 x 300 pixel
        dlg.exec()

def getData(self):
    #kết nối với database
    db = Database()
    connection = db.getConnection()
    # Khởi tạo list chứa dữ liệu
    data = []

    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "SELECT * FROM LoaiHoa"
            cursor.execute(sql)

            # Lấy tất cả các bản ghi
            result = cursor.fetchall()


            # In ra màn hình
            for row in result:
                data.append(row)
            return data
    finally:
        # Đóng kết nối
        db.closeConnection(connection)

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

def updateData(name, image, id):
    #kết nối với database
    db = Database()
    connection = db.getConnection()
    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "UPDATE LoaiHoa SET ten=%s, anh=%s WHERE id=%s"
            tuple = (name, image, id)
            cursor.execute(sql, tuple)
            # sử dụng lệnh commit() khi chúng ta thực hiện thay đổi database
            connection.commit()

            return "Update data successfully"

    finally:
        # Đóng kết nối
        db.closeConnection(connection)

def deleteData(id):
    #kết nối với database
    db = Database()
    connection = db.getConnection()
    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "DELETE FROM LoaiHoa WHERE id=%s"
            tuple = (id)
            cursor.execute(sql, tuple)
            # sử dụng lệnh commit() khi chúng ta thực hiện thay đổi database
            connection.commit()

            return "Delete data successfully"

    finally:
        # Đóng kết nối
        db.closeConnection(connection)
