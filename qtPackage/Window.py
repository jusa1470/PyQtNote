from PyQt6 import QtWidgets, QtCore, QtGui

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800

class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Task Note!')
        self.setFixedSize(WINDOW_WIDTH, WINDOW_HEIGHT)
        self.generalLayout = QtWidgets.QGridLayout()
        self._createTitle()
        self._createNewButton()
        self._createNotes()
        centralWidget = QtWidgets.QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)

    def _createTitle(self):
        label = QtWidgets.QLabel('Notes', self)
        label.setFont(QtGui.QFont('Sanserif', 40))
        label.adjustSize()
        label.setStyleSheet('QLabel {color: pink;}')
        self.generalLayout.addWidget(label)

    def _createNewButton(self):
        newButton = QtWidgets.QPushButton('Add New Note', self)
        newButton.setFont(QtGui.QFont('Sanserif', 40))
        newButton.adjustSize()
        newButton.setStyleSheet('QPushButton {background-color: limegreen; color: black;}')
        self.generalLayout.addWidget(newButton)

    def _createNotes(self):
        notes = ['julias note', 'denver made a note', 'hello']
        noteList = QtWidgets.QListWidget()
        for note in notes:
            # label = QtWidgets.QLabel(note, self)
            noteList.addItem(note)
        self.generalLayout.addWidget(noteList)