import os
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)

# import gui
Ui_MainWindow, QMainWindow = loadUiType(os.path.join('..', 'gui', 'gui.ui'))

class Main(QMainWindow, Ui_MainWindow):
    """The class's docstring"""
    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # define some callback functions here
        from classes.pytecpiv_dialog_conf_class import dialog_conf
        self.actionConfiguration.triggered.connect(self.show_conf_fn)
        self.dialog_conf = dialog_conf(self)

        self.new_project_menu.triggered.connect(self.create_new_project)





    def addmpl(self, fig):
        """The method's docstring"""
        self.canvas = FigureCanvas(fig)
        self.mplvl.addWidget(self.canvas)
        self.canvas.draw()
        self.toolbar = NavigationToolbar(self.canvas, self.mplfig, coordinates=True)
        self.mplvl.addWidget(self.toolbar)

    def rmmpl(self, ):
        """The method's docstring"""
        self.mplvl.removeWidget(self.canvas)
        self.canvas.close()
        self.mplvl.removeWidget(self.toolbar)
        self.toolbar.close()

    def show_conf_fn(self):
        """This function makes visible the dialogue box for the configuration"""
        import os
        from pytecpiv_conf import pytecpiv_get_pref

        current_directory = os.getcwd()
        (file_exist, sources_path, projects_path) = pytecpiv_get_pref()
        self.dialog_conf.code_label.setText(current_directory)
        self.dialog_conf.sources_label.setText(sources_path)
        self.dialog_conf.projects_label.setText(projects_path)
        self.dialog_conf.show()

    def create_new_project(self):
        from PyQt5.QtWidgets import QFileDialog
        from pytecpiv_conf import pytecpiv_get_pref
        from datetime import datetime
        from pytecpiv_util import dprint
        import json

        file_exist, sources_path, projects_path = pytecpiv_get_pref()
        this_project_path = QFileDialog.getExistingDirectory(self, 'Open directory', projects_path)

        drive, path_and_file = os.path.splitdrive(this_project_path)
        path_project, project_name = os.path.split(path_and_file)

        # create new project
        project_create_time = str(datetime.now())
        dprint('creating new project')
        dprint(project_create_time)

        # create new project_metadata file
        t = os.path.isfile('project_metadata.json')

        if t:
            os.remove('project_metadata.json')

        metadata = {'project': []}
        metadata['project'].append({'project_path': this_project_path})
        metadata['project'].append({'path': path_project})
        metadata['project'].append({'project_name': project_name})
        metadata['project'].append({'create_date': project_create_time})

        with open('project_metadata.json', 'w') as outfile:
            json.dump(metadata, outfile)









