"""The module's docstring"""
import os
from PyQt5.uic import loadUiType
from PyQt5.QtWidgets import QFileDialog
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure

# import gui
Ui_MainWindow, QMainWindow = loadUiType(os.path.join('..', 'gui', 'gui.ui'))
Ui_DialogConf, QDialog = loadUiType(os.path.join('..', 'gui', 'dialog_conf.ui'))
Ui_DialogImg, QDialog = loadUiType(os.path.join('..', 'gui', 'dialog_img.ui'))

#  initialise some global variables here
dataset_index = 0
current_dataset = []                    #  curent_dataset list holds what to plot and how
current_dataset.append('name')          # 0 unique name of dataset
current_dataset.append(1)               # 1 frame number
current_dataset.append(1)               # 2 plot image, 0=no, 1=yes
current_dataset.append(0)               # 3 plot vector, 0=no, 1=yes
current_dataset.append(0)               # 4 plot scalar, 0=no, 1=yes
current_dataset.append('path')          # 5 path to image in project
current_dataset.append(0)               # 6 min value image - default value = 0
current_dataset.append(1)               # 7 max value image - default value = 1
current_dataset.append('gray')         # 8 name of the colormap for the model image

time_step = 1
time_unit = 's'


class dialog_img(QDialog, Ui_DialogImg):
    """

    """
    def __init__(self, parent=None):
        super(dialog_img, self).__init__(parent)
        self.setupUi(self)
        self.buttonBox.clicked.connect(self.set_img_prop)


    def set_img_prop(self):
        """

        :return:
        """

        from pytecpiv_util import create_fig
        from matplotlib.figure import Figure

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

class Main(QMainWindow, Ui_MainWindow):
    """The class's docstring"""

    def __init__(self, ):
        super(Main, self).__init__()
        self.setupUi(self)
        self.menubar = self.menuBar()
        self.menubar.setNativeMenuBar(False)

        # define some callback functions here

        self.actionConfiguration.triggered.connect(self.show_conf_fn)  # menu settings
        self.dialog_conf = dialog_conf(self)

        self.dialog_img = dialog_img(self)

        self.new_project_menu.triggered.connect(self.create_new_project)  # menu new project
        self.import_calib_menu.triggered.connect(self.import_calib_img)  # menu data import calib image

        self.Dataset_comboBox.currentIndexChanged.connect(self.dataset_combobox_fn)

        self.Img_pushButton.clicked.connect(self.show_dialog_img)

    def show_dialog_img(self):
        self.dialog_img.show()

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
        dprint(' ')
        dprint(project_create_time)
        dprint('creating new project')

        # create new project_metadata file
        t = os.path.isfile('project_metadata.json')

        if t:
            os.remove('project_metadata.json')

        metadata = {'project': []}
        metadata['project'].append({'project_path': this_project_path})
        metadata['project'].append({'path': path_project})
        metadata['project'].append({'name': project_name})
        metadata['project'].append({'create_date': project_create_time})

        with open('project_metadata.json', 'w') as outfile:
            json.dump(metadata, outfile)

    def import_calib_img(self):
        from PyQt5.QtWidgets import QFileDialog
        from pytecpiv_conf import pytecpiv_get_pref, pytecpiv_set_cores
        from pytecpiv_util import dprint
        from pytecpiv_import import import_img

        import json
        import os

        global dataset_index, current_dataset, time_step

        #  get the preferences for where sources are located
        file_exist, sources_path, projects_path = pytecpiv_get_pref()

        #  pick the directory with the raw calib images; open the sources directory
        source_path_calib_img = QFileDialog.getExistingDirectory(self, 'Open directory', sources_path)

        #  get the fraction core for parallel processing from conf dialog
        fraction_cores = self.dialog_conf.SliderCores.value()
        fraction_cores = fraction_cores / 100

        n_cores, use_cores = pytecpiv_set_cores(fraction_cores)

        dprint(str(n_cores) + ' cores available')
        dprint('using ' + str(use_cores) + ' cores when parallel')

        #  open the project_metadata to get the name and path of the new project
        with open('project_metadata.json') as f:
            project_data = json.load(f)

            project = project_data["project"]
            project = project[0]
            project_path = project["project_path"]

        #  create a directory named CALIB inside the new project directory to store the imported calibration images
        project_path_calib_img = os.path.join(project_path, 'CALIB')

        t = os.path.exists(project_path_calib_img)

        if t:
            dprint('saving in directory: ' + project_path_calib_img)
        else:
            os.mkdir(project_path_calib_img)
            dprint('saving in directory: ' + project_path_calib_img)

        n_img = import_img(source_path_calib_img, project_path_calib_img, use_cores)

        project_data['project'].append({'source_calibration': source_path_calib_img,
                                        'number_calibration_images': n_img})

        # save metadata
        with open('project_metadata.json', 'w') as outfile:
            json.dump(project_data, outfile)

        # create new dataset entry and select
        dataset_index = dataset_index + 1

        current_dataset[0] = 'calibration'
        current_dataset[1] = 1
        current_dataset[2] = 1
        current_dataset[3] = 0
        current_dataset[4] = 0
        current_dataset[5] = project_path_calib_img
        current_dataset[6] = 0
        current_dataset[7] = 1
        current_dataset[8] = 'gray'

        #  change the frame number and time in gui
        self.frame_text.setText(str(1))
        self.time_text.setText(str((1 - 1) * time_step))

        # change status of chow image checkbox
        self.Img_checkBox.setCheckState(2)

        # save dataset in json file
        table_dataset = {dataset_index: []}
        table_dataset[dataset_index].append({
            'name': current_dataset[0],
            'frame': current_dataset[1],
            'plot_image': current_dataset[2],
            'plot_vector': current_dataset[3],
            'plot_scalar': current_dataset[4],
            'image_path': current_dataset[5],
            'img_value_min': current_dataset[6],
            'img_value_max': current_dataset[7],
            'img_colormap': current_dataset[8]
        })

        # save data in json file in sources
        with open('table_dataset.json', 'w') as outfile:
            json.dump(table_dataset, outfile)

        # change the selected combobox
        self.Dataset_comboBox.insertItem(int(dataset_index), 'calibration images')
        self.Dataset_comboBox.setCurrentIndex(int(dataset_index))

    def dataset_combobox_fn(self):
        """

        :param self:
        :return:
        """
        import json
        from pytecpiv_util import create_fig

        global current_dataset, fig1

        index = self.Dataset_comboBox.currentIndex()

        self.rmmpl()  # clear the mpl for a replot

        if index == 0:  # this is a special index with the credits & license

            fig1 = Figure()
            ax1f1 = fig1.add_subplot(111)
            s1 = 'pyTecPIV v0.1-alpha'
            s2 = 'build on Python 3.7 with the following packages:'
            s3 = 'numpy, scikit-image, rawpy, json, hdf5, matplotlib'
            s4 = 'GUI build with Qt5'
            s5 = 'D. Boutelier, 2020'
            ax1f1.margins(0, 0, tight=True)
            ax1f1.set_ylim([0, 1])
            ax1f1.set_xlim([0, 1])
            ax1f1.text(0.01, 0.95, s1, fontsize=12)
            ax1f1.text(0.01, 0.9, s2, fontsize=10)
            ax1f1.text(0.01, 0.85, s3, fontsize=10)
            ax1f1.text(0.01, 0.775, s4, fontsize=10)
            ax1f1.text(0.01, 0.675, s5, fontsize=8)
            ax1f1.set_aspect('equal')
            ax1f1.set_axis_off()

        else:
            #  open the table_dataset file
            with open('table_dataset.json') as f:
                table_dataset = json.load(f)
                selected_dataset = table_dataset[str(index)]
                selected_dataset = selected_dataset[0]
                current_dataset[0] = selected_dataset['name']
                current_dataset[1] = selected_dataset['frame']
                current_dataset[2] = selected_dataset['plot_image']
                current_dataset[3] = selected_dataset['plot_vector']
                current_dataset[4] = selected_dataset['plot_scalar']
                current_dataset[5] = selected_dataset['image_path']
                current_dataset[6] = selected_dataset['img_value_min']
                current_dataset[7] = selected_dataset['img_value_max']
                current_dataset[8] = selected_dataset['img_colormap']

            fig1 = Figure()
            create_fig(fig1, current_dataset)

        self.addmpl(fig1)





if __name__ == '__main__':
    import sys
    import os
    from pytecpiv_util import dprint
    from PyQt5 import QtWidgets
    from datetime import datetime

    # delete log file if it exists
    t = os.path.isfile('log.txt')
    if t:
        os.remove('log.txt')

    # create project time stamp
    project_create_time = str(datetime.now())
    dprint(' ')
    dprint(project_create_time)
    dprint("Starting new instance of PyTecPIV v0.1-alpha")

    # make the intro figure here
    fig1 = Figure()
    ax1f1 = fig1.add_subplot(111)
    s1 = 'pyTecPIV v0.1-alpha'
    s2 = 'build on Python 3.7 with the following packages:'
    s3 = 'numpy, scikit-image, rawpy, json, hdf5, matplotlib'
    s4 = 'GUI build with Qt5'
    s5 = 'D. Boutelier, 2020'
    ax1f1.margins(0, 0, tight=True)
    ax1f1.set_ylim([0, 1])
    ax1f1.set_xlim([0, 1])
    ax1f1.text(0.01, 0.95, s1, fontsize=14)
    ax1f1.text(0.01, 0.9, s2, fontsize=10)
    ax1f1.text(0.01, 0.85, s3, fontsize=10)
    ax1f1.text(0.01, 0.775, s4, fontsize=10)
    ax1f1.text(0.01, 0.7, s5, fontsize=9)
    ax1f1.set_aspect('equal')
    ax1f1.set_axis_off()

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())