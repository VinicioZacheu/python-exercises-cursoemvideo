#write a program that can single one song in python!

import pygame
pygame.init()
pygame.mixer.music.load('ex021.py1.mp3')
pygame.mixer.music.play()
pygame.event.wait()
