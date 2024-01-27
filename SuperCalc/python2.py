from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget

app = QApplication([])


# def calculate(x, y, operation):
# if operation == '+':
# print(x + y)
# elif operation == '-':
# print(x - y)
# elif operation == '*':
# print(x * y)
# elif operation == '/':
# if y != 0:
# print(x / y)
# else:
# return "Помилка"
# else:
# return "Помилка"


def calculateplus(label, label_2):
    print(label + label_2)


def calculateminus(label, label_2):
    print(label - label_2)


def calculatepomnozh(label, label_2):
    print(label * label_2)


def calculatepodel(label, label_2):
    if label_2 != 0:
        print(label / label_2)
    else:
        return "Помилка"


window = QWidget()
window.setWindowTitle("Калькулятор")
window.resize(500, 500)
window.move(600, 300)

window.show()
app.exec_()
