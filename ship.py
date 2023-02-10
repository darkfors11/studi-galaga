import pygame

class Ship():
    # Класс для управления кораблем
    def __init__(self, ai_game):
        # Инициализирует корабль и задает его начальные позиции
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        # Загружает изображение корабля и получает прямоугольник
        self.image = pygame.image.load('ship.bmp')
        self.rect = self.image.get_rect()
        # Каждый новый корабль появляется у нижнего края экрана
        self.rect.midbottom = self.screen_rect.midbottom
        # Флаг перемещения
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Обновляет позицию коробля с учетом флага
        if self.moving_right:
            self.rect.x += 1
        elif self.moving_left:
            self.rect.x -= 1
    def blitme(self):
        # Рисует корабль в текущей позиции
        self.screen.blit(self.image,self.rect)