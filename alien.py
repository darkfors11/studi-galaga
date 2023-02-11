import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    def __init__(self,ai_game):
        super().__init__()
        self.screen = ai_game.screen
        # Загрузка изображения пришельца и назначение атрибута rect
        self.image = pygame.image.load('images/alien.png')
        self.rect = self.image.get_rect()
        # Каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        # Сохранение точной горизонтальной позиции
        self.x = float(self.rect.x)
        self.settings = ai_game.settings
    def update(self):
        # Перемещение пришельцев
        #self.x += self.settings.alien_speed

        # Перемещение пришельцев влево или вправо
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x
    def checka_edges(self):
        # Возвращает True если пришелец находится у края экрана
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right or self.rect.left <= 0:
            return True