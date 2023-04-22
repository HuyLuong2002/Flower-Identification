import pymysql.cursors
#ket noi database
class Database:
    def getConnection(self):
        # Bạn có thể thay đổi các thông số kết nối.
        connection = pymysql.connect(host='127.0.0.1',
        user='root',
        password='BTult6257@@nc',
        db='flower',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor)
        return connection

    def closeConnection(self, connection):
        # Đóng kết nối.
        connection.close()
