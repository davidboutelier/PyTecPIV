from PyQt5.uic import loadUiType
import os

Ui_DialogImg, QDialog = loadUiType(os.path.join('..', 'gui', 'dialog_img.ui'))

global current_dataset, fig1

class dialog_img(QDialog, Ui_DialogImg):
    """The class's docstring"""
    global current_dataset, fig1


    def __init__(self, parent=None):
        super(dialog_img, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.clicked.connect(self.set_img_prop)

    def set_img_prop(self):
        from matplotlib.figure import Figure
        from pytecpiv_util import create_fig

        global current_dataset, fig1

        img_min = self.doubleSpinBox_min.value()
        img_max = self.doubleSpinBox_max.value()
        img_colormap = self.comboBox_colormap.currentText()

        current_dataset[6] = img_min
        current_dataset[7] = img_max
        current_dataset[8] = img_colormap

        self.rmmpl()
        fig1 = Figure()
        create_fig(fig1, current_dataset)
        self.addmpl(fig1)

