import sys

import pygame
from settings import Settings
from ship import Ship
class AlienInvasion:
    #Класс для управления ресурсами и поведением игры
    def __init__(self):
    #Инициализирует игру и создает игровые ресурсы
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("Aliens Invasion")
        self.ship = Ship(self)
        # Назначение цвета фона


    def run_game(self):
    #Запускает основной цикл игры
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()
            # При каждом проходе цикла перерисовывать экран

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = False

                    # Переместить корабль вправо
                    self.ship.rect.x += 1

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        # Отоброжение последнего прорисованного экрана
        pygame.display.flip()




if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()