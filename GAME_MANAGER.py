#Game manager just loads the scripts in order, making this game a more complete experience.
#Each script can be ran without the others, but when they end, the game itself ends.
import pygame
import sys
import random

#This is basically the entire game. It was done this way because it makes it easier to reuse code.
import Game_Intro

import TitleScreen

try:
    import Level1
except:
    ""

import Level2_Intro

try:
    import Level2
except:
    ""

import Level3_Intro

try:
    import Level3
except:
    ""

import Level4_Intro

try:
    import Level4
except:
    ""
    
import Level5_Intro

try:
    import Level5
except:
    ""

import Ending
