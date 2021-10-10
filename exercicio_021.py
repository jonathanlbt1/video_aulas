# EXERCICIO 21 - IMPORTANDO UMA MÚSICA COM PYGAME

import pygame
pygame.mixer.init()
pygame.mixer.music.load('Everything_I_See.mp3')
pygame.mixer.music.play()
input()
