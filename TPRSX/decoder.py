import os
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np
from PIL import Image
import math
from tkinter import Tk, Canvas
from PIL import ImageTk
from PIL import ImageDraw
from tqdm import tqdm
import time
import matplotlib.image as mpimg
from graphical_protocol import *
from bit_operations import *
from utils import *


def decode_image(path_to_image):
    img = Image.open(path_to_image)
    pixels = np.array(img)
    bit_pairs = []
    message_length = None
    protocol_info = None

    for row_index in range(50, len(pixels), 100):
        for col_index in range(50, len(pixels[row_index]), 100):
            pixel = pixels[row_index][col_index]
            # Vérifier la couleur du pixel au milieu de chaque forme géométrique
            if col_index % 2 == 0 and row_index % 2 == 0:  # Vérifier les pixels du milieu
                x = col_index + 0.5
                y = row_index + 0.5

                # Vérifier la couleur du pixel du milieu pour déterminer la forme géométrique
                if np.array_equal(pixel, [255, 255, 0, 255]):  # Jaune (étoile)
                    bit_pairs.append('00')
                elif np.array_equal(pixel, [0, 0, 255, 255]):  # Bleu (cercle)
                    bit_pairs.append('01')
                elif np.array_equal(pixel, [0, 128, 0, 255]):  # Vert (carré)
                    bit_pairs.append('10')
                elif np.array_equal(pixel, [255, 0, 0, 255]):  # Rouge (triangle)
                    bit_pairs.append('11')
    
    # Extract protocol information and message length from the decoded bit_pairs
    protocol_info = bit_pairs[-2:]  # Last 4 bits represent the protocol information
    message_length_bits = bit_pairs[:4]  # Last 2 pairs of bits represent the message length
    message_length = int(''.join(message_length_bits), 2)  # Convert binary to integer

    # Remove the protocol information and message length bits from the bit_pairs
    bit_pairs = bit_pairs[4:-2]

    return bit_pairs, message_length, protocol_info