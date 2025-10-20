# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# import random
# import sys
#
#
# import pygame
#
# from code.Const import EVENT_ENEMY, SPAWN_TIME
# from code.Entity import Entity
# from code.EntityFactory import EntityFactory
#
#
# class Level:
#     def __init__(self, window,name,game_mode):
#         self.window = window
#         self.name = name
#         self.game_mode = game_mode
#         self.entity_list : list[Entity] = []
#         self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
#         self.entity_list.append(EntityFactory.get_entity('Player1'))
#         #pygame.time.Clock()
#        # self.timeout = 20000
#         pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
#
#
#     def run(self, ):
#         # clock.tick(60)
#         while True:
#             for ent in self.entity_list:
#                 self.window.blit(source=ent.surf, dest=ent.rect)
#                 ent.move()
#
#             font = pygame.font.Font(None, 36)  # fonte padrão, tamanho 36
#             player = next((ent for ent in self.entity_list if ent.name == "Player1"), None)
#
#             if player:
#                 text = font.render(f"Borboletas: {player.score}", True, (255, 255, 255))  # texto branco
#                 self.window.blit(text, (20, 20))  # posição do texto na tela
#
#             pygame.display.flip()
#
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#
#                 if event.type == EVENT_ENEMY:
#                     choice = random.choice(('Enemy1', 'Enemy2'))
#                     self.entity_list.append(EntityFactory.get_entity(choice))
#
#


# #!/usr/bin/python
# # -*- coding: utf-8 -*-
# import sys
# import pygame
#
# from code.Entity import Entity
# from code.EntityFactory import EntityFactory
#
#
# class Level:
#     def __init__(self, window, name, game_mode):
#         self.window = window
#         self.name = name
#         self.game_mode = game_mode
#         self.entity_list: list[Entity] = []
#
#         # Fundo
#         bg_entities = EntityFactory.get_entity('Level1Bg')
#         if bg_entities:
#             self.entity_list.extend(bg_entities)
#
#         # Player
#         self.player = EntityFactory.get_entity('Player1')
#         if self.player:
#             self.entity_list.append(self.player)
#
#         # Enemies (borboletas)
#         self.enemies = []
#         for i in range(5):
#             enemy = EntityFactory.get_entity('Enemy1')
#             if enemy:
#                 self.entity_list.append(enemy)
#                 self.enemies.append(enemy)
#
#     def run(self):
#         clock = pygame.time.Clock()
#         font = pygame.font.Font(None, 36)
#
#         while True:
#             # Eventos
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#
#             # Atualiza e desenha entidades
#             self.window.fill((255, 255, 255))  # fundo branco para limpar tela
#
#             for ent in self.entity_list:
#                 ent.move()
#                 self.window.blit(ent.surf, ent.rect)
#
#             # ⚡ Verifica colisão entre Player e cada Enemy
#             for enemy in self.enemies[:]:  # cópia da lista
#                 if self.player.rect.colliderect(enemy.rect):
#                     self.player.score += 1       # soma pontos
#                     self.entity_list.remove(enemy)  # remove da tela
#                     self.enemies.remove(enemy)
#
#             # 🦋 Exibe pontuação na tela
#             score_text = font.render(f"Borboletas: {self.player.score}", True, (0, 0, 0))
#             self.window.blit(score_text, (20, 20))
#
#             # Atualiza tela
#             pygame.display.flip()
#             clock.tick(60)


#!/usr/bin/python
# -*- coding: utf-8 -*-
# import random
# import sys
# import pygame
#
# from code.Const import EVENT_ENEMY, SPAWN_TIME
# from code.Entity import Entity
# from code.EntityFactory import EntityFactory
#
#
# class Level:
#     def __init__(self, window, name, game_mode):
#         self.window = window
#         self.name = name
#         self.game_mode = game_mode
#         self.entity_list: list[Entity] = []
#         self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
#         self.entity_list.append(EntityFactory.get_entity('Player1'))
#
#         pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
#
#     def run(self):
#         clock = pygame.time.Clock()
#
#         while True:
#             self.window.fill((0, 0, 0))  # limpa a tela antes de desenhar
#             clock.tick(60)
#
#             # atualiza e desenha entidades
#             for ent in self.entity_list:
#                 self.window.blit(source=ent.surf, dest=ent.rect)
#                 ent.move()
#
#             # obtém o player
#             player = next((ent for ent in self.entity_list if ent.name == "Player1"), None)
#
#             # checa colisões do player com inimigos (borboletas)
#             if player:
#                 for enemy in [e for e in self.entity_list if "Enemy" in e.name]:
#                     if player.rect.colliderect(enemy.rect):
#                         player.score += 1
#                         self.entity_list.remove(enemy)  # remove a borboleta capturada
#
#                 # exibe contagem de borboletas capturadas
#                 font = pygame.font.Font(None, 36)
#                 text = font.render(f"Borboletas: {player.score}", True, (255, 255, 255))
#                 self.window.blit(text, (20, 20))
#
#             pygame.display.flip()
#
#             # eventos do jogo
#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#
#                 if event.type == EVENT_ENEMY:
#                     for i in range (3):
#                         choice = random.choice(('Enemy1', 'Enemy2'))
#                         self.entity_list.append(EntityFactory.get_entity(choice))


#!/usr/bin/python
# -*- coding: utf-8 -*-
import random
import sys
import pygame

from code.Const import EVENT_ENEMY, SPAWN_TIME
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:
    def __init__(self, window, name, game_mode):
        self.wim = None
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))

        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)

        # ⏱️ Controle de tempo e pontuação
        self.start_time = pygame.time.get_ticks()
        self.missed_butterflies = 0
        self.game_over = False

    def run(self):
        clock = pygame.time.Clock()
        font = pygame.font.Font(None, 36)

        while True:
            self.window.fill((0, 0, 0))
            clock.tick(60)

            # Atualiza e desenha entidades
            for ent in list(self.entity_list):  # list() para poder remover enquanto itera
                ent.move()
                self.window.blit(source=ent.surf, dest=ent.rect)

                # Verifica se é uma borboleta que saiu da tela → perdeu
                if "Enemy" in ent.name and ent.rect.right < 0:
                    self.entity_list.remove(ent)
                    self.missed_butterflies += 1

            # Pega o player
            player = next((ent for ent in self.entity_list if ent.name == "Player1"), None)

            # Colisões e pontuação
            if player:
                for enemy in [e for e in self.entity_list if "Enemy" in e.name]:
                    if player.rect.colliderect(enemy.rect):
                        player.score += 1
                        self.entity_list.remove(enemy)

                # Exibe placar
                text_score = font.render(f"Borboletas: {player.score}", True, (255, 255, 255))
                text_missed = font.render(f"Perdidas: {self.missed_butterflies}", True, (255, 100, 100))
                self.window.blit(text_score, (20, 20))
                self.window.blit(text_missed, (20, 50))

            # ⏱️ Verifica o tempo e condições de game over
            elapsed_time = (pygame.time.get_ticks() - self.start_time) / 1000  # segundos
            if elapsed_time >= 10:
                self.wim = True

            if self.missed_butterflies >= 10:
                self.game_over = True

            # Tela de Game Over
            if self.game_over:
                win = font.render("YOU WIN", True, (255, 255, 255))
                game_over_text = font.render("GAME OVER!", True, (255, 0, 0))
                final_score_text = font.render(f"Borboletas capturadas: {player.score}", True, (255, 255, 255))
                self.window.blit(game_over_text, (self.window.get_width() // 2 - 100, self.window.get_height() // 2))
                self.window.blit(final_score_text, (self.window.get_width() // 2 - 150, self.window.get_height() // 2 + 40))
                pygame.display.flip()
                pygame.time.wait(SPAWN_TIME)
                pygame.quit()
                sys.exit()

            pygame.display.flip()

            # Eventos
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == EVENT_ENEMY:
                    # Cria 3 borboletas por evento
                    for _ in range(3):
                        choice = random.choice(('Enemy1', 'Enemy2'))
                        self.entity_list.append(EntityFactory.get_entity(choice))
