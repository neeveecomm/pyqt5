from PyQt5 import QtCore, QtGui, QtWidgets
from dialog import Ui_Dialog
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class myfirstui(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        super(myfirstui,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.buttonBox.accepted.connect(self.pushClick)
        self.ui.buttonBox.rejected.connect(self.close)

    def pushClick(self):
        print ("ok button clicked")

        
    def close(self):
        print("cancel button clicked")
            
app = QtWidgets.QApplication([])
window = myfirstui()
window.show()
app.exec_()
