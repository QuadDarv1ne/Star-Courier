"""
Утилиты для работы с текстом и файлами
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
