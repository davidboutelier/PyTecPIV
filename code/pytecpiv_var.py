#  initialise some global variables here
dataset_index = 0
time_step = 1

#  curent_dataset holds what to plot and how
current_dataset = []
current_dataset.append('name')          # 0 unique name of dataset
current_dataset.append(1)               # 1 frame number
current_dataset.append(1)               # 2 plot image, 0=no, 1=yes
current_dataset.append(0)               # 3 plot vector, 0=no, 1=yes
current_dataset.append(0)               # 4 plot scalar, 0=no, 1=yes
current_dataset.append('path')          # 5 path to image in project
current_dataset.append(0)               # 6 min value image - default value = 0
current_dataset.append(1)               # 7 max value image - default value = 1
current_dataset.append('Greys')          # 8 name of the colormap for the model image