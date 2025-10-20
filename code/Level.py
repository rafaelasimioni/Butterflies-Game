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
