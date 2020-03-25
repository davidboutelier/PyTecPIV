from PyQt5.uic import loadUiType
import os
from pytecpiv_var import *

Ui_DialogImg, QDialog = loadUiType(os.path.join('..', 'gui', 'dialog_img.ui'))


class dialog_img(QDialog, Ui_DialogImg):
    """

    """
    def __init__(self, parent=None):
        from pytecpiv_var import current_dataset

        super(dialog_img, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.set_img_prop)


    def set_img_prop(self):
        """

        :return:
        """
        from pytecpiv_var import current_dataset
        from classes.pytecpiv_class_main import Main
        from pytecpiv_util import create_fig
        from matplotlib.figure import Figure

        main = Main()

        img_min = self.doubleSpinBox_min.value()
        img_max = self.doubleSpinBox_max.value()
        img_colormap = self.comboBox_colormap.currentText()

        current_dataset[6] = img_min
        current_dataset[7] = img_max
        current_dataset[8] = img_colormap

        main.rmmpl()
        fig1 = Figure()
        create_fig(fig1, current_dataset)
        main.addmpl(fig1)




