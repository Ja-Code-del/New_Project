import sys
from PyQt6.QtWidgets import QApplication
from gui import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = PDFApp()
    window.show()
    sys.exit(app.exec())
