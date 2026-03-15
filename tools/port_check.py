#!/usr/bin/env python3
"""
Star Courier - Port Check Utility
Проверка доступности порта для запуска игры
"""

import socket
import sys


def check_port(port: int, host: str = 'localhost') -> bool:
    """
    Проверить, свободен ли порт.
    Returns True если порт свободен.
    """
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    try:
        sock.bind((host, port))
        return True
    except OSError:
        return False
    finally:
        sock.close()


def find_available_port(start_port: int = 8000, end_port: int = 9000) -> int:
    """
    Найти свободный порт в диапазоне.
    Returns номер порта или -1 если не найдено.
    """
    for port in range(start_port, end_port + 1):
        if check_port(port):
            return port
    return -1


def main():
    """Основная функция"""
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
            if check_port(port):
                print(f"Порт {port} свободен ✓")
                sys.exit(0)
            else:
                print(f"Порт {port} занят ✗")
                sys.exit(1)
        except ValueError:
            print("Ошибка: номер порта должен быть числом")
            sys.exit(1)
    else:
        port = find_available_port()
        if port > 0:
            print(f"Свободный порт: {port}")
            sys.exit(0)
        else:
            print("Не удалось найти свободный порт")
            sys.exit(1)


if __name__ == "__main__":
    main()
