from PySide6.QtWidgets import QApplication
from infra.view.jnlaposta import Ui_MainWindow, QMainWindow

class TelaAposta(QMainWindow):
    def __init__(self):
        super(TelaAposta, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == "__main__":
    app = QApplication([])
    mainWindow = TelaAposta()
    mainWindow.show()
    app.exec()