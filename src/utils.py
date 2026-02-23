"""
Утилиты для работы с текстом и файлами
"""

import os
import sys
from typing import List, Optional
from pathlib import Path


def clear_screen():
    """Очистить экран консоли"""
    os.system("cls" if os.name == "nt" else "clear")


def print_slow(text: str, delay: float = 0.02, width: int = 80):
    """
    Вывод текста с задержкой между символами.
    
    Args:
        text: Текст для вывода
        delay: Задержка между символами (сек)
        width: Ширина строки
    """
    import time
    
    words = text.split()
    line = ""
    
    for word in words:
        if len(line) + len(word) + 1 > width:
            print(line)
            line = word + " "
        else:
            line += word + " "
        
        # Печатаем слово целиком для производительности
        print(word, end=" ", flush=True)
        time.sleep(delay * len(word))  # Задержка зависит от длины слова
    
    if line:
        print(line)
    
    print()  # Пустая строка в конце


def print_typewriter(text: str, delay: float = 0.03):
    """
    Эффект печатной машинки — посимвольный вывод.
    
    Args:
        text: Текст для вывода
        delay: Задержка между символами (сек)
    """
    import time
    
    for char in text:
        print(char, end="", flush=True)
        time.sleep(delay)
    print()


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
        try:
            choice = input("\nВаш выбор: ").strip()
            if not choice:
                print("Введите число")
                continue
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return idx
            print(f"Введите число от 1 до {len(options)}")
        except ValueError:
            print("Введите число")
        except KeyboardInterrupt:
            print("\n")
            raise


def confirm(prompt: str = "Вы уверены?") -> bool:
    """
    Запрос подтверждения.
    
    Args:
        prompt: Текст запроса
    
    Returns:
        True если подтверждено
    """
    choice = input(f"{prompt} (y/n): ").strip().lower()
    return choice in ("y", "yes", "да", "д")


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
    print("+" + "-" * (width - 2) + "+")
    
    # Центрирование текста
    padding = (width - 2 - len(text)) // 2
    line = "|" + " " * padding + text + " " * (width - 2 - padding - len(text)) + "|"
    print(line)
    
    print("+" + "-" * (width - 2) + "+")
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
        try:
            choice = input("Выберите пункт: ").strip()
            if not choice:
                print("Введите число")
                continue
            idx = int(choice) - 1
            if 0 <= idx < len(options):
                return idx
            print(f"Введите число от 1 до {len(options)}")
        except ValueError:
            print("Введите число")
        except KeyboardInterrupt:
            print("\n")
            raise


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
            if current_line:
                current_line += " " + word
            else:
                current_line = word
    
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
        print(f"Ошибка чтения {filepath}: {e}")
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
