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
        file_exist, sources_path, projects_path = pytecpiv_get_pref()
        print(file_exist)

        current_directory = os.getcwd()
        print(current_directory)
        new_projects_path = QFileDialog.getExistingDirectory(self, 'Open directory', current_directory)

        if file_exist == 'yes':
            #  write in the file
            with open('pytecpiv_settings.json') as f:
                pytecpiv_settings = json.load(f)

            pytecpiv_settings['projects'] = []
            pytecpiv_settings['projects'].append({'projects_path': new_projects_path})
            with open('pytecpiv_settings.json', 'w') as outfile:
                json.dump(pytecpiv_settings, outfile)


        else:
            #  create the conf file and write in
            pytecpiv_settings = {'sources': []}
            pytecpiv_settings['sources'].append({'sources_path': ' '})
            pytecpiv_settings['projects'] = []
            pytecpiv_settings['projects'].append({'projects_path': new_projects_path})
            with open('pytecpiv_settings.json', 'w') as outfile:
                json.dump(pytecpiv_settings, outfile)

        self.sources_label.setText(sources_path)
        self.projects_label.setText(projects_path)

    def set_sources_path(self):
        """

        """
        import os
        import json
        from PyQt5.QtWidgets import QFileDialog
        from pytecpiv_conf import pytecpiv_get_pref

        # get the data from the conf file if exist
        file_exist, sources_path, projects_path = pytecpiv_get_pref()

        current_directory = os.getcwd()
        new_sources_path = QFileDialog.getExistingDirectory(self, 'Open directory', current_directory)

        if file_exist == 'yes':
            #  write in the file
            with open('pytecpiv_settings.json') as f:
                pytecpiv_settings = json.load(f)

            pytecpiv_settings['sources'] = []
            pytecpiv_settings['sources'].append({'sources_path': new_sources_path})
            with open('pytecpiv_settings.json', 'w') as outfile:
                json.dump(pytecpiv_settings, outfile)

        else:
            #  create the conf file and write in
            pytecpiv_settings = {'sources': []}
            pytecpiv_settings['sources'].append({'sources_path': new_sources_path})
            pytecpiv_settings['projects'] = []
            pytecpiv_settings['projects'].append({'projects_path': ' '})
            with open('pytecpiv_settings.json', 'w') as outfile:
                json.dump(pytecpiv_settings, outfile)

        self.sources_label.setText(sources_path)
        self.projects_label.setText(projects_path)