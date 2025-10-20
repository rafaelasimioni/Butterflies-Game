#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Surface, Rect
from pygame.font import Font

from code.Const import WIN_WIDTH, verdeOliva, MENU_OPTION, cinzaClaro, MENU_TEXT, WIN_HEIGHT


class Menu:
    def __init__(self,window):
        self.window = window
        self.surf = pygame.image.load('./asset/MenuArvore.svg').convert_alpha()
        self.rect= self.surf.get_rect(left=0,top=0) #cria o retangulo

    def run(self, ):
        pygame.mixer_music.load('./asset/MenuMusic.wav')
        pygame.mixer_music.play(-1)
        select_option = 0
        while True:
            self.window.blit(source=self.surf, dest=self.rect)  # para imagem aparecer dentro do retangulo
            self.menu_text(80, text= "Butterflies", text_color=verdeOliva,
                           text_center_pos=((WIN_WIDTH/2),60))
            self.menu_text(60, text="Game", text_color=verdeOliva,
                           text_center_pos=(WIN_WIDTH/2,120))

            for i in range(len(MENU_OPTION)):

                if i == select_option:
                    self.menu_text(40, MENU_OPTION[i], text_color=verdeOliva, text_center_pos=((WIN_WIDTH/2), 190 + 40 * i))
                else:
                    self.menu_text(40, MENU_OPTION[i], text_color=cinzaClaro,
                                   text_center_pos=((WIN_WIDTH / 2), 190 + 40 * i))


            self.menu_text(30, MENU_TEXT, text_color=cinzaClaro, text_center_pos=(WIN_WIDTH/2, 310))

            # Check for all events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit() # Close Window
                    quit() # end pygame

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                       if select_option < len(MENU_OPTION)-1:
                           select_option +=1
                       else:
                           select_option = 0

                    if event.key == pygame.K_UP:
                        if select_option > 0:
                            select_option -= 1
                        else:
                            select_option = len(MENU_OPTION)-1

                    if event.key == pygame.K_RETURN: #ENTER
                        return MENU_OPTION[select_option]

            pygame.display.flip()

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.Font('./asset/font/malvides/Malvides.otf', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

