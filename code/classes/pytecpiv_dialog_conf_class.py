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

        # call backs for dialog here
        self.set_projects_button.clicked.connect(self.set_projects_path)
        self.set_sources_button.clicked.connect(self.set_sources_path)

    def set_projects_path(self):
        """

        :return:
        """
        import os
        import json
        from PyQt5.QtWidgets import QFileDialog
        from pytecpiv_conf import pytecpiv_get_pref

        # get the data from the conf file if exist
        file_exist, projects_path, sources_path = pytecpiv_get_pref()
        print(file_exist)

        current_directory = os.getcwd()
        print(current_directory)
        new_projects_path = QFileDialog.getExistingDirectory(self, 'Open directory', current_directory)

        if file_exist == 'yes':
            #  write in the file


        else:
            #  create the conf file and write in



        return new_projects_path

    def set_sources_path(self):
        """

        :return:
        """
        import os
        from PyQt5.QtWidgets import QFileDialog

        current_directory = os.getcwd()
        sources_path = QFileDialog.getExistingDirectory(self, 'Open directory', current_directory)
        return sources_path