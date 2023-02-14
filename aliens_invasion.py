import sys

import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard

class AlienInvasion:
    #Класс для управления ресурсами и поведением игры
    def __init__(self):
    #Инициализирует игру и создает игровые ресурсы
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        pygame.display.set_caption("Aliens Invasion")

    # Создание кнопки плей
        self.play_button = Button(self, 'Play')
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._creat_fleet()
        self.game_active = False
    # Игровая статистика
        self.stats = GameStats(self)
        self.sb = Scoreboard(self)








    def run_game(self):
        self._update_screen()
    #Запускает основной цикл игры
        while True:
            self._check_events()
            if self.stats.game_active:
                # При каждом проходе цикла перерисовывать экран
                self._update_screen()
                self.ship.update()
                self._update_bullets()
                self._update_aliens()






    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_event(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_event(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._chek_play_button(mouse_pos)
            self.ship.rect.x += 1

    def _chek_play_button(self,mouse_pos):
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.stats.game_active:
            self.settings.initialize_dynamic_settings()
            # Сброс игровой статистики
            self.stats.reset_stats()
            self.stats.game_active = True
            self.sb.prep_scpre()
            # Очистка списка пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # Создание нового флота и размещение корабля в центре
            self._creat_fleet()
            self.ship.center_ship()




    def _check_keydown_event(self,event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()


    def _check_keyup_event(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False


    def _fire_bullet(self):
        # Создание нового снаряда и включение его в группу bullets
        if len(self.bullets) < self.settings.bullet_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        # Удаление снарядов, вышедщих за край экрана
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collisions()

    def _check_bullet_alien_collisions(self):
        # Проверка попаданий в пришельцев
        collisions = pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.sb.prep_scpre()
        if not self.aliens:
            self.bullets.empty()
            self._creat_fleet()
            self.settings.increase_speed()




    def _update_aliens(self):
        self._chek_feet_edges()
        self.aliens.update()
        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()

        self._chek_aliens_bottom()

    def _creat_fleet(self):
        # Создание флота вторжения
        # Создание пришельца
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        available_space_x = self.settings.screen_width - (2*alien_width)
        number_alien_x = available_space_x//(2* alien_width)
        # Определяет колличество рядов помещающихся на экране
        ship_hight = self.ship.rect.height
        available_space_y = (self.settings.screen_height - (3 * alien_height) - ship_hight)
        number_rows = available_space_y//(2 * alien_height)
        for row_namber in range(number_rows):
            for alien_namber in range(number_alien_x):
                self._creat_alien(alien_namber,row_namber)




    def _creat_alien(self, alien_namber,row_namber):

        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        alien.x = alien_width + 2 * alien_width * alien_namber
        alien.rect.x = alien.x
        alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_namber
        self.aliens.add(alien)

    def _chek_feet_edges(self):
        # Реагирует на достижение пришельцем края экрана
        for alien in self.aliens.sprites():
            if alien.checka_edges():
                self._chek_feet_direction()
                break

    def _chek_feet_direction(self):
        # Опускает весь флот и меняет направление флота
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _ship_hit(self):
        # Уменьшает жизни
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            # Очистка списков пришельцев и снарядов
            self.aliens.empty()
            self.bullets.empty()
            # Создание нового флота и размещение корабля в центре
            self._creat_fleet()
            self.ship.center_ship()
            # Пауза
            sleep(0.5)
        else:
            self.stats.game_active = False

    def _chek_aliens_bottom(self):
        # Проверяет добрались ли пришельци до нижнего края экрана
        screen_rect = self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break




    def _update_screen(self):


        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()

        for bullet in self.bullets.sprites():
            bullet.draf_bullet()

        self.aliens.draw(self.screen)
        self.sb.show_score()
        if not self.stats.game_active:
            self.play_button.draw_button()
        # Отоброжение последнего прорисованного экрана
        pygame.display.flip()






if __name__ == '__main__':
    # Создание экземпляра и запуск игры
    ai = AlienInvasion()
    ai.run_game()