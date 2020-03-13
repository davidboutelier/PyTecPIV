import os
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

Ui_DialogConf, QDialog = loadUiType(os.path.join('..', 'gui', 'dialog_conf.ui'))

class dialog_conf(QDialog, Ui_DialogConf):
    """The class's docstring"""

    def __init__(self, parent=None):
        super(dialog_conf, self).__init__(parent)
        self.setupUi(self)

