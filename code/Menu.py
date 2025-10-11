#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, verdeOliva, MENU_OPTION, cinzaClaro


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuArvore.svg')
        self.rect= self.surf.get_rect(left=0,top=0) #cria o retangulo

    def run(self, ):
        pygame.mixer_music.load('./asset/MenuMusic.wav')
        pygame.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # para imagem aparecer dentro do retangulo
            self.menu_text(80, text= "Butterflies", text_color=verdeOliva,
                           text_center_pos=((WIN_WIDTH/2),60))
            self.menu_text(60, text="Game", text_color=verdeOliva,
                           text_center_pos=(WIN_WIDTH/2,120))

            for i in range(len(MENU_OPTION)):
                self.menu_text(40, MENU_OPTION[i], text_color=cinzaClaro, text_center_pos=((WIN_WIDTH/2), 200 + 45 * i))


            pygame.display.flip()


        # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:

                    pygame.quit() # Close Window
                    quit() # end pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/font/malvides/Malvides.otf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

