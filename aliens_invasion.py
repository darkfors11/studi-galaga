import sys

import pygame

class AlienInvasion:
    #Класс для управления ресурсами и поведением игры
    def __init__(self):
    #Инициализирует игру и создает игровые ресурсы
        pygame.init()

        self.screen = pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Aliens Invasion")

    def run_game(self):
    #Запускает основной цикл игры
        while True:
        # отслеживание  событий клавиатуры и мыши
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # Отоброжение последнего прорисованного экрана
            pygame.display.flip()

if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()