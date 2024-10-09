from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit

def handleCalc():
    info = textedit.toPlainText()

    salary_above_20k = ''
    salary_bellow_20k = ''

    for line in info.splitlines(): # 去除换行符
        if not line.strip(): # 去除首尾的空格
            continue
        parts = line.split(' ') # 以空格为分隔符分割str
        parts


app = QApplication([])

window = QMainWindow()
window.resize(500, 400)
window.move(300,310)
window.setWindowTitle('薪资统计')

textedit = QPlainTextEdit(window)
textedit.setPlaceholderText('请输入薪资表')
textedit.move(10,25)
textedit.resize(300,350)

button = QPushButton('统计', window)
button.move(380, 80)
button.clicked.connect(handleCalc)

window.show()
app.exec_()