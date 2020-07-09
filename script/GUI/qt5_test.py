from PyQt5 import QtWidgets, uic

def Convert():
    dlg.lineEdit_output.setText(str(float(dlg.lineEdit_input.text())*20))

app = QtWidgets.QApplication([])
dlg = uic.loadUi("/home/kai/Scripts/test.ui")

dlg.lineEdit_input.setFocus()
dlg.lineEdit_input.setPlaceholderText("float")
dlg.pushButton.clicked.connect(Convert)

dlg.lineEdit_input.returnPressed.connect(Convert)
dlg.lineEdit_output.setReadOnly(True)
dlg.show()
app.exec_()
