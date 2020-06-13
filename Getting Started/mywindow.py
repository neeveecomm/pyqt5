from PyQt5 import QtCore, QtGui, QtWidgets
from firstui import Ui_MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import uic

class myfirstui(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.var = 0    
        super(myfirstui,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.setObjectName("TestButton")
        self.ui.pushButton.clicked.connect(self.pushClick)

    def pushClick(self):
        self.var = self.var + 1
        print ("self push click function called")
        self.ui.pushButton.setText("pushButton")
        self.ui.textEdit.setText("test")
        
    def close(self):
        print("push button clicked")
            
app = QtWidgets.QApplication([])
window = myfirstui()
window.show()
app.exec()
