
from PySide6.QtWidgets import QDialog, QHeaderView, QAbstractItemView, QMessageBox, QLineEdit
from PySide6.QtCore import Qt, QBuffer, QByteArray, QIODevice
from ui_shareflower import Ui_Dialog
import smtplib
from email.message import EmailMessage
# pyside6-uic shareflower.ui -o ui_shareflower.py
class ShareFlowerDialog(QDialog):
    def __init__(self, parent=None, pixmap=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pixmap = pixmap
        self.ui.edt_mypassword.setEchoMode(QLineEdit.Password)

        # Kết nối sự kiện clicked() của nút "OK" với hàm xử lý sự kiện on_ok_clicked()
        self.ui.buttonBox.accepted.connect(self.on_ok_clicked)

        # Kết nối sự kiện clicked() của nút "Cancel" với hàm xử lý sự kiện on_cancel_clicked()
        self.ui.buttonBox.rejected.connect(self.on_cancel_clicked)

    def on_ok_clicked(self):
        myemail = self.ui.edt_myemail.text()
        mypassword = self.ui.edt_mypassword.text()

        person_email = self.ui.edt_personemail.text()
        email_content = self.ui.edt_emailcontent.toPlainText()

        message = EmailMessage()
        message['Subject'] = "Share identified image to you"
        message['From'] = myemail
        message['To'] = person_email
        message.set_content(email_content)
        # Convert pixmap to bytes

        byte_array = QByteArray()
        buffer = QBuffer(byte_array)
        buffer.open(QIODevice.WriteOnly)
        self.ui.pixmap.save(buffer, "PNG")
        image_data = bytes(byte_array)


        # Create attachment with the image data
        message.add_related(image_data, 'image', 'png', cid='flower_image')

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com',465) as mail:
                mail.login(myemail, mypassword)
                mail.send_message(message)
            QMessageBox.information(self, "Success", "Email sent successfully!")
        except Exception as e:
            QMessageBox.critical(self, "Error", "Failed to send email: " + str(e))


    def on_cancel_clicked(self):
        self.reject()



