"""
Модуль конфигурации игры
"""

# Настройки игры
GAME_TITLE = "Star Courier"
VERSION = "0.1.0"

# Путь к сохранениям
SAVE_DIR = "saves"
DEFAULT_SAVE = "save.json"

# Параметры отображения
TEXT_WIDTH = 80
SPEED_DELAY = 0.02  # задержка между символами (0 = мгновенно)

# Начальные параметры игрока
DEFAULT_STATS = {
    "alchemy": 0,      # алхимия
    "biotics": 0,      # биотика
    "psychic": 0,      # психика
}

# Максимальный уровень отношений
MAX_RELATIONSHIP = 100
