from PyQt5 import QtWidgets
from bmicalc import Ui_Form
import sys

class BMI_Calculator(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(BMI_Calculator, self).__init__()
        self.uif = Ui_Form()
        self.uif.setupUi(self)
        self.uif.bmiCalcButton.pressed.connect(self.bmiCalculate)
        self.uif.weightEdit.textChanged.connect(self.weightChange)
        self.uif.heightEdit.textChanged.connect(self.heightChange)

    def weightChange(self):
        try:
            weight = float(self.uif.weightEdit.text())
        except Exception as err:
            QtWidgets.QMessageBox.about(self, 'Error', 'Invalid Weight')

    def heightChange(self):
        try:
            height = float(self.uif.heightEdit.text())
        except Exception as err:
            QtWidgets.QMessageBox.about(self, 'Error', 'Invalid Height')

    def bmiCalculate(self):
        try:
            weight = float(self.uif.weightEdit.text())
            height = float(self.uif.heightEdit.text()) / 100 # 100 CM -> 1 Meter
            bmi = weight / (height * height)
            self.uif.bmiButton.setText(str(round(bmi, 2)))
            if bmi < 15:
                self.uif.bmiButton.setStyleSheet('background: Yellow')
            elif bmi < 20:
                self.uif.bmiButton.setStyleSheet('background: Orange')
            elif bmi < 25:
                self.uif.bmiButton.setStyleSheet('background: Green')
            elif bmi < 30:
                self.uif.bmiButton.setStyleSheet('background: Pink')
            else:
                self.uif.bmiButton.setStyleSheet('background: Red')
            #print('Entered Weight = {} Height = {}'.format(weight, height))
        except Exception as err:
            print('Exception {}'.format(err))


app = QtWidgets.QApplication(sys.argv)
bmic = BMI_Calculator()
bmic.show()
app.exec_()