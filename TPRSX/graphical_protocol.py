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
from decoder import *
from bit_operations import *
from utils import *


class GraphicalProtocol:
    def __init__(self, message, matrix_size):
        self.message = message
        self.matrix_size = matrix_size
        self.cell_size = 1  # Taille de chaque cellule en pixels
    
   

    def combine_with_logo(self, logo_path, output_path):
        logo = Image.open(logo_path)

        logo = logo.resize((50, 50))

        image_with_grid = Image.open('image.png')

        grid = Image.new('RGBA', image_with_grid.size, (0, 0, 0, 0))

        grid.paste(image_with_grid, (0, 0))

        logo_position = (int((image_with_grid.width - logo.width) / 2), int((image_with_grid.height - logo.height) / 2))

        grid.paste(logo, logo_position, mask=logo)

        grid.save(output_path)

    def generate_matrix(self, pathtoimg):
        fig, ax = plt.subplots(figsize=(self.matrix_size, self.matrix_size))
        for i, bits in enumerate(self.message):
            row = i // self.matrix_size
            col = i % self.matrix_size
            shape = self.bits_to_shape(bits)
            color = self.shape_to_color(shape)
            self.draw_shape(ax, row, col, shape, color)

        plt.xlim(0, self.matrix_size)
        plt.ylim(0, self.matrix_size)
        ax.set_aspect(1)
        ax.axis('off')
        # Supprimer les marges blanches autour de la figure et les axes x et y
        plt.axis('off')
        plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
        plt.savefig('image.png', bbox_inches='tight', pad_inches=0)
        print("La matrice a été générée avec succès et enregistrée dans le fichier '{}'.".format(pathtoimg))

    def bits_to_shape(self, bits):
        if bits == '00':
            return 'star'
        elif bits == '01':
            return 'circle'
        elif bits == '10':
            return 'square'
        elif bits == '11':
            return 'triangle'

    def shape_to_color(self, shape):
        if shape == 'star':
            return 'yellow'
        elif shape == 'circle':
            return 'blue'
        elif shape == 'square':
            return 'green'
        elif shape == 'triangle':
            return 'red'

    def draw_shape(self, ax, row, col, shape, color):
        x = col
        y = self.matrix_size - row - 1
        if shape == 'star':
            ax.plot(x + 0.5, y + 0.5, marker='*', markersize=50, markerfacecolor=color,markeredgecolor='white')
        elif shape == 'circle':
            ax.plot(x + 0.5, y + 0.5, marker='o', markersize=50, markerfacecolor=color,markeredgecolor='white')
        elif shape == 'square':
            ax.add_patch(patches.Rectangle((x, y), 1, 1, fill=True, color=color))
        elif shape == 'triangle':
            ax.plot(x + 0.5, y + 0.5, marker='^', markersize=50, markerfacecolor=color,markeredgecolor='white')