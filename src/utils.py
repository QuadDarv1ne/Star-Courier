"""
Утилиты для работы с текстом и файлами
Расширенная версия с анимациями и эффектами
"""

import os
import sys
import time
import logging
from typing import List, Optional
from pathlib import Path

logger = logging.getLogger('utils')


def clear_screen():
    """Очистить экран консоли"""
    os.system("cls" if os.name == "nt" else "clear")


def print_slow(text: str, delay: float = 0.02, width: int = 80):
    """
    Вывод текста с задержкой между словами.

    Args:
        text: Текст для вывода
        delay: Задержка между словами (сек)
        width: Ширина строки
    """
    words = text.split()
    line = ""
    output_buffer = []

    for word in words:
        if len(line) + len(word) + 1 > width:
            if line:
                output_buffer.append(line)
            line = word
        else:
            line = f"{line} {word}".strip()

    if line:
        output_buffer.append(line)

    for line in output_buffer:
        print(line, flush=True)
        time.sleep(delay)

    print()


def print_typewriter(text: str, delay: float = 0.03):
    """
    Эффект печатной машинки — посимвольный вывод.

    Args:
        text: Текст для вывода
        delay: Задержка между символами (сек)
    """
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


def print_typewriter_colored(text: str, delay: float = 0.03, color: str = ""):
    """
    Эффект печатной машинки с цветом.

    Args:
        text: Текст для вывода
        delay: Задержка между символами (сек)
        color: ANSI код цвета
    """
    from .colors import colorize

    for char in text:
        if color:
            print(colorize(char, color), end="", flush=True)
        else:
            print(char, end="", flush=True)
        time.sleep(delay)
    print()


def print_glitch(text: str, delay: float = 0.05, glitch_chars: str = "░▒▓█▀▄"):
    """
    Эффект глитча/помех для текста.
    
    Args:
        text: Текст для вывода
        delay: Задержка между символами
        glitch_chars: Символы для эффекта глитча
    """
    import random
    
    for char in text:
        if char == " " or random.random() > 0.3:
            print(char, end="", flush=True)
        else:
            # Показываем случайный символ глитча
            glitch_char = random.choice(glitch_chars)
            print(glitch_char, end="", flush=True)
            time.sleep(delay / 2)
            # Возвращаем оригинальный символ
            print("\b" + char, end="", flush=True)
        time.sleep(delay)
    print()


def print_digital_rain(text: str, delay: float = 0.1):
    """
    Эффект «цифрового дождя» в стиле Матрицы.
    Выводит текст по одной строке с эффектом падения.
    
    Args:
        text: Текст для вывода
        delay: Задержка между строками
    """
    lines = text.split("\n")
    digital_chars = "01ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶﾑﾕﾗｾﾈｽﾀﾇﾍｦｲｸｺ"
    
    for line in lines:
        # Сначала показываем «падающие» символы
        for _ in range(3):
            print("".join(__import__('random').choice(digital_chars) for _ in range(len(line))), 
                  end="\r", flush=True)
            time.sleep(delay / 3)
        
        # Затем показываем реальную строку
        print(line, end="\r", flush=True)
        time.sleep(delay)
        print(line)
    
    print()


def print_wave(text: str, delay: float = 0.1, amplitude: int = 3):
    """
    Вывод текста волной.
    
    Args:
        text: Текст для вывода
        delay: Задержка между символами
        amplitude: Амплитуда волны (сдвиг строк)
    """
    import math
    
    lines = []
    for i, char in enumerate(text):
        if char == " ":
            lines.append((" ", 0))
            continue
        
        offset = int(amplitude * math.sin(i * 0.5))
        lines.append((char, offset))
    
    # Группируем по строкам
    max_offset = max(off for _, off in lines) if lines else 0
    min_offset = min(off for _, off in lines) if lines else 0
    
    for row in range(min_offset, max_offset + 1):
        line_chars = []
        for char, offset in lines:
            if offset == row:
                line_chars.append(char)
            else:
                line_chars.append(" ")
        print("".join(line_chars))
        time.sleep(delay * 2)
    
    print()


def print_fade_in(text: str, delay: float = 0.05):
    """
    Эффект плавного появления текста.
    
    Args:
        text: Текст для вывода
        delay: Задержка между шагами
    """
    # Символы для эффекта появления
    fade_chars = " ░▒▓█"
    
    for i, char in enumerate(text):
        # Показываем символ с нарастающей «яркостью»
        for fade_char in fade_chars:
            print(fade_char, end="\b", flush=True)
            time.sleep(delay / len(fade_chars))
        print(char, end="", flush=True)
    
    print()


def print_reveal(text: str, delay: float = 0.03, reveal_char: str = "_"):
    """
    Эффект «проявления» текста.

    Args:
        text: Текст для вывода
        delay: Задержка между символами
        reveal_char: Символ-заполнитель
    """
    print(reveal_char * len(text), end="", flush=True)
    time.sleep(delay * 2)

    for i, char in enumerate(text):
        print("\b" + char, end="", flush=True)
        time.sleep(delay)

    print()


def print_scroll(text: str, delay: float = 0.02, direction: str = "left"):
    """
    Эффект прокрутки текста.
    
    Args:
        text: Текст для вывода
        delay: Задержка между шагами
        direction: Направление прокрутки (left/right/up/down)
    """
    if direction == "left":
        # Прокрутка справа налево
        padded = " " * 20 + text + " " * 20
        for i in range(len(padded) - 40):
            print("\r" + padded[i:i+40], end="", flush=True)
            time.sleep(delay)
        print()
    
    elif direction == "right":
        # Прокрутка слева направо
        padded = " " * 20 + text + " " * 20
        for i in range(len(padded) - 40, -1, -1):
            print("\r" + padded[i:i+40], end="", flush=True)
            time.sleep(delay)
        print()


def print_bounce(text: str, bounces: int = 3, delay: float = 0.1):
    """
    Эффект «подпрыгивания» текста.
    
    Args:
        text: Текст для вывода
        bounces: Количество подпрыгиваний
        delay: Задержка между кадрами
    """
    max_indent = 20
    
    for _ in range(bounces):
        # Вправо
        for i in range(max_indent):
            print("\r" + " " * i + text, end="", flush=True)
            time.sleep(delay)
        # Влево
        for i in range(max_indent, 0, -1):
            print("\r" + " " * i + text, end="", flush=True)
            time.sleep(delay)
    
    print("\r" + text, end="", flush=True)
    print()


def print_spinner(duration: float = 2.0, message: str = "Загрузка..."):
    """
    Показывать спиннер загрузки.

    Args:
        duration: Длительность показа (сек)
        message: Сообщение рядом со спиннером
    """
    spinner_chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
    start_time = time.time()

    try:
        while time.time() - start_time < duration:
            for char in spinner_chars:
                print(f"\r{char} {message}", end="", flush=True)
                time.sleep(0.1)
                if time.time() - start_time >= duration:
                    break
    except KeyboardInterrupt:
        pass

    print(f"\r✓ {message}", end="", flush=True)
    print()


def print_progress_bar(current: int, total: int, width: int = 40, fill: str = "█", empty: str = "░"):
    """
    Отобразить прогресс-бар.
    
    Args:
        current: Текущий прогресс
        total: Всего
        width: Ширина в символах
        fill: Символ заполнения
        empty: Символ пустого места
    """
    percent = current / total if total > 0 else 0
    filled = int(width * percent)
    bar = fill * filled + empty * (width - filled)
    print(f"\r[{bar}] {percent*100:.1f}%", end="", flush=True)


def animate_dialogue(text: str, speaker: str = "", delay: float = 0.03,
                     show_name: bool = True, color: str = ""):
    """
    Анимированный вывод диалога.

    Args:
        text: Текст реплики
        speaker: Имя говорящего
        delay: Задержка между символами
        show_name: Показывать ли имя
        color: Цвет текста
    """
    from .colors import colorize, style_text

    if show_name and speaker:
        name_display = f"[{speaker}]"
        if color:
            print(colorize(name_display, color))
        else:
            print(style_text(name_display, bold=True))
        print()

    if color:
        print_typewriter_colored(text, delay, color)
    else:
        print_typewriter(text, delay)


def type_with_sound(text: str, delay: float = 0.05, beep: bool = False):
    """
    Печатная машинка со звуком (опционально).
    Требует установки библиотеки playsound или аналогичной.

    Args:
        text: Текст для вывода
        delay: Задержка между символами
        beep: Воспроизводить ли звук
    """
    for char in text:
        print(char, end="", flush=True)
        if beep:
            sys.stdout.write('\a')
            sys.stdout.flush()
        time.sleep(delay)
    print()


def _get_int_input(prompt: str, min_val: int = None, max_val: int = None) -> Optional[int]:
    """Вспомогательная функция для получения целого числа"""
    try:
        choice = input(prompt).strip()
        if not choice:
            return None
        idx = int(choice) - 1
        if min_val is not None and idx < min_val:
            return None
        if max_val is not None and idx > max_val:
            return None
        return idx
    except ValueError:
        logger.debug(f"Неверный ввод: ожидалось число")
        return None
    except KeyboardInterrupt:
        print("\n")
        raise


def get_choice(prompt: str, options: List[str]) -> int:
    """
    Получить выбор от пользователя.

    Args:
        prompt: Текст запроса
        options: Список вариантов

    Returns:
        Индекс выбранного варианта (0-based)
    """
    print(f"\n{prompt}\n")

    if not options:
        logger.warning("get_choice вызван с пустым списком опций")
        return -1

    for i, option in enumerate(options, 1):
        print(f"  [{i}] {option}")

    while True:
        idx = _get_int_input("\nВаш выбор: ", 0, len(options) - 1)
        if idx is not None:
            return idx
        print(f"Введите число от 1 до {len(options)}")


def confirm(prompt: str = "Вы уверены?") -> bool:
    """
    Запрос подтверждения.

    Args:
        prompt: Текст запроса

    Returns:
        True если подтверждено
    """
    try:
        choice = input(f"{prompt} (y/n): ").strip().lower()
        return choice in ("y", "yes", "да", "д")
    except (KeyboardInterrupt, EOFError):
        print()
        return False


def print_separator(char: str = "—", length: int = 60):
    """Вывести разделитель"""
    print(char * length)


def print_header(text: str, width: int = 60):
    """
    Вывести заголовок в рамке.

    Args:
        text: Текст заголовка
        width: Ширина рамки
    """
    border = "+" + "-" * (width - 2) + "+"
    print(border)

    padding_left = (width - 2 - len(text)) // 2
    padding_right = width - 2 - padding_left - len(text)
    # Заменяем Unicode-символы на ASCII для совместимости с Windows
    safe_text = text.replace("\u2605", "*").replace("\u2550", "=").replace("\u2501", "-")
    print(f"|{' ' * padding_left}{safe_text}{' ' * padding_right}|")

    print(border)
    print()


def print_menu(title: str, options: List[str]) -> int:
    """
    Вывести меню и получить выбор.

    Args:
        title: Заголовок меню
        options: Список опций

    Returns:
        Индекс выбранной опции (0-based)
    """
    clear_screen()
    print_header(title)

    for i, option in enumerate(options, 1):
        print(f"  {i}. {option}")

    print()

    while True:
        idx = _get_int_input("Выберите пункт: ", 0, len(options) - 1)
        if idx is not None:
            return idx
        print(f"Введите число от 1 до {len(options)}")


def list_saves_menu(saves: list) -> None:
    """
    Вывести список сохранений.

    Args:
        saves: Список сохранений
    """
    if not saves:
        print("  Нет сохранений")
        return

    print(f"  Доступные сохранения ({len(saves)}):")
    for i, save in enumerate(saves[:5], 1):
        print(f"    {i}. {save['timestamp']} — Глава {save['chapter']}")
    if len(saves) > 5:
        print(f"    ... и ещё {len(saves) - 5}")


def wrap_text(text: str, width: int = 80) -> List[str]:
    """
    Разбить текст на строки заданной ширины.

    Args:
        text: Текст
        width: Максимальная ширина строки

    Returns:
        Список строк
    """
    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > width:
            if current_line:
                lines.append(current_line)
            current_line = word
        else:
            current_line = f"{current_line} {word}".strip()

    if current_line:
        lines.append(current_line)

    return lines


def extract_text_from_docx(filepath: str) -> Optional[str]:
    """
    Извлечь текст из .docx файла.

    Args:
        filepath: Путь к файлу

    Returns:
        Текст или None при ошибке
    """
    try:
        from docx import Document

        doc = Document(filepath)
        paragraphs = [p.text for p in doc.paragraphs if p.text.strip()]
        return "\n\n".join(paragraphs)
    except Exception as e:
        logger.error(f"Ошибка чтения {filepath}: {e}")
        return None


def list_docx_files(directory: str, recursive: bool = False) -> List[Path]:
    """
    Найти все .docx файлы в директории.
    
    Args:
        directory: Путь к директории
        recursive: Искать рекурсивно
    
    Returns:
        Список путей к файлам
    """
    path = Path(directory)
    if recursive:
        return list(path.rglob("*.docx"))
    return list(path.glob("*.docx"))


def resource_path(relative_path: str) -> str:
    """
    Получить абсолютный путь к ресурсу.
    Работает как для обычной разработки, так и для PyInstaller.
    
    Args:
        relative_path: Относительный путь
    
    Returns:
        Абсолютный путь
    """
    if hasattr(sys, "_MEIPASS"):
        # PyInstaller создаёт временную папку _MEIPASS
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)
