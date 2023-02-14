class Settings():


    # Класс для хранения всех настроек игры
    def __init__(self):
        # Инициализируем настройки игры
        # Параметры экрана

        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51,51,153)
        self.ship_speed = 1.5
        # Параметры снаряда
        self.bullet_speed = 5
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_colot = (255,51,51)
        self.bullet_allowed = 30
        # настройка скорости пришельцев
        self.alien_speed = 2.0
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.5
        # Темп роста стоимости пришельцев
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
        # обозначение двежения вправо
        self.fleet_direction = 1
        self.ship_limit = 3

    def initialize_dynamic_settings(self):
        # Инициализирует настройки изменяющиеся в ходе игры
        self.ship_speed_factor = 1.5
        self.bullet_speed_factou = 3.0
        self.alien_speed_factor = 1.0
        # давижения вправо и в лево
        self.fleet_direction = 1
        self.alien_points = 50

    def increase_speed(self):
        # увеличивает настройки скорости и стоимости пришельцев
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factou *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
