def convert_dng(frame_num, file, dir_out):
    """
    This function converts a dng to 16-bit tiff file using rawpy and saves it in designated directory.
    """
    import os
    import rawpy
    import numpy as np
    import warnings
    from skimage import io, img_as_uint
    from pytecpiv_util import dprint, rgb2gray

    with rawpy.imread(file) as raw:
        rgb = raw.postprocess()
        grayscale_image = rgb2gray(rgb)
        grayscale_image_max = np.max(grayscale_image.flatten())
        grayscale_image_min = np.min(grayscale_image.flatten())
        grayscale_image = (grayscale_image - grayscale_image_min) / (grayscale_image_max - grayscale_image_min)
        warnings.filterwarnings("ignore", category=UserWarning)
        bit_16_grayscale_image = img_as_uint(grayscale_image)
        io.imsave(os.path.join(dir_out, 'IMG_' + str(frame_num + 1) + '.tif'), bit_16_grayscale_image)
        dprint('- image ' + file + ' imported')

def import_img(path_in, path_out, use_cores):


    import os
    from joblib import Parallel, delayed

    #  list the images in the source directory and count the number of images
    list_img = sorted(os.listdir(path_in))
    n_img = len(list_img)

    Parallel(n_jobs=use_cores)(delayed(convert_dng)(frame_num,
                                                    os.path.join(path_in,
                                                                 list_img[frame_num]),
                                                    path_out) for frame_num in range(0, n_img))

    return n_img