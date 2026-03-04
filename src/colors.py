"""
Цветовая поддержка для терминала
"""

import sys


class Colors:
    """ANSI цвета для терминала"""
    
    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    
    # Основные цвета
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    
    # Яркие цвета
    BRIGHT_RED = "\033[91;1m"
    BRIGHT_GREEN = "\033[92;1m"
    BRIGHT_YELLOW = "\033[93;1m"
    BRIGHT_BLUE = "\033[94;1m"
    
    # Фоны
    BG_RED = "\033[41m"
    BG_BLUE = "\033[44m"
    BG_BLACK = "\033[40m"
    
    # Цвета персонажей
    CHARACTER_COLORS = {
        "max_well": CYAN,
        "athena": MAGENTA,
        "alia_naar": BLUE,
        "irina_lebedeva": GREEN,
        "rina_mirai": YELLOW,
        "nadezhda": RED,
        "ekaterina": CYAN,
    }
    
    @classmethod
    def supports_color(cls) -> bool:
        """Проверить поддержку цвета в терминале"""
        if not hasattr(sys.stdout, "isatty"):
            return False
        if not sys.stdout.isatty():
            return False
        if sys.platform == "win32":
            try:
                import colorama
                colorama.init()
                return True
            except ImportError:
                return False
        return True
    
    @classmethod
    def disable(cls):
        """Отключить цвета"""
        cls.RESET = ""
        cls.BOLD = ""
        cls.DIM = ""
        cls.RED = ""
        cls.GREEN = ""
        cls.YELLOW = ""
        cls.BLUE = ""
        cls.MAGENTA = ""
        cls.CYAN = ""
        cls.WHITE = ""
        cls.BRIGHT_RED = ""
        cls.BRIGHT_GREEN = ""
        cls.BRIGHT_YELLOW = ""
        cls.BRIGHT_BLUE = ""
        cls.BG_RED = ""
        cls.BG_BLUE = ""
        cls.BG_BLACK = ""
        cls.CHARACTER_COLORS = {k: "" for k in cls.CHARACTER_COLORS}


def colorize(text: str, color: str) -> str:
    """Обернуть текст в цвет"""
    return f"{color}{text}{Colors.RESET}"


def print_colored(text: str, color: str):
    """Вывести цветной текст"""
    print(colorize(text, color))


def print_alert(text: str):
    """Вывести предупреждение (красный)"""
    print_colored(text, Colors.BRIGHT_RED)


def print_info(text: str):
    """Вывести информацию (синий)"""
    print_colored(text, Colors.BLUE)


def print_success(text: str):
    """Вывести успех (зелёный)"""
    print_colored(text, Colors.GREEN)


def get_character_color(char_id: str) -> str:
    """Получить цвет персонажа"""
    return Colors.CHARACTER_COLORS.get(char_id, Colors.WHITE)
