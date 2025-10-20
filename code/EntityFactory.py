#!/usr/bin/python
# -*- coding: utf-8 -*-
import random


from code.Background import Background
from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Enemy import Enemy
from code.Player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name:str, position=(0,0)):

        if entity_name == 'Level1Bg':
            list_bg = []
            for i in range(2):
                list_bg.append(Background(f'Level1Bg{i}', (0, 0)))
                list_bg.append(Background(f'Level1Bg{i}', (WIN_WIDTH, 0)))
            return list_bg

        if entity_name == 'Player1':
            return Player('Player1', (0,WIN_HEIGHT/2))


        if entity_name == 'Enemy1':
            return Enemy('Enemy1', (WIN_WIDTH,random.randint(0,WIN_HEIGHT)))
        elif entity_name == 'Enemy2':
            return Enemy('Enemy2', (WIN_WIDTH, random.randint(0, WIN_HEIGHT)))
        return None


