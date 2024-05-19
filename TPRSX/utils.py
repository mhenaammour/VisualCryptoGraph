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
from graphical_protocol import *
from bit_operations import *




def afficher_chargement():
    # Utilisation de tqdm pour afficher une barre de progression
    for _ in tqdm(range(10), desc="Chargement", unit=" ", ascii=False):
        time.sleep(0.1)  # Pause de 0.1 seconde entre chaque itération pour simuler le chargement



def afficher_image(image_path):
    img = mpimg.imread(image_path)
    plt.imshow(img)
    plt.axis('off')
    plt.show()


def afficher_menu():
    print("================== Menu ===================")
    print("0. Quitter le programme")
    print("1. Coder une information SANS image")
    print("2. Coder une information AVEC image")
    print("3. Décodage SANS image")
    print("4. Décodage AVEC image")
    print("5. Afficher les informations sur le protocole")
    print('6. afficher image code generé ')
    print("7. Aide")

def help():
    print("Aide:")
    print("- Pour coder une information SANS image, entrez le message à encoder.")
    print("- Pour coder une information AVEC image, entrez le message à encoder.")
    print('l image sans logo décodéer sera par defaut ''image.png''')
    print('l image avec logo décodéer sera par defaut ''combined_image.png''')
    print("- Pour afficher les informations sur le protocole, entrez l'option 5.")
    print("- Pour quitter le programme, entrez l'option 0.")




def afficher_informations():
    print("Informations sur le protocole:")
    print("- Le protocole utilise une représentation graphique pour encoder les données.")
    print("- Chaque forme géométrique (étoile, cercle, carré, triangle) représente une paire de bits.")
    print("- Les couleurs (jaune, bleu, vert, rouge) des formes indiquent la valeur des bits.")
    print("- Le protocole utilise un logo pour la combinaison avec l'image.")
    print("- Lors du décodage, le protocole extrait les informations à partir des pixels d'une image.")
    print("- Le décodage peut se faire avec ou sans l'image combinée avec le logo.")
    print("- Le protocole utilise les 4 derniers bits pour stocker des informations sur le protocole.")
    print("- Le protocole utilise les 4 premiers bits pour stocker la taille du message.")
    print("- Le protocole utilise une grille pour afficher les formes géométriques.")
    print("- Le protocole est identifie par la séquence '0011' qui est codé avec le message pour marquer le protocle.")
          

