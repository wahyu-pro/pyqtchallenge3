from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QMainWindow):
    def __init__(self):
        super(MyApp, self).__init__()
        self.mainUI()
        self.setLayout()
        self.setCentralWidget(self.setWidget)

    def mainUI(self):
        self.list = QListWidget()
        self.btnAdd = QPushButton("Add")
        self.btnAdd.clicked.connect(self.setInputDialog)
        self.buttonRemove = QPushButton("Remove")
        self.buttonRemove.clicked.connect(self.removeItems)
        self.btnClear = QPushButton("Clear")
        self.btnClear.clicked.connect(self.clear)
        self.btnUpdate = QPushButton("Update")
        self.btnUpdate.clicked.connect(self.update)
        self.btnDuplicate = QPushButton("Duplicate")
        self.btnDuplicate.clicked.connect(self.duplicate)

        # Slider
        self.slider = QSlider(Qt.Horizontal)
        self.slider.valueChanged.connect(self.valueSlider)

        # progressbar
        self.progressBar = QProgressBar()

    def setLayout(self):
        self.layoutList = QVBoxLayout()
        self.layoutList.addWidget(self.list)
        self.layoutList.addWidget(self.btnAdd)
        self.layoutList.addWidget(self.buttonRemove)
        self.layoutList.addWidget(self.btnClear)
        self.layoutList.addWidget(self.btnUpdate)
        self.layoutList.addWidget(self.btnDuplicate)
        self.layoutList.addWidget(self.slider)
        self.layoutList.addWidget(self.progressBar)

        self.setWidget = QWidget()
        self.setWidget.setLayout(self.layoutList)

    def setInputDialog(self):
        self.inputDialog, ok = QInputDialog.getText(self, "Add item", "Add list item")
        if self.inputDialog == "" and ok == True:
            QMessageBox.warning(self, "Warning", "Please input data !")
        elif ok == False:
            pass
        elif self.inputDialog.isalnum() and ok == True:
            item = QListWidgetItem(self.inputDialog, self.list)
            self.list.addItem(item)

        self.progressBar.setValue(self.list.count())

    def removeItems(self):
        listItems = self.list.selectedItems()
        if not listItems:
            pass
        for item in listItems:
            self.list.takeItem(self.list.row(item))
        self.progressBar.setValue(self.list.count())

    def clear(self):
        self.list.clear()
        self.progressBar.setValue(self.list.count())

    def update(self):
        listItems = self.list.selectedItems()
        listdata = []
        for i in listItems:
            listdata.append(i.text())
        self.inputUpdate, ok = QInputDialog.getText(self, "Edit", "Edit list item", text=listdata[0])
        if self.inputUpdate != "" and ok == True:
            for item in listItems:
                self.list.item(self.list.row(item)).setText(self.inputUpdate)

    def valueSlider(self):
        value = self.slider.value()
        return value

    def duplicate(self):
        value = self.valueSlider()
        listItems = self.list.selectedItems()
        listdata = []
        for i in listItems:
            listdata.append(i.text())

        for x in range(value):
            item = QListWidgetItem(listdata[0], self.list)
            self.list.addItem(item)
            self.progressBar.setValue(self.list.count())


if __name__ == "__main__":
    app = QApplication([])
    window = MyApp()
    window.show()
    app.exec()