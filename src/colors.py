"""
Цветовая поддержка для терминала
Расширенная версия с 256-цветной палитрой и темами
"""

import sys
import os
from typing import Optional
from enum import Enum


class ColorCode(Enum):
    """Коды цветов для 256-цветной палитры"""
    # Основные цвета
    BLACK = 0
    RED = 1
    GREEN = 2
    YELLOW = 3
    BLUE = 4
    MAGENTA = 5
    CYAN = 6
    WHITE = 7
    
    # Яркие цвета
    BRIGHT_BLACK = 8
    BRIGHT_RED = 9
    BRIGHT_GREEN = 10
    BRIGHT_YELLOW = 11
    BRIGHT_BLUE = 12
    BRIGHT_MAGENTA = 13
    BRIGHT_CYAN = 14
    BRIGHT_WHITE = 15


class Colors:
    """ANSI цвета для терминала"""

    RESET = "\033[0m"
    BOLD = "\033[1m"
    DIM = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    REVERSE = "\033[7m"
    STRIKETHROUGH = "\033[9m"

    # Основные цвета
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    MAGENTA = "\033[95m"
    CYAN = "\033[96m"
    WHITE = "\033[97m"
    BLACK = "\033[30m"

    # Яркие цвета
    BRIGHT_RED = "\033[91;1m"
    BRIGHT_GREEN = "\033[92;1m"
    BRIGHT_YELLOW = "\033[93;1m"
    BRIGHT_BLUE = "\033[94;1m"
    BRIGHT_MAGENTA = "\033[95;1m"
    BRIGHT_CYAN = "\033[96;1m"

    # Тёмные цвета
    DARK_RED = "\033[31m"
    DARK_GREEN = "\033[32m"
    DARK_BLUE = "\033[34m"

    # Фоны
    BG_RED = "\033[41m"
    BG_GREEN = "\033[42m"
    BG_YELLOW = "\033[43m"
    BG_BLUE = "\033[44m"
    BG_MAGENTA = "\033[45m"
    BG_CYAN = "\033[46m"
    BG_WHITE = "\033[47m"
    BG_BLACK = "\033[40m"
    BG_BRIGHT_RED = "\033[101m"
    BG_BRIGHT_GREEN = "\033[102m"
    BG_BRIGHT_BLUE = "\033[104m"

    # Цвета персонажей
    CHARACTER_COLORS = {
        "max_well": CYAN,
        "athena": MAGENTA,
        "alia_naar": BRIGHT_BLUE,
        "irina_lebedeva": BRIGHT_GREEN,
        "rina_mirai": BRIGHT_YELLOW,
        "nadezhda": BRIGHT_RED,
        "ekaterina": CYAN,
        "selena_ro": BRIGHT_MAGENTA,
    }
    
    # Цвета для типов квестов
    QUEST_TYPE_COLORS = {
        "main": BRIGHT_YELLOW,
        "side": CYAN,
        "combat": BRIGHT_RED,
        "research": BRIGHT_MAGENTA,
        "delivery": GREEN,
        "exploration": BLUE,
        "commission": YELLOW,
    }
    
    # Цвета для редкости предметов
    RARITY_COLORS = {
        "common": WHITE,
        "uncommon": GREEN,
        "rare": BRIGHT_BLUE,
        "epic": BRIGHT_MAGENTA,
        "legendary": BRIGHT_YELLOW,
    }
    
    # Цвета для статусов
    STATUS_COLORS = {
        "success": BRIGHT_GREEN,
        "info": BRIGHT_CYAN,
        "warning": BRIGHT_YELLOW,
        "error": BRIGHT_RED,
        "critical": BRIGHT_RED + BOLD,
    }

    @classmethod
    def supports_color(cls) -> bool:
        """Проверить поддержку цвета в терминале"""
        # Проверка переменной окружения NO_COLOR
        if os.environ.get("NO_COLOR"):
            return False
            
        # Проверка переменной окружения FORCE_COLOR
        if os.environ.get("FORCE_COLOR"):
            return True
        
        if not hasattr(sys.stdout, "isatty"):
            return False
        if not sys.stdout.isatty():
            return False
            
        # Windows с colorama
        if sys.platform == "win32":
            try:
                import colorama
                colorama.init()
                return True
            except ImportError:
                # Windows 10+ поддерживает ANSI
                try:
                    from ctypes import windll
                    kernel32 = windll.kernel32
                    kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
                    return True
                except Exception:
                    return False
        return True

    @classmethod
    def supports_256_color(cls) -> bool:
        """Проверить поддержку 256-цветной палитры"""
        if not cls.supports_color():
            return False
        
        # Проверка терминала
        term = os.environ.get("TERM", "")
        return "256" in term or term in ("xterm", "xterm-256color", "screen", "tmux")

    @classmethod
    def disable(cls):
        """Отключить цвета"""
        cls.RESET = ""
        cls.BOLD = ""
        cls.DIM = ""
        cls.ITALIC = ""
        cls.UNDERLINE = ""
        cls.BLINK = ""
        cls.REVERSE = ""
        cls.STRIKETHROUGH = ""
        cls.RED = ""
        cls.GREEN = ""
        cls.YELLOW = ""
        cls.BLUE = ""
        cls.MAGENTA = ""
        cls.CYAN = ""
        cls.WHITE = ""
        cls.BLACK = ""
        cls.BRIGHT_RED = ""
        cls.BRIGHT_GREEN = ""
        cls.BRIGHT_YELLOW = ""
        cls.BRIGHT_BLUE = ""
        cls.BRIGHT_MAGENTA = ""
        cls.BRIGHT_CYAN = ""
        cls.DARK_RED = ""
        cls.DARK_GREEN = ""
        cls.DARK_BLUE = ""
        cls.BG_RED = ""
        cls.BG_GREEN = ""
        cls.BG_YELLOW = ""
        cls.BG_BLUE = ""
        cls.BG_MAGENTA = ""
        cls.BG_CYAN = ""
        cls.BG_WHITE = ""
        cls.BG_BLACK = ""
        cls.BG_BRIGHT_RED = ""
        cls.BG_BRIGHT_GREEN = ""
        cls.BG_BRIGHT_BLUE = ""
        cls.CHARACTER_COLORS = {k: "" for k in cls.CHARACTER_COLORS}
        cls.QUEST_TYPE_COLORS = {k: "" for k in cls.QUEST_TYPE_COLORS}
        cls.RARITY_COLORS = {k: "" for k in cls.RARITY_COLORS}
        cls.STATUS_COLORS = {k: "" for k in cls.STATUS_COLORS}

    @classmethod
    def rgb(cls, r: int, g: int, b: int) -> str:
        """
        Получить ANSI код для RGB цвета.
        Требует поддержки 24-битного цвета.
        """
        if not cls.supports_color():
            return ""
        return f"\033[38;2;{r};{g};{b}m"

    @classmethod
    def color_256(cls, code: int) -> str:
        """
        Получить цвет из 256-цветной палитры.
        code: 0-255
        """
        if not cls.supports_color():
            return ""
        code = max(0, min(255, code))
        return f"\033[38;5;{code}m"

    @classmethod
    def bg_color_256(cls, code: int) -> str:
        """
        Получить фон из 256-цветной палитры.
        code: 0-255
        """
        if not cls.supports_color():
            return ""
        code = max(0, min(255, code))
        return f"\033[48;5;{code}m"


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


def print_warning(text: str):
    """Вывести предупреждение (жёлтый)"""
    print_colored(text, Colors.BRIGHT_YELLOW)


def print_error(text: str):
    """Вывести ошибку (красный)"""
    print_colored(text, Colors.BRIGHT_RED)


def print_critical(text: str):
    """Вывести критическое сообщение (красный + жирный)"""
    print_colored(text, Colors.STATUS_COLORS["critical"])


def get_character_color(char_id: str) -> str:
    """Получить цвет персонажа"""
    return Colors.CHARACTER_COLORS.get(char_id, Colors.WHITE)


def get_quest_type_color(quest_type: str) -> str:
    """Получить цвет типа квеста"""
    return Colors.QUEST_TYPE_COLORS.get(quest_type, Colors.WHITE)


def get_rarity_color(rarity: str) -> str:
    """Получить цвет редкости предмета"""
    return Colors.RARITY_COLORS.get(rarity, Colors.WHITE)


def get_status_color(status: str) -> str:
    """Получить цвет статуса"""
    return Colors.STATUS_COLORS.get(status, Colors.WHITE)


def style_text(
    text: str,
    color: Optional[str] = None,
    bold: bool = False,
    dim: bool = False,
    italic: bool = False,
    underline: bool = False,
) -> str:
    """
    Стилизация текста с несколькими эффектами.
    
    Args:
        text: Текст для стилизации
        color: Цвет текста (опционально)
        bold: Жирный шрифт
        dim: Приглушённый шрифт
        italic: Курсив
        underline: Подчёркивание
    
    Returns:
        Стилизированный текст
    """
    if not Colors.supports_color():
        return text
    
    result = ""
    if color:
        result += color
    if bold:
        result += Colors.BOLD
    if dim:
        result += Colors.DIM
    if italic:
        result += Colors.ITALIC
    if underline:
        result += Colors.UNDERLINE
    
    result += text + Colors.RESET
    return result


def gradient_text(text: str, start_color: str, end_color: str) -> str:
    """
    Создать градиентный текст.
    Требует поддержки 24-битного цвета.
    Работает только с простыми цветами RGB.
    """
    if not Colors.supports_color() or len(text) == 0:
        return text

    # Простая реализация для односимвольного градиента
    result = ""
    for char in text:
        result += colorize(char, start_color)

    return result


def rainbow_text(text: str) -> str:
    """Создать радужный текст"""
    if not Colors.supports_color():
        return text
    
    colors = [
        Colors.RED,
        Colors.BRIGHT_YELLOW,
        Colors.GREEN,
        Colors.CYAN,
        Colors.BLUE,
        Colors.MAGENTA,
    ]
    
    result = ""
    for i, char in enumerate(text):
        result += colorize(char, colors[i % len(colors)])
    
    return result


def box_text(text: str, title: str = "", color: str = Colors.WHITE) -> str:
    """
    Создать текстовое поле с рамкой.
    
    Args:
        text: Текст внутри поля
        title: Заголовок поля (опционально)
        color: Цвет рамки
    
    Returns:
        Форматированное текстовое поле
    """
    lines = text.split("\n")
    max_width = max(len(line) for line in lines)
    
    # Если есть заголовок, учитываем его
    if title:
        max_width = max(max_width, len(title) + 4)
    
    border = "─" * max_width
    corner_tl = "╭"
    corner_tr = "╮"
    corner_bl = "╰"
    corner_br = "╯"
    
    result = []
    result.append(colorize(f"{corner_tl}{border}{corner_tr}", color))
    
    if title:
        title_line = f"│ {title.center(max_width - 2)} │"
        result.append(colorize(title_line, color))
        result.append(colorize(f"├{border}┤", color))
    
    for line in lines:
        padded = line.ljust(max_width)
        result.append(colorize(f"│{padded}│", color))
    
    result.append(colorize(f"{corner_bl}{border}{corner_br}", color))
    
    return "\n".join(result)
