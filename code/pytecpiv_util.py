"""
This is a collection of utility functions.
"""

def dprint(content):
    """
    Command for printing to the screen and in a log file.
    """
    print(content)
    log_file = open('log.txt', 'a')
    print(content, file=log_file)
    log_file.close()

def rgb2gray(rgb):
    import numpy as np
    return np.dot(rgb[..., :3], [0.2989, 0.5870, 0.1140])

def colorbar(mappable):
    import matplotlib.pyplot as plt
    from mpl_toolkits.axes_grid1 import make_axes_locatable
    ax = mappable.axes
    fig = ax.figure
    divider = make_axes_locatable(ax)
    cax = divider.append_axes("right", size="3%", pad=0.1)
    cax.tick_params(labelsize=7)
    return fig.colorbar(mappable, cax=cax)

def create_fig(fig1, dataset):
    from skimage import img_as_float
    import os
    from skimage import io
    """The method's docstring"""
    dataset_name = dataset[0]  # get name of dataset
    frame_number = dataset[1]

    image_path = dataset[5]

    if dataset_name == 'calibration':
        min_val = dataset[6]
        max_val = dataset[7]

        ax1f1 = fig1.add_subplot(111)
        img = img_as_float(io.imread(os.path.join(image_path, 'IMG_' + str(frame_number) + '.tif')))
        img = (img - min_val) / (max_val - min_val)
        im = ax1f1.imshow(img, cmap='gray')
        colorbar(im)
        ax1f1.set_aspect('equal')

    elif dataset_name == 'experiment':
        plot_image = dataset[2]  # boolean: plot image or not
        if plot_image == 1:
            min_val = dataset[6]
            max_val = dataset[7]
            ax1f1 = fig1.add_subplot(111)
            img = img_as_float(io.imread(os.path.join(image_path, 'IMG_' + str(frame_number) + '.tif')))
            img = (img - min_val) / (max_val - min_val)
            im = ax1f1.imshow(img, cmap='gray')
            colorbar(im)
            ax1f1.set_aspect('equal')
        else:
            print('nothing to plot')