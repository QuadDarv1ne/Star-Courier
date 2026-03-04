"""
Модуль конфигурации игры
"""

# Настройки игры
GAME_TITLE = "Star Courier"
VERSION = "0.1.0"
MAX_SAVE_SLOTS = 10

# Пути к данным
SAVE_DIR = "saves"
DEFAULT_SAVE = "save.json"
CHAPTERS_DIR = "chapters"
CHARACTERS_DIR = "characters"

# Параметры отображения
TEXT_WIDTH = 80
SPEED_DELAY = 0.02  # задержка между символами (0 = мгновенно)

# Начальные параметры игрока
DEFAULT_STATS = {
    "alchemy": 0,      # алхимия
    "biotics": 0,      # биотика
    "psychic": 0,      # психика
}
DEFAULT_HP = 100
DEFAULT_ENERGY = 100

# Отношения
MAX_RELATIONSHIP = 100
MIN_RELATIONSHIP = 0

# Баланс
STARTING_CREDITS = 100
MAX_INVENTORY_SLOTS = 20
