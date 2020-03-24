"""The module's docstring"""

from matplotlib.figure import Figure
from classes.pytecpiv_class_main import Main

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
    ax1f1.margins(0, 0, tight=True)
    ax1f1.set_ylim([0, 1])
    ax1f1.set_xlim([0, 1])
    ax1f1.text(0.01, 0.95, s1, fontsize=12)
    ax1f1.text(0.01, 0.9, s2, fontsize=10)
    ax1f1.text(0.01, 0.85, s3, fontsize=10)
    ax1f1.text(0.01, 0.775, s4, fontsize=10)
    ax1f1.set_aspect('equal')
    ax1f1.set_axis_off()

    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.addmpl(fig1)
    main.show()
    sys.exit(app.exec_())