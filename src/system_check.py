# -*- coding: utf-8 -*-
"""
Star Courier - System Check Utility
Проверка системных требований и доступности порта
"""

import sys
import socket
import platform
from typing import Tuple, Optional


def check_python_version() -> Tuple[bool, str]:
    """Проверить версию Python"""
    required = (3, 8)
    current = sys.version_info[:2]
    
    if current >= required:
        version_str = f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        return True, f"Python {version_str}"
    else:
        return False, f"Требуется Python {'.'.join(map(str, required))} или выше"


def check_port_available(port: int, host: str = 'localhost') -> Tuple[bool, str]:
    """
    Проверить, доступен ли порт для использования.
    
    Args:
        port: Номер порта для проверки
        host: Хост для проверки (по умолчанию localhost)
    
    Returns:
        Tuple[bool, str]: (доступен, сообщение)
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind((host, port))
            return True, f"Порт {port} доступен на {host}"
    except OSError as e:
        return False, f"Порт {port} занят на {host}: {e}"
    except Exception as e:
        return False, f"Ошибка проверки порта {port}: {e}"


def find_available_port(start_port: int = 8000, end_port: int = 9000, 
                        host: str = 'localhost') -> Tuple[Optional[int], str]:
    """
    Найти первый доступный порт в диапазоне.
    
    Args:
        start_port: Начальный порт диапазона
        end_port: Конечный порт диапазона
        host: Хост для проверки
    
    Returns:
        Tuple[Optional[int], str]: (номер порта или None, сообщение)
    """
    for port in range(start_port, end_port + 1):
        available, _ = check_port_available(port, host)
        if available:
            return port, f"Найден доступный порт: {port}"
    
    return None, f"Нет доступных портов в диапазоне {start_port}-{end_port}"


def check_memory() -> Tuple[bool, str]:
    """Проверить доступную память"""
    try:
        import psutil
        available_mb = psutil.virtual_memory().available / (1024 * 1024)
        if available_mb >= 256:
            return True, f"Доступно памяти: {available_mb:.0f} MB"
        else:
            return False, f"Недостаточно памяти: {available_mb:.0f} MB (требуется 256 MB)"
    except ImportError:
        return True, "Модуль psutil не установлен, проверка памяти пропущена"


def check_disk_space() -> Tuple[bool, str]:
    """Проверить место на диске"""
    try:
        import psutil
        disk = psutil.disk_usage('.')
        available_gb = disk.free / (1024 * 1024 * 1024)
        if available_gb >= 1:
            return True, f"Свободно на диске: {available_gb:.1f} GB"
        else:
            return False, f"Недостаточно места: {available_gb:.1f} GB (требуется 1 GB)"
    except ImportError:
        return True, "Модуль psutil не установлен, проверка диска пропущена"


def check_encoding() -> Tuple[bool, str]:
    """Проверить поддержку UTF-8"""
    encoding = sys.getfilesystemencoding()
    if 'utf-8' in encoding.lower():
        return True, f"Кодировка файловой системы: {encoding}"
    else:
        return True, f"Кодировка: {encoding} (рекомендуется UTF-8)"


def check_terminal_support() -> Tuple[bool, str]:
    """Проверить поддержку терминала"""
    # Проверка на Windows
    if platform.system() == 'Windows':
        try:
            from ctypes import windll
            kernel32 = windll.kernel32
            h = kernel32.GetStdHandle(-11)  # STD_OUTPUT_HANDLE
            mode = windll.c_ulong()
            if kernel32.GetConsoleMode(h, mode):
                # Попробовать включить VT100
                mode.value |= 0x0004  # ENABLE_VIRTUAL_TERMINAL_PROCESSING
                if kernel32.SetConsoleMode(h, mode):
                    return True, "Windows Console с поддержкой ANSI"
            return True, "Windows Console (базовая поддержка)"
        except Exception:
            return True, "Windows Console (ограниченная поддержка)"
    else:
        return True, f"Unix-терминал ({platform.system()})"


def run_system_check(include_port_check: bool = False, 
                     port: int = None) -> dict:
    """
    Запустить полную проверку системы.
    
    Args:
        include_port_check: Включить проверку порта
        port: Номер порта для проверки (если включено)
    
    Returns:
        dict: Результаты проверок
    """
    results = {
        'success': True,
        'checks': []
    }
    
    # Проверка версии Python
    success, msg = check_python_version()
    results['checks'].append(('Python', success, msg))
    if not success:
        results['success'] = False
    
    # Проверка кодировки
    success, msg = check_encoding()
    results['checks'].append(('Кодировка', success, msg))
    
    # Проверка терминала
    success, msg = check_terminal_support()
    results['checks'].append(('Терминал', success, msg))
    
    # Проверка памяти
    success, msg = check_memory()
    results['checks'].append(('Память', success, msg))
    
    # Проверка диска
    success, msg = check_disk_space()
    results['checks'].append(('Диск', success, msg))
    
    # Проверка порта (опционально)
    if include_port_check and port:
        success, msg = check_port_available(port)
        results['checks'].append(('Порт', success, msg))
        if not success:
            # Попробовать найти другой порт
            alt_port, alt_msg = find_available_port(8000, 9000)
            results['checks'].append(('Альтернативный порт', alt_port is not None, alt_msg))
    
    return results


def print_system_check(include_port_check: bool = False,
                       port: int = None) -> bool:
    """
    Вывести результаты проверки системы.
    
    Args:
        include_port_check: Включить проверку порта
        port: Номер порта для проверки
    
    Returns:
        bool: Все ли проверки пройдены
    """
    print("\n" + "=" * 60)
    print("  ПРОВЕРКА СИСТЕМНЫХ ТРЕБОВАНИЙ")
    print("=" * 60)
    
    results = run_system_check(include_port_check, port)
    
    all_passed = True
    for name, success, msg in results['checks']:
        status = "✓" if success else "✗"
        print(f"  [{status}] {name}: {msg}")
        if not success:
            all_passed = False
    
    print("=" * 60)
    
    if all_passed:
        print("  ✓ Все проверки пройдены успешно!")
    else:
        print("  ✗ Некоторые проверки не пройдены!")
    
    print()
    return all_passed


def main():
    """Точка входа для утилиты"""
    import argparse
    
    parser = argparse.ArgumentParser(
        description='Проверка системных требований Star Courier'
    )
    parser.add_argument(
        '--port', '-p',
        type=int,
        default=None,
        help='Номер порта для проверки (опционально)'
    )
    parser.add_argument(
        '--find-port', '-f',
        action='store_true',
        help='Найти доступный порт в диапазоне 8000-9000'
    )
    parser.add_argument(
        '--quiet', '-q',
        action='store_true',
        help='Тихий режим (только результат)'
    )
    
    args = parser.parse_args()
    
    if args.find_port:
        port, msg = find_available_port(8000, 9000)
        if port:
            print(f"✓ {msg}")
            sys.exit(0)
        else:
            print(f"✗ {msg}")
            sys.exit(1)
    
    if args.quiet:
        results = run_system_check(args.port is not None, args.port)
        sys.exit(0 if results['success'] else 1)
    
    success = print_system_check(args.port is not None, args.port)
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()
