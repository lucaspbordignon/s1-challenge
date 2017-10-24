from gui.main_window import Ui_main_window
from PyQt5.QtWidgets import QMainWindow


class Interface(QMainWindow, Ui_main_window):
    """
        Handles all the events related to the interface, connecting
        the events generated by the user with their proper handlers. Part of 
        the view compontent of a MVC architecture.
    """
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
