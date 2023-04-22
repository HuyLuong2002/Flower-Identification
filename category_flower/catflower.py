# This Python file uses the following encoding: utf-8
import sys
sys.path.append('../database')
from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtCore import Qt
from ui_catflowerform import Ui_Form
from database.database import Database

id = -1
class CatFlowerDialog(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        data = getData(self)

        # Tạo model
        model = QStandardItemModel(len(data), 2)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))

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
        self.ui.tbl_category.setModel(model)

    def HandleCellClick(self, index):
        # Lấy dòng được chọn
        row = index.row()
        global id
        # Lấy các giá trị của ô trong dòng được chọn
        model_table = self.ui.tbl_category.model()
        id = model_table.data(model_table.index(row, 0))
        name = model_table.data(model_table.index(row, 1))
        self.ui.edt_flower_name.setText(name)

    def AddCatFlower(self):
        category_name = self.ui.edt_flower_name.text()
        result = addData(category_name)
        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 2)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
        self.ui.tbl_category.setModel(model)

        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        dlg.exec()

    def UpdateCatFlower(self):
        category_name = self.ui.edt_flower_name.text()
        result = updateData(category_name, id)
        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 2)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
        self.ui.tbl_category.setModel(model)
        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
        dlg.exec()

    def DeleteCatFlower(self):
        result = deleteData(id)
        data = getData(self)
        # Tạo model
        model = QStandardItemModel(len(data), 2)
        model.setHeaderData(0, Qt.Horizontal, 'Id')
        model.setHeaderData(1, Qt.Horizontal, 'Name')
        for row, item in enumerate(data):
            model.setItem(row, 0, QStandardItem(str(item['id'])))
            model.setItem(row, 1, QStandardItem(str(item['ten'])))
        self.ui.tbl_category.setModel(model)
        #create dialog message to user
        dlg = QMessageBox(self)
        dlg.setWindowTitle("Thông báo")
        dlg.setText(result)
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

def addData(name):
    #kết nối với database
    db = Database()
    connection = db.getConnection()

    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "INSERT INTO LoaiHoa(ten) VALUES(%s)"
            tuple = (name)
            cursor.execute(sql, tuple)
            connection.commit()

            return "Insert successfully"

    finally:
        # Đóng kết nối
        db.closeConnection(connection)

def updateData(name, id):
    #kết nối với database
    db = Database()
    connection = db.getConnection()
    try:
        with connection.cursor() as cursor:
            # Thực hiện truy vấn SQL
            sql = "UPDATE LoaiHoa SET ten=%s WHERE id=%s"
            tuple = (name, id)
            cursor.execute(sql, tuple)
            # sử dụng lệnh commit() khi chúng ta thực hiện thay đổi database
            connection.commit()

            return "Update successfully"

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

            return "Delete successfully"

    finally:
        # Đóng kết nối
        db.closeConnection(connection)
