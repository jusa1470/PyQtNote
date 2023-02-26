# main.py

"""Task Note is a task making app built with PyQT"""

import sys
from PyQt6 import QtWidgets
from qtPackage import Window

def main():
    app = QtWidgets.QApplication([])
    window = Window.Window()
    window.show()

    while app.exec(): continue
    sys.exit()

if __name__ == "__main__":
    main()