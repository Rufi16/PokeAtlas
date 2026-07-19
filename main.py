import sys
from PySide6.QtWidgets import QApplication 
from MainWindow import mainWindow
from PySide6.QtCore import Qt
app = QApplication(sys.argv)

window = mainWindow()
window.show()

app.exec()