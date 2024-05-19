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
from utils import *







def main():
    while True:
        afficher_menu()
        choix = input("Entrez le numéro de l'option choisie : ")
        if choix == '0':
            print("Au revoir !")
            break
        elif choix == '1':
            message_text = input("Entrez le message à encoder : ")
            protocol_info = ['00', '11']  # Example protocol information (4 bits)
            message_length = len(message_text)
            binary_size = bin(min(message_length, 255))[2:].zfill(8)  # Encode message size as 8-bit binary with leading zeros
            message_pairs = [binary_size[i:i+2] for i in range(0, len(binary_size), 2)]  # Store as pairs of bits
            bits_pairs = convert_string_to_bits(message_text)
            bits_pairs = message_pairs + bits_pairs + protocol_info
            print("Le message codé en paire de bytes:", bits_pairs)
            bit_list = [int(bit) for binary_num in bits_pairs for bit in binary_num]
            data_with_parity = add_parity_bits(bit_list)
            print("Données avec bits de parité :", data_with_parity)

            


            print("Taille du message en binaire:", binary_size)
            print("Taille du message en paires de bits:", message_pairs)
            nombre_de_bits = len(bits_pairs)
            print('debug')
            taille_matrice = math.ceil(math.sqrt(nombre_de_bits))
            print('generation de la matrice en cours ...')
            afficher_chargement()
            protocol = GraphicalProtocol(bits_pairs, taille_matrice)
            protocol.generate_matrix('image.png')
            print('generation de la matrice terminée')

           


        elif choix == '2':
            message_text = input("Entrez le message à encoder : ")
            protocol_info = ['00', '11']  # Example protocol information (4 bits)
            message_length = len(message_text)
            binary_size = bin(min(message_length, 255))[2:].zfill(8)  # Encode message size as 8-bit binary with leading zeros
            message_pairs = [binary_size[i:i+2] for i in range(0, len(binary_size), 2)]  # Store as pairs of bits
            bits_pairs = convert_string_to_bits(message_text)
            bits_pairs = message_pairs + bits_pairs + protocol_info
            print("Le message codé en paire de bytes:", bits_pairs)
            print("Taille du message en binaire:", binary_size)
            print("Taille du message en paires de bits:", message_pairs)
            nombre_de_bits = len(bits_pairs)
            taille_matrice = math.ceil(math.sqrt(nombre_de_bits))
            print('generation de la matrice en cours ...')
            afficher_chargement()

            protocol = GraphicalProtocol(bits_pairs, taille_matrice)
            protocol.generate_matrix('combined_image.png')
            protocol.combine_with_logo('logo.png', 'combined_image.png')
            print('generation de la matrice terminée')



        elif choix == '3':
            decoded_bits1 , message_length , proto_info = decode_image('image.png')
            data_without_parity = remove_parity_bits(decoded_bits1)
            print('data without parity',data_without_parity)

            print("Bits décodés à partir de l'image sans logo (messge , taille , protocole ):", decoded_bits1 , message_length , proto_info)
            liste_dec=liste_paire_binaire_to_chaine(decoded_bits1)
            print('décodage en cours ...')
            afficher_chargement()
            print("Message décodé:", binaire_en_mot(liste_dec))
        elif choix == '4':
            decoded_bits , message_length , proto_info= decode_image('combined_image.png')
            print("Bits décodés à partir de l'image avec logo (messge , taille , protocole ):", decoded_bits , message_length , proto_info)
            liste_dec1=liste_paire_binaire_to_chaine(decoded_bits)
            print('décodage en cours ...')
            afficher_chargement()
            print("Message décodé:", binaire_en_mot(liste_dec1))
            
        elif choix == '5':
            afficher_informations()

        elif choix == '6':
            if 'image.png' in os.listdir():
                print('affichage de l image généré sans logo')
                afficher_image('image.png')
            else:
                print('l image n existe pas')

            if 'combined_image.png' in os.listdir():
                print('affichage de l image généré avec logo')
                afficher_image('combined_image.png')
        elif choix == '7':
            help()
        else:
            print("Option invalide. Veuillez choisir une option valide.")

if __name__ == "__main__":
    main()


