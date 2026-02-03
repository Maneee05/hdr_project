import pygame,sys
from pygame.locals import *
import numpy as np
from tensorflow.keras.models import load_model
import cv2     # to read the image

WINDOWSIZEX=640
WINDOWSIZEY=480

# Initialise pygame
pygame.init()
pygame.display.set_mode(WINDOWSIZEX,WINDOWSIZEY)