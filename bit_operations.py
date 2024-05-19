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
from utils import *


def convert_string_to_bits(message):
    # Convertir chaque caractère en code ASCII puis en bits (8 bits)
    bits_list = ['{0:08b}'.format(ord(char)) for char in message]
    # Concaténer tous les tableaux de bits en un seul
    bits_string = ''.join(bits_list)
    cc=bits_string
    print('convert to string',cc)
    # Séparer la chaîne de bits en paires
    # Séparer la chaîne de bits en paires
    pairs = [cc[i] + cc[i+1] for i in range(0, len(cc), 2)]
    print('convert to pairs',pairs)

    return pairs

def liste_paire_binaire_to_chaine(liste_paires):
    chaine_concatenee = ''.join(liste_paires)
        
    longueur = len(chaine_concatenee)
        
    nombre_groupes = longueur // 8
        
    groupes = [chaine_concatenee[i*8:(i+1)*8] for i in range(nombre_groupes)]
        
    chaine_resultat = ' '.join(groupes)
        
    return chaine_resultat


def binaire_en_mot(binaire):
    mots = binaire.split()
    mot = ''.join(chr(int(x, 2)) for x in mots)
    return mot



def calculer_bit_parite(data):
    """
    Calcule le bit de parité pour une séquence de bits.
    
    :param data: Une séquence de bits (une liste ou un tuple de 0 et de 1).
    :return: Le bit de parité (0 ou 1).
    """
    return sum(data) % 2

def verifier_bit_parite(data_with_parity):
    """
    Vérifie si le bit de parité est correct pour une séquence de bits donnée.
    
    :param data_with_parity: Une séquence de bits avec le bit de parité à la fin.
    :return: True si le bit de parité est correct, False sinon.
    """
    return sum(data_with_parity) % 2 == 0

def detecter_erreur(data_with_parity):
    """
    Détecte une erreur dans une séquence de bits avec le bit de parité.
    
    :param data_with_parity: Une séquence de bits avec le bit de parité à la fin.
    :return: L'index du bit erroné s'il est détecté, sinon None.
    """
    return next((i for i, bit in enumerate(data_with_parity[:-1]) if bit != verifier_bit_parite(data_with_parity)), None)

def string_to_binary(string):
    """
    Convertit une chaîne de caractères en une séquence de bits binaire.
    
    :param string: La chaîne de caractères à convertir.
    :return: La séquence de bits binaire (une liste de 0 et de 1).
    """
    return [int(bit) for bit in ''.join(format(ord(char), '08b') for char in string)]

def add_parity_bits(data):
    """
    Ajoute des bits de parité à chaque octet de données.
    
    :param data: Une séquence de bits (une liste ou un tuple de 0 et de 1).
    :return: La séquence de bits avec des bits de parité ajoutés.
    """
    data_with_parity = []
    for i in range(0, len(data), 8):
        byte = data[i:i+8]
        parity_bit = calculer_bit_parite(byte)
        data_with_parity.extend(byte + [parity_bit])
    return data_with_parity

def remove_parity_bits(data_with_parity):
    """
    Supprime les bits de parité de chaque octet de données.
    
    :param data_with_parity: Une séquence de bits avec des bits de parité à la fin de chaque octet.
    :return: Les données sans les bits de parité.
    """
    return [byte for i, byte in enumerate(data_with_parity) if (i + 1) % 9 != 0]


def convert_to_binary_list(data_with_parity):
    """
    Convertit les données avec les bits de parité en une liste de paires de bits.
    
    :param data_with_parity: Une séquence de bits avec des bits de parité à la fin de chaque octet.
    :return: Une liste de paires de bits.
    """
    binary_list = []
    for i in range(0, len(data_with_parity), 9):
        byte_with_parity = data_with_parity[i:i+9]
        byte_data = byte_with_parity[:-1]  # Enlever le bit de parité
        binary_list.extend([''.join(map(str, byte_data[j:j+2])) for j in range(0, len(byte_data), 2)])
    return binary_list



def reconstruct_binary_list(data_with_parity):
    """
    Reconstitue les données avec les bits de parité en une liste de paires de bits.
    
    :param data_with_parity: Une séquence de bits avec des bits de parité à la fin de chaque octet.
    :return: Une liste de paires de bits.
    """
    binary_list = []
    for i in range(0, len(data_with_parity), 9):
        byte_with_parity = data_with_parity[i:i+9]
        byte_data = byte_with_parity[:-1]  # Enlever le bit de parité
        for j in range(0, len(byte_data), 2):
            binary_list.append(''.join(map(str, byte_data[j:j+2])))
    return binary_list

def add_parity_bits_to_pairs(data_with_parity):
    """
    Reconstitue les données avec les bits de parité en une liste de paires de bits.
    
    :param data_with_parity: Une séquence de bits avec des bits de parité à la fin de chaque octet.
    :return: Une liste de paires de bits.
    """
    binary_list = []
    for i in range(0, len(data_with_parity), 9):
        byte_with_parity = data_with_parity[i:i+9]
        binary_list.extend([''.join(map(str, byte_with_parity[j:j+2])) for j in range(0, len(byte_with_parity), 2)])
    return binary_list
