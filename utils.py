import math
import numpy as np
from PIL import Image

def dist(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

def arr_to_img(arr):
    '''
    accepts: numpy array with shape (Height, Width, Channels)
    returns: binary stream (used to save to database)
    '''
    arr = np.uint8(arr)
    img = Image.fromarray(arr)
    return img

def is_number_type(i):
    return type(i) == int or type(i) == float