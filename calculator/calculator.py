from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from calc import Ui_Form
import sys

class Calculator(QtWidgets.QMainWindow, Ui_Form):
    def __init__(self):
        super(Calculator, self).__init__()
        self.uif = Ui_Form()
        self.uif.setupUi(self)
        self.uif.calcLCD.setAlignment(Qt.AlignRight)
        self.uif.button_0.pressed.connect(self.btn_zero)
        self.uif.button_00.pressed.connect(self.btn_dzero)
        self.uif.button_1.pressed.connect(self.btn_one)
        self.uif.button_2.pressed.connect(self.btn_two)
        self.uif.button_3.pressed.connect(self.btn_three)
        self.uif.button_4.pressed.connect(self.btn_four)
        self.uif.button_5.pressed.connect(self.btn_five)
        self.uif.button_6.pressed.connect(self.btn_six)
        self.uif.button_7.pressed.connect(self.btn_seven)
        self.uif.button_8.pressed.connect(self.btn_eight)
        self.uif.button_9.pressed.connect(self.btn_nine)
        self.uif.button_add.pressed.connect(self.btn_add)
        self.uif.button_minus.pressed.connect(self.btn_minus)
        self.uif.button_mul.pressed.connect(self.btn_mul)
        self.uif.button_div.pressed.connect(self.btn_div)
        self.uif.button_dot.pressed.connect(self.btn_dot)
        self.uif.button_c.pressed.connect(self.btn_cancel)
        self.uif.button_open.pressed.connect(self.btn_open)
        self.uif.button_10.pressed.connect(self.btn_close)
        self.uif.button_11.pressed.connect(self.btn_equal)

    def btn_zero(self):
        str = self.uif.calcLCD.text()
        str += '0'
        self.uif.calcLCD.setText(str)

    def btn_dzero(self):
        str = self.uif.calcLCD.text()
        str += '00'
        self.uif.calcLCD.setText(str)
    def btn_one(self):
        str = self.uif.calcLCD.text()
        str += '1'
        self.uif.calcLCD.setText(str)
    def btn_two(self):
        str = self.uif.calcLCD.text()
        str += '2'
        self.uif.calcLCD.setText(str)
    def btn_three(self):
        str = self.uif.calcLCD.text()
        str += '3'
        self.uif.calcLCD.setText(str)
    def btn_four(self):
        str = self.uif.calcLCD.text()
        str += '4'
        self.uif.calcLCD.setText(str)
    def btn_five(self):
        str = self.uif.calcLCD.text()
        str += '5'
        self.uif.calcLCD.setText(str)
    def btn_six(self):
        str = self.uif.calcLCD.text()
        str += '6'
        self.uif.calcLCD.setText(str)
    def btn_seven(self):
        str = self.uif.calcLCD.text()
        str += '7'
        self.uif.calcLCD.setText(str)
    def btn_eight(self):
        str = self.uif.calcLCD.text()
        str += '8'
        self.uif.calcLCD.setText(str)
    def btn_nine(self):
        str = self.uif.calcLCD.text()
        str += '9'
        self.uif.calcLCD.setText(str)
    def btn_dot(self):
        str = self.uif.calcLCD.text()
        str += '.'
        self.uif.calcLCD.setText(str)
    def btn_add(self):
        str = self.uif.calcLCD.text()
        str += '+'
        self.uif.calcLCD.setText(str)
    def btn_minus(self):
        str = self.uif.calcLCD.text()
        str += '-'
        self.uif.calcLCD.setText(str)
    def btn_mul(self):
        str = self.uif.calcLCD.text()
        str += '*'
        self.uif.calcLCD.setText(str)
    def btn_div(self):
        str = self.uif.calcLCD.text()
        str += '/'
        self.uif.calcLCD.setText(str)
    def btn_open(self):
        str = self.uif.calcLCD.text()
        str += '('
        self.uif.calcLCD.setText(str)
    def btn_close(self):
        str = self.uif.calcLCD.text()
        str += ')'
        self.uif.calcLCD.setText(str)
    def btn_cancel(self):
        str = ''
        self.uif.calcLCD.setText(str)
    def btn_equal(self):
        try:
            expr = self.uif.calcLCD.text()
            result = str(eval(expr, {}, {}))
        except Exception:
            result = 'Error'
        self.uif.calcLCD.setText(result)
app = QtWidgets.QApplication(sys.argv)
calc = Calculator()
calc.show()
app.exec_()