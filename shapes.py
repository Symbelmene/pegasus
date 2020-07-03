# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 23:41:53 2020

@author: chris
"""

import pygame

def drawPoly():
    pygame.draw.polygon(win, (100, 100, 100), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
    
def drawTriangle():
    pygame.draw.polygon(win, (100, 100, 100), ((0,100), (0,200), (100, 150))