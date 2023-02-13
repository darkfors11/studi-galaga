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
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10
        # обозначение двежения вправо
        self.fleet_direction = 1
        self.ship_limit = 3