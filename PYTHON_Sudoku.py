import pygame as pg
import random
import math

preto = (0,0,0)
vermelho = (255,0,0)
verde = (0,255,0)
azul_claro = (200,200,255)
azul = (100,100,255)
branco = (255,255,255)

window = pg.display.set_mode((1000,700))

pg.font.init()

fonte = pg.font.SysFont("Courier New", 50, bold=True)